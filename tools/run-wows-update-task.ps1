param(
    [ValidateSet("Run", "SelfTest", "NotifyTest")]
    [string]$Mode = "Run",
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$OutputRoot = "",
    [string]$GameDir = "S:\SteamLibrary\steamapps\common\World of Warships",
    [string]$SteamManifest = "S:\SteamLibrary\steamapps\appmanifest_552990.acf",
    [string]$CodexExe = ""
)

$ErrorActionPreference = "Stop"

try {
    chcp.com 65001 | Out-Null
    $utf8 = New-Object System.Text.UTF8Encoding $false
    [Console]::InputEncoding = $utf8
    [Console]::OutputEncoding = $utf8
    $OutputEncoding = $utf8
} catch {
    # Encoding setup is best-effort.
}

function Get-UtcTimestamp {
    return [datetime]::UtcNow.ToString("o")
}

function Write-JsonAtomic {
    param([string]$Path, $Value)

    $parent = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    $temporary = "$Path.$([guid]::NewGuid().ToString('N')).tmp"
    $json = $Value | ConvertTo-Json -Depth 20
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($temporary, $json, $utf8NoBom)
    Move-Item -LiteralPath $temporary -Destination $Path -Force
}

function Write-LogLines {
    param([string]$Path, [object[]]$Lines)

    $parent = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    $text = (@($Lines) | ForEach-Object { [string]$_ }) -join [Environment]::NewLine
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($Path, $text, $utf8NoBom)
}

function Read-RunnerState {
    param([string]$Path)

    $state = [ordered]@{
        schemaVersion = 1
        lastRunAt = ""
        lastStatus = ""
        lastEventKey = ""
        lastNotificationKey = ""
        lastNotificationAt = ""
        lastNotificationSucceeded = $false
        lastCodexThreadId = ""
        lastCodexExitCode = $null
        lastCheckLog = ""
        lastCodexLog = ""
        lastError = ""
    }
    if (-not (Test-Path -LiteralPath $Path)) { return $state }

    $existing = Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
    foreach ($property in $existing.PSObject.Properties) {
        $state[$property.Name] = $property.Value
    }
    return $state
}

function ConvertFrom-LastJsonLine {
    param([object[]]$Lines)

    $items = @($Lines)
    for ($index = $items.Count - 1; $index -ge 0; $index -= 1) {
        $line = ([string]$items[$index]).Trim()
        if (-not $line.StartsWith("{")) { continue }
        try {
            return $line | ConvertFrom-Json
        } catch {
            continue
        }
    }
    return $null
}

function Get-Sha256Text {
    param([string]$Text)

    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
        return ([System.BitConverter]::ToString($sha256.ComputeHash($bytes))).Replace("-", "").ToLowerInvariant()
    } finally {
        $sha256.Dispose()
    }
}

function Get-EventKey {
    param($Outcome)

    if ([string]$Outcome.status -eq "READY_TO_PUBLISH") {
        # A retry result omits Steam metadata, so identify a ready package by its immutable build and hash.
        $parts = @([string]$Outcome.status, [string]$Outcome.gameBuild, [string]$Outcome.packageSha256)
    } else {
        $parts = @(
            [string]$Outcome.status,
            [string]$Outcome.steamBuildId,
            [string]$Outcome.gameBuild,
            [string]$Outcome.error,
            [string]$Outcome.lastError
        )
    }
    return Get-Sha256Text ($parts -join "|")
}

function Test-ShouldNotify {
    param([string]$Status)

    return $Status -notin @("NO_UPDATE", "WAITING_FOR_STEAM", "ALREADY_RUNNING", "SELF_TEST_OK")
}

function Resolve-CodexExecutable {
    param([string]$ExplicitPath)

    $candidates = @()
    if ($ExplicitPath) { $candidates += $ExplicitPath }
    if ($env:USERPROFILE) {
        $candidates += (Join-Path $env:USERPROFILE ".codex\.sandbox-bin\codex.exe")
        $candidates += (Join-Path $env:USERPROFILE ".codex\plugins\.plugin-appserver\codex.exe")
    }
    $command = Get-Command codex.exe -ErrorAction SilentlyContinue
    if ($command) { $candidates += $command.Source }

    foreach ($candidate in ($candidates | Select-Object -Unique)) {
        if ($candidate -and (Test-Path -LiteralPath $candidate -PathType Leaf)) {
            return (Resolve-Path -LiteralPath $candidate).Path
        }
    }
    throw "CODEX_EXE_MISSING: no usable codex.exe was found."
}

