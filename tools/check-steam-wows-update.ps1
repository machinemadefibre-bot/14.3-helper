param(
    [ValidateSet("CheckAndBuild", "MarkPublished", "MarkPublishFailed", "DryRun", "SelfTest")]
    [string]$Mode = "CheckAndBuild",
    [string]$GameDir = "S:\SteamLibrary\steamapps\common\World of Warships",
    [string]$SteamManifest = "S:\SteamLibrary\steamapps\appmanifest_552990.acf",
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$StatePath = "",
    [string]$PublishedUrl = "",
    [string]$ErrorMessage = "",
    [string]$TargetUrl = "https://aslain.com/index.php?/topic/35814-143-helper/#comment-143136",
    [double]$MaxShipCountDeltaPercent = 10,
    [double]$MaxRemovedPercent = 5,
    [double]$MaxDiffPercent = 25
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

function ConvertFrom-AcfText {
    param([string]$Text)

    $values = @{}
    $matches = [regex]::Matches($Text, '(?m)^\s*"([^"]+)"\s+"([^"]*)"\s*$')
    foreach ($match in $matches) {
        $values[$match.Groups[1].Value] = $match.Groups[2].Value
    }
    return $values
}

function Read-SteamManifest {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        throw "STEAM_MANIFEST_MISSING: $Path"
    }
    return ConvertFrom-AcfText (Get-Content -LiteralPath $Path -Raw -Encoding UTF8)
}

function Get-SteamInstallStatus {
    param([hashtable]$Manifest)

    if ($Manifest["appid"] -ne "552990") {
        return [pscustomobject]@{ Complete = $false; Reason = "Steam manifest appid is not 552990." }
    }

    $stateFlags = 0L
    if (-not [int64]::TryParse([string]$Manifest["StateFlags"], [ref]$stateFlags)) {
        return [pscustomobject]@{ Complete = $false; Reason = "Steam StateFlags is missing or invalid." }
    }
    if (($stateFlags -band 4) -eq 0) {
        return [pscustomobject]@{ Complete = $false; Reason = "Steam does not report the game as fully installed." }
    }

    $buildId = [string]$Manifest["buildid"]
    $targetBuildId = [string]$Manifest["TargetBuildID"]
    if (-not $buildId) {
        return [pscustomobject]@{ Complete = $false; Reason = "Steam buildid is missing." }
    }
    if ($targetBuildId -and $targetBuildId -ne $buildId) {
        return [pscustomobject]@{ Complete = $false; Reason = "Steam TargetBuildID does not match buildid." }
    }

    foreach ($pair in @(@("BytesToDownload", "BytesDownloaded"), @("BytesToStage", "BytesStaged"))) {
        $expected = [string]$Manifest[$pair[0]]
        $actual = [string]$Manifest[$pair[1]]
        if ($expected -and $actual -and $expected -ne $actual) {
            return [pscustomobject]@{ Complete = $false; Reason = "Steam $($pair[1]) does not match $($pair[0])." }
        }
    }

    return [pscustomobject]@{ Complete = $true; Reason = "Installed"; BuildId = $buildId }
}

function ConvertFrom-ProductVersion {
    param([string]$ProductVersion)

    $parts = @($ProductVersion -split '[\.,]' | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" })
    if ($parts.Count -lt 4) {
        throw "GAME_VERSION_INVALID: ProductVersion '$ProductVersion' does not contain four components."
    }
    foreach ($part in $parts[0..3]) {
        $number = 0L
        if (-not [int64]::TryParse($part, [ref]$number)) {
            throw "GAME_VERSION_INVALID: ProductVersion '$ProductVersion' contains a non-numeric component."
        }
    }

    return [pscustomobject]@{
        Major = $parts[0]
        Minor = $parts[1]
        Patch = $parts[2]
        Build = $parts[3]
        PublicVersion = "$($parts[0]).$($parts[1])"
        FullVersion = "$($parts[0]).$($parts[1]).$($parts[2]).$($parts[3])"
    }
}

function Get-InstalledGameVersion {
    param([string]$Root)

    $binRoot = Join-Path $Root "bin"
    if (-not (Test-Path -LiteralPath $binRoot)) {
        throw "GAME_BIN_MISSING: $binRoot"
    }

    $buildDirs = @(
        Get-ChildItem -LiteralPath $binRoot -Directory -ErrorAction Stop |
            Where-Object { $_.Name -match '^\d+$' } |
            Sort-Object { [int64]$_.Name } -Descending
    )
    if ($buildDirs.Count -eq 0) {
        throw "GAME_BUILD_MISSING: no numeric build directory exists under $binRoot"
    }

    $buildDir = $buildDirs[0]
    $exePath = Join-Path $buildDir.FullName "bin64\WorldOfWarships64.exe"
    if (-not (Test-Path -LiteralPath $exePath)) {
        throw "GAME_EXE_MISSING: $exePath"
    }

    $parsed = ConvertFrom-ProductVersion (Get-Item -LiteralPath $exePath).VersionInfo.ProductVersion
    if ($parsed.Build -ne $buildDir.Name) {
        throw "GAME_VERSION_MISMATCH: ProductVersion build $($parsed.Build) does not match bin directory $($buildDir.Name)"
    }

    return [pscustomobject]@{
        Build = $parsed.Build
        PublicVersion = $parsed.PublicVersion
        FullVersion = $parsed.FullVersion
        BinDir = $buildDir.FullName
        ExePath = $exePath
    }
}

function Read-JsonFile {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return $null }
    return Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
}

