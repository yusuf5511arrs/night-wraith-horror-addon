$ErrorActionPreference = 'Stop'
$base = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $base
python tools/generate_placeholder_assets.py
$items = @('behavior_pack', 'resource_pack')
$archive = Join-Path $base 'night_wraith_horror_release.zip'
if (Test-Path $archive) { Remove-Item $archive }
Compress-Archive -Path $items -DestinationPath $archive -Force
Write-Host "Created: $archive"
Write-Host "Rename .zip to .mcaddon manually in Windows Explorer."
