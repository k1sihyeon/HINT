$ErrorActionPreference = "Stop"
$day3 = Split-Path $PSScriptRoot -Parent
$path = Join-Path $day3 "current\firmware.json"
$obj = Get-Content $path -Raw | ConvertFrom-Json
$obj.behavior = "FORCE_HEADLAMP_OFF"
$json = $obj | ConvertTo-Json -Depth 10

# Save as UTF-8 without BOM for Windows PowerShell 5.1 compatibility.
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($path, $json, $utf8NoBom)

Write-Host "[ATTACK] Firmware payload changed after signing"
Write-Host "         behavior = FORCE_HEADLAMP_OFF"