function New-ReleaseState {
    return [ordered]@{
        schemaVersion = 1
        targetUrl = $TargetUrl
        status = "UNKNOWN"
        steamBuildId = ""
        gameBuild = ""
        gameVersion = ""
        fullGameVersion = ""
        databaseBuild = ""
        packagePath = ""
        packageSha256 = ""
        diffPath = ""
        addedShips = 0
        removedShips = 0
        changedShips = 0
        replyText = ""
        publishedUrl = ""
        publishedAt = ""
        publishAttempts = 0
        lastAttempt = ""
        lastError = ""
    }
}

function Read-ReleaseState {
    param([string]$Path)

    $state = New-ReleaseState
    if (-not (Test-Path -LiteralPath $Path)) { return $state }
    $existing = Read-JsonFile $Path
    if ($null -eq $existing) { return $state }
    foreach ($property in $existing.PSObject.Properties) {
        $state[$property.Name] = $property.Value
    }
    return $state
}

function Write-JsonAtomic {
    param([string]$Path, $Value)

    $parent = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    $tempPath = "$Path.$([guid]::NewGuid().ToString('N')).tmp"
    $json = $Value | ConvertTo-Json -Depth 12
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($tempPath, $json, $utf8NoBom)
    Move-Item -LiteralPath $tempPath -Destination $Path -Force
}

function Write-Outcome {
    param($Outcome, [switch]$Persist)

    if ($Persist) {
        $lastResultPath = Join-Path (Split-Path -Parent $StatePath) "last-result.json"
        Write-JsonAtomic $lastResultPath $Outcome
    }
    Write-Output ($Outcome | ConvertTo-Json -Depth 12 -Compress)
}

function Get-DatabaseBuild {
    $dataPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
    $database = Read-JsonFile $dataPath
    if ($null -eq $database -or $null -eq $database.meta -or -not $database.meta.gameBuild) {
        throw "DATABASE_BUILD_MISSING: $dataPath"
    }
    return [string]$database.meta.gameBuild
}

function Get-ConstantValue {
    param([string]$Name)
    $path = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_constants.py"
    $text = Get-Content -LiteralPath $path -Raw -Encoding UTF8
    if ($text -match "(?m)^\s*$([regex]::Escape($Name))\s*=\s*'([^']*)'") {
        return [string]$Matches[1]
    }
    throw "CONSTANT_MISSING: $Name in $path"
}

function ConvertTo-SafeNamePart {
    param([string]$Value)
    $safe = ([string]$Value).Trim() -replace '[^A-Za-z0-9._-]+', '_'
    return $safe.Trim("_")
}

function Get-PackagePath {
    param([string]$PublicVersion)
    $modVersion = Get-ConstantValue "MOD_VERSION"
    if (-not $modVersion.StartsWith("v", [System.StringComparison]::OrdinalIgnoreCase)) {
        $modVersion = "v$modVersion"
    }
    $safeModVersion = ConvertTo-SafeNamePart $modVersion
    $safePublicVersion = ConvertTo-SafeNamePart $PublicVersion
    return Join-Path $ProjectRoot "dist\14.3-helper_${safeModVersion}_Aslain-patch$safePublicVersion.zip"
}