function New-NotificationPrompt {
    param($Outcome, [string]$CheckLog, [string]$ReleaseStatePath, [string]$CopiedPackagePath)

    $outcomeJson = $Outcome | ConvertTo-Json -Depth 20
    return @"
This is a one-time notification created by the standalone Windows WoWS updater. It is not a daily Codex check.

Report the result directly to the user in Chinese. Do not call tools, modify files, open a browser, upload attachments, or post to Aslain or any other third party. Your only job is to produce a clear user notification in this Codex task.

For READY_TO_PUBLISH, say that the package was built automatically. Include the game version, internal build, added/removed/changed ship counts, zip path, SHA-256, and paste-ready English reply. Remind the user to publish it manually.
For a failure or blocked result, say that user action is required and include the error and log path.
If the user later says it was published, first obtain the exact comment URL and never guess it. MarkPublished may only be run after the user explicitly asks.

Check log: $CheckLog
Release state: $ReleaseStatePath
Package copied to the primary checkout: $CopiedPackagePath

Result JSON:
$outcomeJson
"@
}

function Invoke-CodexNotification {
    param($Outcome, [string]$CheckLog, [string]$ReleaseStatePath, [string]$CopiedPackagePath, [string]$LogDirectory)

    $resolvedCodex = Resolve-CodexExecutable $CodexExe
    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $codexLog = Join-Path $LogDirectory "codex-notification.$stamp.jsonl"
    $lastMessage = Join-Path $LogDirectory "codex-notification.$stamp.txt"
    $prompt = New-NotificationPrompt $Outcome $CheckLog $ReleaseStatePath $CopiedPackagePath

    $previousErrorActionPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        $output = @($prompt | & $resolvedCodex exec --sandbox read-only --cd $ProjectRoot --json --output-last-message $lastMessage - 2>&1)
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }
    Write-LogLines $codexLog $output

    $threadId = ""
    foreach ($line in $output) {
        try {
            $event = ([string]$line) | ConvertFrom-Json
            if ($event.type -eq "thread.started" -and $event.thread_id) {
                $threadId = [string]$event.thread_id
                break
            }
        } catch {
            # Non-JSON diagnostics remain in the log.
        }
    }

    return [pscustomobject]@{
        Success = ($exitCode -eq 0 -and (Test-Path -LiteralPath $lastMessage))
        ExitCode = $exitCode
        ThreadId = $threadId
        LogPath = $codexLog
        LastMessagePath = $lastMessage
        CodexExe = $resolvedCodex
    }
}

function Invoke-CheckAndBuild {
    param([string]$LogDirectory)

    $checker = Join-Path $ProjectRoot "tools\check-steam-wows-update.ps1"
    if (-not (Test-Path -LiteralPath $checker)) {
        throw "CHECK_SCRIPT_MISSING: $checker"
    }

    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $logPath = Join-Path $LogDirectory "check-and-build.$stamp.log"
    $arguments = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $checker,
        "-Mode", "CheckAndBuild",
        "-ProjectRoot", $ProjectRoot,
        "-GameDir", $GameDir,
        "-SteamManifest", $SteamManifest
    )
    $previousErrorActionPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        $output = @(& powershell.exe @arguments 2>&1)
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }
    Write-LogLines $logPath $output
    $outcome = ConvertFrom-LastJsonLine $output
    if ($null -eq $outcome) {
        $outcome = [pscustomobject]@{
            status = "BUILD_FAILED"
            checkedAt = Get-UtcTimestamp
            error = "CHECK_RESULT_MISSING: check script exited with code $exitCode without a JSON result."
        }
    }

    return [pscustomobject]@{ Outcome = $outcome; ExitCode = $exitCode; LogPath = $logPath }
}

