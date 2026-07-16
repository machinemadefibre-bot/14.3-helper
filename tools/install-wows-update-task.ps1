param(
    [ValidateSet("Install", "Uninstall", "Show", "SelfTest")]
    [string]$Mode = "Install",
    [string]$SourceRepoRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$AutomationWorktree = "",
    [string]$TaskName = "WoWS Armor Update (Standalone)",
    [string]$DailyAt = "08:00",
    [string]$GameDir = "S:\SteamLibrary\steamapps\common\World of Warships",
    [string]$SteamManifest = "S:\SteamLibrary\steamapps\appmanifest_552990.acf"
)

$ErrorActionPreference = "Stop"

function Invoke-Git {
    param([string[]]$Arguments)

    $output = @(& git -C $SourceRepoRoot @Arguments 2>&1)
    if ($LASTEXITCODE -ne 0) {
        throw "git $($Arguments -join ' ') failed: $($output -join [Environment]::NewLine)"
    }
    return @($output)
}

function ConvertTo-QuotedArgument {
    param([string]$Value)

    if ($Value -notmatch '[\s"]') { return $Value }
    return '"' + $Value.Replace('"', '\"') + '"'
}

function Get-TaskSummary {
    $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction Stop
    $info = Get-ScheduledTaskInfo -TaskName $TaskName -ErrorAction Stop
    return [ordered]@{
        status = "TASK_PRESENT"
        taskName = $TaskName
        state = [string]$task.State
        nextRunTime = $info.NextRunTime.ToString("o")
        lastRunTime = $info.LastRunTime.ToString("o")
        lastTaskResult = $info.LastTaskResult
        execute = [string]$task.Actions[0].Execute
        arguments = [string]$task.Actions[0].Arguments
        workingDirectory = [string]$task.Actions[0].WorkingDirectory
    }
}

function Assert-DevelopWorktree {
    if (-not (Test-Path -LiteralPath (Join-Path $AutomationWorktree ".git"))) {
        $sourceBranch = ((Invoke-Git @("branch", "--show-current")) | Select-Object -First 1).Trim()
        if ($sourceBranch -eq "develop") {
            throw "WORKTREE_CREATE_BLOCKED: switch the source checkout to main before creating the develop automation worktree."
        }
        $null = Invoke-Git @("worktree", "add", $AutomationWorktree, "develop")
    }

    $branch = (& git -C $AutomationWorktree branch --show-current 2>&1 | Select-Object -First 1).Trim()
    if ($LASTEXITCODE -ne 0 -or $branch -ne "develop") {
        throw "WORKTREE_BRANCH_INVALID: $AutomationWorktree must check out develop."
    }
    $dirty = @(& git -C $AutomationWorktree status --short 2>&1)
    if ($LASTEXITCODE -ne 0 -or $dirty.Count -gt 0) {
        throw "WORKTREE_DIRTY: the develop automation worktree must be clean: $($dirty -join ', ')"
    }

    $runner = Join-Path $AutomationWorktree "tools\run-wows-update-task.ps1"
    if (-not (Test-Path -LiteralPath $runner)) {
        throw "RUNNER_MISSING: $runner"
    }

    $sourceTools = Join-Path $SourceRepoRoot ".tools"
    $worktreeTools = Join-Path $AutomationWorktree ".tools"
    if ((Test-Path -LiteralPath $sourceTools) -and -not (Test-Path -LiteralPath $worktreeTools)) {
        New-Item -ItemType Junction -Path $worktreeTools -Target $sourceTools | Out-Null
    }
}

$SourceRepoRoot = (Resolve-Path -LiteralPath $SourceRepoRoot).Path
if (-not $AutomationWorktree) {
    $AutomationWorktree = Join-Path $SourceRepoRoot "build\automation\develop-worktree"
}
$AutomationWorktree = [System.IO.Path]::GetFullPath($AutomationWorktree)

if ($Mode -eq "SelfTest") {
    $quoted = ConvertTo-QuotedArgument "S:\path with spaces\script.ps1"
    if ($quoted -ne '"S:\path with spaces\script.ps1"') {
        throw "SelfTest failed: task argument quoting is incorrect."
    }
    [void][datetime]::ParseExact($DailyAt, "HH:mm", [System.Globalization.CultureInfo]::InvariantCulture)
    Write-Output (([ordered]@{ status = "SELF_TEST_OK"; taskName = $TaskName; dailyAt = $DailyAt }) | ConvertTo-Json -Compress)
    exit 0
}

if ($Mode -eq "Uninstall") {
    $existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($existing) { Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false }
    Write-Output (([ordered]@{ status = "TASK_REMOVED"; taskName = $TaskName }) | ConvertTo-Json -Compress)
    exit 0
}

if ($Mode -eq "Show") {
    Write-Output ((Get-TaskSummary) | ConvertTo-Json -Depth 10 -Compress)
    exit 0
}

Assert-DevelopWorktree
$time = [datetime]::ParseExact($DailyAt, "HH:mm", [System.Globalization.CultureInfo]::InvariantCulture)
$powerShellExe = Join-Path $env:SystemRoot "System32\WindowsPowerShell\v1.0\powershell.exe"
$runnerPath = Join-Path $AutomationWorktree "tools\run-wows-update-task.ps1"
$argumentValues = @(
    "-NoProfile",
    "-WindowStyle", "Hidden",
    "-ExecutionPolicy", "Bypass",
    "-File", $runnerPath,
    "-Mode", "Run",
    "-ProjectRoot", $AutomationWorktree,
    "-OutputRoot", $SourceRepoRoot,
    "-GameDir", $GameDir,
    "-SteamManifest", $SteamManifest
)
$actionArguments = ($argumentValues | ForEach-Object { ConvertTo-QuotedArgument ([string]$_) }) -join " "
$action = New-ScheduledTaskAction -Execute $powerShellExe -Argument $actionArguments -WorkingDirectory $AutomationWorktree
$trigger = New-ScheduledTaskTrigger -Daily -At $time
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -WakeToRun -ExecutionTimeLimit (New-TimeSpan -Hours 4) -MultipleInstances IgnoreNew -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
$task = New-ScheduledTask -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "Checks Steam WoWS daily, builds on develop, and wakes Codex only for actionable notifications."
Register-ScheduledTask -TaskName $TaskName -InputObject $task -Force | Out-Null

Write-Output ((Get-TaskSummary) | ConvertTo-Json -Depth 10 -Compress)