function Get-GitOutput {
    param([string[]]$Arguments)
    $previousErrorActionPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        $output = @(& git @Arguments 2>&1)
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }
    return [pscustomobject]@{ ExitCode = $exitCode; Lines = $output; Text = ($output -join [Environment]::NewLine) }
}

function Get-GitChangedPaths {
    $result = Get-GitOutput @("status", "--porcelain=v1", "--untracked-files=all")
    if ($result.ExitCode -ne 0) { throw "GIT_STATUS_FAILED: $($result.Text)" }

    $paths = @()
    foreach ($line in $result.Lines) {
        $text = [string]$line
        if ($text.Length -lt 4) { continue }
        $path = $text.Substring(3).Trim().Trim('"')
        if ($path -match ' -> ') { $path = ($path -split ' -> ')[-1] }
        $paths += ($path -replace '\\', '/')
    }
    return @($paths)
}

function Assert-CleanMain {
    $branchResult = Get-GitOutput @("branch", "--show-current")
    if ($branchResult.ExitCode -ne 0) { throw "GIT_BRANCH_FAILED: $($branchResult.Text)" }
    $branch = ($branchResult.Lines | Select-Object -First 1).Trim()
    if ($branch -ne "main") {
        throw "GIT_BRANCH_BLOCKED: unattended update requires main, current branch is '$branch'."
    }

    $dirty = @(Get-GitChangedPaths)
    if ($dirty.Count -gt 0) {
        throw "GIT_DIRTY_BLOCKED: main has uncommitted paths: $($dirty -join ', ')"
    }
}

function Get-GeneratedSourcePaths {
    return @(
        "src/res_mods/PnFMods/APOvermatchAssistant/data/armor_overmatch.json",
        "src/res_mods/PnFMods/APOvermatchAssistant/data/armor_overmatch.py",
        "src/res_mods/PnFMods/APOvermatchAssistant/overmatch_constants.py",
        "src/res_mods/gui/unbound2/PnFMods/APOvermatchAssistant.unbound"
    )
}