function Copy-PackageToOutputRoot {
    param($Outcome)

    if ($Outcome.status -ne "READY_TO_PUBLISH" -or -not $Outcome.packagePath) { return "" }
    if (-not (Test-Path -LiteralPath $Outcome.packagePath -PathType Leaf)) {
        throw "PACKAGE_COPY_SOURCE_MISSING: $($Outcome.packagePath)"
    }
    $destinationDirectory = Join-Path $OutputRoot "dist"
    New-Item -ItemType Directory -Force -Path $destinationDirectory | Out-Null
    $destination = Join-Path $destinationDirectory ([System.IO.Path]::GetFileName([string]$Outcome.packagePath))
    Copy-Item -LiteralPath $Outcome.packagePath -Destination $destination -Force
    $sourceHash = (Get-FileHash -LiteralPath $Outcome.packagePath -Algorithm SHA256).Hash
    $destinationHash = (Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash
    if ($sourceHash -ne $destinationHash) {
        throw "PACKAGE_COPY_HASH_MISMATCH: $destination"
    }
    return $destination
}

function Invoke-SelfTest {
    $sample = @("diagnostic", '{"status":"READY_TO_PUBLISH","gameBuild":"12830008","packageSha256":"abc"}')
    $parsed = ConvertFrom-LastJsonLine $sample
    if ($null -eq $parsed -or $parsed.gameBuild -ne "12830008") {
        throw "SelfTest failed: JSON result parsing is incorrect."
    }
    if (Test-ShouldNotify "NO_UPDATE") {
        throw "SelfTest failed: NO_UPDATE would wake Codex."
    }
    if (-not (Test-ShouldNotify "READY_TO_PUBLISH") -or -not (Test-ShouldNotify "BUILD_FAILED")) {
        throw "SelfTest failed: actionable results would not wake Codex."
    }
    $key1 = Get-EventKey $parsed
    $key2 = Get-EventKey $parsed
    if (-not $key1 -or $key1 -ne $key2) {
        throw "SelfTest failed: notification event keys are not deterministic."
    }
    $retry = '{"status":"READY_TO_PUBLISH","gameBuild":"12830008","packageSha256":"abc","retry":true}' | ConvertFrom-Json
    if ((Get-EventKey $retry) -ne $key1) {
        throw "SelfTest failed: a ready-package retry would create a duplicate notification."
    }
    $prompt = New-NotificationPrompt $parsed "check.log" "release.json" "package.zip"
    if ($prompt -notmatch 'Do not call tools' -or $prompt -notmatch 'publish it manually') {
        throw "SelfTest failed: the notification prompt does not preserve the no-post boundary."
    }
    return [ordered]@{ status = "SELF_TEST_OK"; checkedAt = Get-UtcTimestamp }
}

$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path
if (-not $OutputRoot) { $OutputRoot = $ProjectRoot }
$OutputRoot = (Resolve-Path -LiteralPath $OutputRoot).Path
$automationDirectory = Join-Path $ProjectRoot "build\automation"
$logDirectory = Join-Path $automationDirectory "scheduled-logs"
$runnerStatePath = Join-Path $automationDirectory "standalone-runner-state.json"
$releaseStatePath = Join-Path $automationDirectory "wows-release-state.json"
New-Item -ItemType Directory -Force -Path $logDirectory | Out-Null

if ($Mode -eq "SelfTest") {
    $selfTest = Invoke-SelfTest
    Write-Output ($selfTest | ConvertTo-Json -Compress)
    exit 0
}

$mutex = New-Object System.Threading.Mutex($false, "Local\WoWSArmorUpdateStandaloneTask")
$hasMutex = $false
try {
    try { $hasMutex = $mutex.WaitOne(0) } catch [System.Threading.AbandonedMutexException] { $hasMutex = $true }
    if (-not $hasMutex) {
        Write-Output (([ordered]@{ status = "ALREADY_RUNNING"; checkedAt = Get-UtcTimestamp }) | ConvertTo-Json -Compress)
        exit 0
    }

    $runnerState = Read-RunnerState $runnerStatePath
    $copiedPackagePath = ""
    $checkLog = ""
    $checkExitCode = 0

    if ($Mode -eq "NotifyTest") {
        $outcome = [pscustomobject]@{
            status = "NOTIFICATION_TEST"
            checkedAt = Get-UtcTimestamp
            gameVersion = "test"
            gameBuild = "test-$([guid]::NewGuid().ToString('N'))"
            message = "The standalone WoWS Windows task successfully woke Codex. This is a mobile notification test."
        }
        $checkLog = "(notification test; no version check or build was run)"
    } else {
        $check = Invoke-CheckAndBuild $logDirectory
        $outcome = $check.Outcome
        $checkLog = $check.LogPath
        $checkExitCode = $check.ExitCode
        if ($outcome.status -eq "READY_TO_PUBLISH") {
            $copiedPackagePath = Copy-PackageToOutputRoot $outcome
        }
    }

    $eventKey = Get-EventKey $outcome
    $runnerState.lastRunAt = Get-UtcTimestamp
    $runnerState.lastStatus = [string]$outcome.status
    $runnerState.lastEventKey = $eventKey
    $runnerState.lastCheckLog = $checkLog
    $runnerState.lastError = ""

    $shouldNotify = Test-ShouldNotify ([string]$outcome.status)
    $duplicateNotification = ($Mode -ne "NotifyTest" -and $runnerState.lastNotificationSucceeded -and $runnerState.lastNotificationKey -eq $eventKey)
    $notification = $null
    if ($shouldNotify -and -not $duplicateNotification) {
        $notification = Invoke-CodexNotification $outcome $checkLog $releaseStatePath $copiedPackagePath $logDirectory
        $runnerState.lastNotificationKey = $eventKey
        $runnerState.lastNotificationAt = Get-UtcTimestamp
        $runnerState.lastNotificationSucceeded = [bool]$notification.Success
        $runnerState.lastCodexThreadId = $notification.ThreadId
        $runnerState.lastCodexExitCode = $notification.ExitCode
        $runnerState.lastCodexLog = $notification.LogPath
        if (-not $notification.Success) {
            $runnerState.lastError = "CODEX_WAKE_FAILED: codex exec exited with code $($notification.ExitCode)."
        }
    }
    Write-JsonAtomic $runnerStatePath $runnerState

    $summary = [ordered]@{
        status = [string]$outcome.status
        checkedAt = Get-UtcTimestamp
        checkExitCode = $checkExitCode
        checkLog = $checkLog
        copiedPackagePath = $copiedPackagePath
        notificationRequired = $shouldNotify
        notificationSuppressedAsDuplicate = $duplicateNotification
        notificationSent = if ($null -ne $notification) { [bool]$notification.Success } else { $false }
        codexThreadId = if ($null -ne $notification) { $notification.ThreadId } else { "" }
        runnerStatePath = $runnerStatePath
    }
    Write-Output ($summary | ConvertTo-Json -Depth 10 -Compress)
    if ($null -ne $notification -and -not $notification.Success) { exit 1 }
    exit 0
} catch {
    $message = $_.Exception.Message
    $outcome = [pscustomobject]@{ status = "STANDALONE_RUNNER_FAILED"; checkedAt = Get-UtcTimestamp; error = $message }
    $notification = $null
    try {
        $notification = Invoke-CodexNotification $outcome "(runner failed before a check log was available)" $releaseStatePath "" $logDirectory
    } catch {
        $message = "$message; CODEX_WAKE_FAILED: $($_.Exception.Message)"
    }
    $failure = [ordered]@{
        status = "STANDALONE_RUNNER_FAILED"
        checkedAt = Get-UtcTimestamp
        error = $message
        notificationSent = ($null -ne $notification -and $notification.Success)
        codexThreadId = if ($null -ne $notification) { $notification.ThreadId } else { "" }
    }
    try { Write-JsonAtomic (Join-Path $automationDirectory "standalone-runner-failure.json") $failure } catch {}
    Write-Output ($failure | ConvertTo-Json -Depth 10 -Compress)
    exit 1
} finally {
    if ($hasMutex) { $mutex.ReleaseMutex() }
    $mutex.Dispose()
}