function New-RollbackSnapshot {
    param([string[]]$RelativePaths)

    $root = Join-Path $ProjectRoot ("build\automation\rollback\" + [guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Force -Path $root | Out-Null
    $entries = @()
    foreach ($relativePath in $RelativePaths) {
        $sourcePath = Join-Path $ProjectRoot ($relativePath -replace '/', '\')
        $backupPath = Join-Path $root ($relativePath -replace '/', '\')
        $exists = Test-Path -LiteralPath $sourcePath
        if ($exists) {
            $backupParent = Split-Path -Parent $backupPath
            New-Item -ItemType Directory -Force -Path $backupParent | Out-Null
            Copy-Item -LiteralPath $sourcePath -Destination $backupPath -Force
        }
        $entries += [pscustomobject]@{ RelativePath = $relativePath; SourcePath = $sourcePath; BackupPath = $backupPath; Existed = $exists }
    }
    return [pscustomobject]@{ Root = $root; Entries = $entries }
}

function Restore-RollbackSnapshot {
    param($Snapshot)
    if ($null -eq $Snapshot) { return }

    foreach ($entry in $Snapshot.Entries) {
        if ($entry.Existed) {
            Copy-Item -LiteralPath $entry.BackupPath -Destination $entry.SourcePath -Force
        } elseif (Test-Path -LiteralPath $entry.SourcePath) {
            Remove-Item -LiteralPath $entry.SourcePath -Force
        }
    }
    $relativePaths = @($Snapshot.Entries | ForEach-Object { $_.RelativePath })
    if ($relativePaths.Count -gt 0) {
        $unstageResult = Get-GitOutput (@("restore", "--staged", "--") + $relativePaths)
        if ($unstageResult.ExitCode -ne 0) {
            throw "Unable to unstage generated files during rollback: $($unstageResult.Text)"
        }
    }
    if (Test-Path -LiteralPath $Snapshot.Root) {
        Remove-Item -LiteralPath $Snapshot.Root -Recurse -Force
    }
}

function Remove-RollbackSnapshot {
    param($Snapshot)
    if ($null -ne $Snapshot -and (Test-Path -LiteralPath $Snapshot.Root)) {
        Remove-Item -LiteralPath $Snapshot.Root -Recurse -Force
    }
}

function Get-LatestDiff {
    param([datetime]$RunStart)

    $dir = Join-Path $ProjectRoot "build\armor-update"
    $files = @(
        Get-ChildItem -LiteralPath $dir -Filter "armor_diff.*.json" -ErrorAction SilentlyContinue |
            Where-Object { $_.LastWriteTime -ge $RunStart.AddSeconds(-10) } |
            Sort-Object LastWriteTime -Descending
    )
    if ($files.Count -eq 0) { return $null }
    $diff = Read-JsonFile $files[0].FullName
    return [pscustomobject]@{ Path = $files[0].FullName; Value = $diff }
}

function Test-DiffMetrics {
    param([double]$OldCount, [double]$NewCount, [int]$Added, [int]$Removed, [int]$Changed)

    if ($OldCount -le 0 -or $NewCount -le 0) { return $false }
    $deltaPercent = ([math]::Abs($NewCount - $OldCount) / $OldCount) * 100
    $removedPercent = ($Removed / $OldCount) * 100
    $diffPercent = (($Added + $Removed + $Changed) / $OldCount) * 100
    return ($deltaPercent -le $MaxShipCountDeltaPercent -and $removedPercent -le $MaxRemovedPercent -and $diffPercent -le $MaxDiffPercent)
}

function Invoke-GeneratedCommit {
    param([string[]]$ChangedPaths, [string]$Message)

    if ($ChangedPaths.Count -eq 0) { return "" }
    $addResult = Get-GitOutput (@("add", "--") + $ChangedPaths)
    if ($addResult.ExitCode -ne 0) { throw "GIT_ADD_FAILED: $($addResult.Text)" }

    $commitResult = Get-GitOutput @("commit", "-m", $Message)
    if ($commitResult.ExitCode -ne 0 -and $commitResult.Text -match 'index\.lock') {
        $lockPath = Join-Path $ProjectRoot ".git\index.lock"
        if (-not (Test-Path -LiteralPath $lockPath)) {
            Start-Sleep -Seconds 1
            $commitResult = Get-GitOutput @("commit", "-m", $Message)
        }
    }
    if ($commitResult.ExitCode -ne 0) { throw "GIT_COMMIT_FAILED: $($commitResult.Text)" }

    $shaResult = Get-GitOutput @("rev-parse", "HEAD")
    if ($shaResult.ExitCode -ne 0) { throw "GIT_REV_PARSE_FAILED: $($shaResult.Text)" }
    return ([string]($shaResult.Lines | Select-Object -First 1)).Trim()
}

function Invoke-SelfTest {
    $acf = @'
"AppState"
{
    "appid" "552990"
    "StateFlags" "4"
    "buildid" "23670357"
    "TargetBuildID" "23670357"
    "BytesToDownload" "100"
    "BytesDownloaded" "100"
    "BytesToStage" "200"
    "BytesStaged" "200"
}
'@
    $manifest = ConvertFrom-AcfText $acf
    $steamStatus = Get-SteamInstallStatus $manifest
    if (-not $steamStatus.Complete -or $steamStatus.BuildId -ne "23670357") {
        throw "SelfTest failed: complete Steam manifest was rejected."
    }

    $manifest["BytesDownloaded"] = "99"
    if ((Get-SteamInstallStatus $manifest).Complete) {
        throw "SelfTest failed: incomplete Steam download was accepted."
    }

    $version = ConvertFrom-ProductVersion "15,5,0,12668706"
    if ($version.PublicVersion -ne "15.5" -or $version.Build -ne "12668706") {
        throw "SelfTest failed: ProductVersion parsing is incorrect."
    }

    if (-not (Test-DiffMetrics 1186 1196 10 0 0)) {
        throw "SelfTest failed: a normal diff was rejected."
    }
    if (Test-DiffMetrics 1186 900 0 286 0) {
        throw "SelfTest failed: an abnormal diff was accepted."
    }

    $state = New-ReleaseState
    $state.status = "READY_TO_PUBLISH"
    $state.gameBuild = "12668706"
    $state.status = "PUBLISHED"
    $state.publishedUrl = $TargetUrl
    if ($state.status -ne "PUBLISHED" -or -not $state.publishedUrl) {
        throw "SelfTest failed: publication state transition is incorrect."
    }

    return [ordered]@{ status = "SELF_TEST_OK"; checkedAt = Get-UtcTimestamp; targetUrl = $TargetUrl }
}

$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path
if (-not $StatePath) {
    $StatePath = Join-Path $ProjectRoot "build\automation\wows-release-state.json"
}

if ($Mode -eq "SelfTest") {
    Write-Outcome (Invoke-SelfTest)
    exit 0
}

$state = Read-ReleaseState $StatePath

if ($Mode -eq "MarkPublished") {
    if (-not $PublishedUrl) { throw "-PublishedUrl is required with MarkPublished." }
    if (-not $state.gameBuild) { throw "No built game version exists in release state." }
    $state.status = "PUBLISHED"
    $state.publishedUrl = $PublishedUrl
    $state.publishedAt = Get-UtcTimestamp
    $state.lastAttempt = $state.publishedAt
    $state.lastError = ""
    $state.publishAttempts = [int]$state.publishAttempts + 1
    Write-JsonAtomic $StatePath $state
    Write-Outcome ([ordered]@{ status = "PUBLISHED"; gameBuild = $state.gameBuild; packagePath = $state.packagePath; publishedUrl = $PublishedUrl }) -Persist
    exit 0
}

if ($Mode -eq "MarkPublishFailed") {
    if (-not $ErrorMessage) { $ErrorMessage = "Aslain publication failed or needs user input." }
    $state.status = "PUBLISH_FAILED"
    $state.lastAttempt = Get-UtcTimestamp
    $state.lastError = $ErrorMessage
    $state.publishAttempts = [int]$state.publishAttempts + 1
    Write-JsonAtomic $StatePath $state
    Write-Outcome ([ordered]@{ status = "PUBLISH_FAILED"; gameBuild = $state.gameBuild; packagePath = $state.packagePath; error = $ErrorMessage }) -Persist
    exit 1
}

$rollbackSnapshot = $null
$commitCompleted = $false
$steamBuildId = ""
$gameVersion = $null
$databaseBuild = ""
$runStart = Get-Date

try {
    $manifest = Read-SteamManifest $SteamManifest
    $steamStatus = Get-SteamInstallStatus $manifest
    $steamBuildId = [string]$manifest["buildid"]
    if (-not $steamStatus.Complete) {
        $outcome = [ordered]@{
            status = "WAITING_FOR_STEAM"
            checkedAt = Get-UtcTimestamp
            steamBuildId = $steamBuildId
            reason = $steamStatus.Reason
        }
        if ($Mode -eq "DryRun") { Write-Outcome $outcome } else {
            $state.status = "WAITING_FOR_STEAM"
            $state.steamBuildId = $steamBuildId
            $state.lastAttempt = $outcome.checkedAt
            $state.lastError = $steamStatus.Reason
            Write-JsonAtomic $StatePath $state
            Write-Outcome $outcome -Persist
        }
        exit 0
    }

    $gameVersion = Get-InstalledGameVersion $GameDir
    $databaseBuild = Get-DatabaseBuild
    $packagePath = Get-PackagePath $gameVersion.PublicVersion

    $installedBuildNumber = 0L
    $databaseBuildNumber = 0L
    if (-not [int64]::TryParse($gameVersion.Build, [ref]$installedBuildNumber)) {
        throw "GAME_BUILD_INVALID: $($gameVersion.Build)"
    }
    if (-not [int64]::TryParse($databaseBuild, [ref]$databaseBuildNumber)) {
        throw "DATABASE_BUILD_INVALID: $databaseBuild"
    }
    if ($databaseBuildNumber -gt $installedBuildNumber) {
        throw "VERSION_REGRESSION_BLOCKED: database build $databaseBuild is newer than installed game build $($gameVersion.Build)"
    }

    if ($state.gameBuild -eq $gameVersion.Build -and $state.status -eq "PUBLISHED") {
        $outcome = [ordered]@{
            status = "NO_UPDATE"
            checkedAt = Get-UtcTimestamp
            steamBuildId = $steamBuildId
            gameBuild = $gameVersion.Build
            gameVersion = $gameVersion.PublicVersion
            databaseBuild = $databaseBuild
            publishedUrl = $state.publishedUrl
        }
        Write-Outcome $outcome -Persist:($Mode -ne "DryRun")
        exit 0
    }

    if ($state.gameBuild -eq $gameVersion.Build -and $state.status -in @("READY_TO_PUBLISH", "PUBLISH_FAILED") -and (Test-Path -LiteralPath $state.packagePath)) {
        $outcome = [ordered]@{
            status = "READY_TO_PUBLISH"
            checkedAt = Get-UtcTimestamp
            retry = $true
            gameBuild = $state.gameBuild
            gameVersion = $state.gameVersion
            packagePath = $state.packagePath
            packageSha256 = $state.packageSha256
            replyText = $state.replyText
            targetUrl = $state.targetUrl
            lastError = $state.lastError
        }
        Write-Outcome $outcome -Persist:($Mode -ne "DryRun")
        exit 0
    }

    $needsBuild = ($databaseBuildNumber -lt $installedBuildNumber) -or (-not (Test-Path -LiteralPath $packagePath))
    if (-not $needsBuild) {
        $hash = (Get-FileHash -LiteralPath $packagePath -Algorithm SHA256).Hash.ToLowerInvariant()
        $outcome = [ordered]@{
            status = "READY_TO_PUBLISH"
            checkedAt = Get-UtcTimestamp
            retry = $false
            gameBuild = $gameVersion.Build
            gameVersion = $gameVersion.PublicVersion
            databaseBuild = $databaseBuild
            packagePath = $packagePath
            packageSha256 = $hash
            targetUrl = $TargetUrl
        }
        if ($Mode -eq "DryRun") { Write-Outcome $outcome } else {
            $state.status = "READY_TO_PUBLISH"
            $state.steamBuildId = $steamBuildId
            $state.gameBuild = $gameVersion.Build
            $state.gameVersion = $gameVersion.PublicVersion
            $state.fullGameVersion = $gameVersion.FullVersion
            $state.databaseBuild = $databaseBuild
            $state.packagePath = $packagePath
            $state.packageSha256 = $hash
            $state.lastAttempt = $outcome.checkedAt
            $state.lastError = ""
            Write-JsonAtomic $StatePath $state
            Write-Outcome $outcome -Persist
        }
        exit 0
    }

    if ($Mode -eq "DryRun") {
        Write-Outcome ([ordered]@{
            status = "UPDATE_AVAILABLE"
            checkedAt = Get-UtcTimestamp
            steamBuildId = $steamBuildId
            gameBuild = $gameVersion.Build
            gameVersion = $gameVersion.PublicVersion
            databaseBuild = $databaseBuild
            expectedPackagePath = $packagePath
        })
        exit 0
    }

    Assert-CleanMain
    $generatedPaths = @(Get-GeneratedSourcePaths)
    $rollbackSnapshot = New-RollbackSnapshot $generatedPaths

    $updateScript = Join-Path $ProjectRoot "tools\update-armor-db-and-build.ps1"
    $updateArgs = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $updateScript,
        "-GameDir", $GameDir,
        "-ProjectRoot", $ProjectRoot,
        "-Mode", "update",
        "-AutoApply",
        "-FullTest",
        "-NoPause",
        "-ExpectedGameBuild", $gameVersion.Build,
        "-TargetGameVersion", $gameVersion.PublicVersion,
        "-PatchVersion", $gameVersion.PublicVersion,
        "-MaxShipCountDeltaPercent", [string]$MaxShipCountDeltaPercent,
        "-MaxRemovedPercent", [string]$MaxRemovedPercent,
        "-MaxDiffPercent", [string]$MaxDiffPercent
    )

    Write-Host ("Updating armor database for WoWS {0} ({1})..." -f $gameVersion.PublicVersion, $gameVersion.Build)
    & powershell @updateArgs
    if ($LASTEXITCODE -ne 0) {
        throw "ARMOR_UPDATE_FAILED: update-armor-db-and-build.ps1 exited with code $LASTEXITCODE"
    }

    if (-not (Test-Path -LiteralPath $packagePath)) {
        throw "PACKAGE_MISSING: $packagePath"
    }

    $changedPaths = @(Get-GitChangedPaths)
    $unexpected = @($changedPaths | Where-Object { $generatedPaths -notcontains $_ })
    if ($unexpected.Count -gt 0) {
        throw "UNEXPECTED_SOURCE_CHANGES: $($unexpected -join ', ')"
    }

    $diffInfo = Get-LatestDiff $runStart
    if ($null -eq $diffInfo -or $null -eq $diffInfo.Value) {
        throw "DIFF_MISSING: no diff was produced for this update."
    }
    $diff = $diffInfo.Value
    $addedCount = @($diff.added).Count
    $removedCount = @($diff.removed).Count
    $changedCount = @($diff.changed).Count
    $hash = (Get-FileHash -LiteralPath $packagePath -Algorithm SHA256).Hash.ToLowerInvariant()

    $commitSha = Invoke-GeneratedCommit $changedPaths ("chore: update armor data for WoWS {0} ({1})" -f $gameVersion.PublicVersion, $gameVersion.Build)
    $commitCompleted = [bool]$commitSha
    $remainingChanges = @(Get-GitChangedPaths)
    if ($remainingChanges.Count -gt 0) {
        throw "GIT_NOT_CLEAN_AFTER_COMMIT: $($remainingChanges -join ', ')"
    }

    Remove-RollbackSnapshot $rollbackSnapshot
    $rollbackSnapshot = $null

    $replyText = @"
Update armor data for World of Warships $($gameVersion.PublicVersion) (build $($gameVersion.Build)).

Armor database:
- Added ships: $addedCount
- Removed ships: $removedCount
- Changed ships: $changedCount

Package: $([System.IO.Path]::GetFileName($packagePath))
SHA-256: $hash
"@.Trim()

    $state.status = "READY_TO_PUBLISH"
    $state.targetUrl = $TargetUrl
    $state.steamBuildId = $steamBuildId
    $state.gameBuild = $gameVersion.Build
    $state.gameVersion = $gameVersion.PublicVersion
    $state.fullGameVersion = $gameVersion.FullVersion
    $state.databaseBuild = $gameVersion.Build
    $state.packagePath = $packagePath
    $state.packageSha256 = $hash
    $state.diffPath = $diffInfo.Path
    $state.addedShips = $addedCount
    $state.removedShips = $removedCount
    $state.changedShips = $changedCount
    $state.replyText = $replyText
    $state.publishedUrl = ""
    $state.publishedAt = ""
    $state.lastAttempt = Get-UtcTimestamp
    $state.lastError = ""
    Write-JsonAtomic $StatePath $state

    Write-Outcome ([ordered]@{
        status = "READY_TO_PUBLISH"
        checkedAt = $state.lastAttempt
        retry = $false
        steamBuildId = $steamBuildId
        gameBuild = $gameVersion.Build
        gameVersion = $gameVersion.PublicVersion
        databaseBuild = $gameVersion.Build
        packagePath = $packagePath
        packageSha256 = $hash
        diffPath = $diffInfo.Path
        addedShips = $addedCount
        removedShips = $removedCount
        changedShips = $changedCount
        commitSha = $commitSha
        replyText = $replyText
        targetUrl = $TargetUrl
    }) -Persist
    exit 0
} catch {
    $message = $_.Exception.Message
    if ($null -ne $rollbackSnapshot -and -not $commitCompleted) {
        try { Restore-RollbackSnapshot $rollbackSnapshot } catch { $message = "$message; rollback failed: $($_.Exception.Message)" }
    }

    $status = if ($message -match 'AUTOMATION_DIFF_UNSAFE') { "ABNORMAL_DIFF" } elseif ($message -match 'GIT_DIRTY_BLOCKED|GIT_BRANCH_BLOCKED') { "BLOCKED_DIRTY_WORKTREE" } else { "BUILD_FAILED" }
    $latestDiff = Get-LatestDiff $runStart
    $state.status = $status
    $state.targetUrl = $TargetUrl
    $state.steamBuildId = $steamBuildId
    if ($null -ne $gameVersion) {
        $state.gameBuild = $gameVersion.Build
        $state.gameVersion = $gameVersion.PublicVersion
        $state.fullGameVersion = $gameVersion.FullVersion
    }
    $state.databaseBuild = $databaseBuild
    if ($null -ne $latestDiff) { $state.diffPath = $latestDiff.Path }
    $state.lastAttempt = Get-UtcTimestamp
    $state.lastError = $message
    try { Write-JsonAtomic $StatePath $state } catch { $message = "$message; state write failed: $($_.Exception.Message)" }

    Write-Outcome ([ordered]@{
        status = $status
        checkedAt = Get-UtcTimestamp
        steamBuildId = $steamBuildId
        gameBuild = if ($null -ne $gameVersion) { $gameVersion.Build } else { "" }
        gameVersion = if ($null -ne $gameVersion) { $gameVersion.PublicVersion } else { "" }
        databaseBuild = $databaseBuild
        diffPath = if ($null -ne $latestDiff) { $latestDiff.Path } else { "" }
        error = $message
    }) -Persist
    exit 1
}
