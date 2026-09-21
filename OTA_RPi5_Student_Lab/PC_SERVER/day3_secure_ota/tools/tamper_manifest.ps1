$ErrorActionPreference = "Stop"
$day3 = Split-Path $PSScriptRoot -Parent
$path = Join-Path $day3 "current\manifest.json"
$obj = Get-Content $path -Raw | ConvertFrom-Json
$obj.version = "9.9"
$json = $obj | ConvertTo-Json -Depth 10

# Save as UTF-8 without BOM for Windows PowerShell 5.1 compatibility.
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($path, $json, $utf8NoBom)

Write-Host "[ATTACK] Signed manifest changed after signing"
Write-Host "         version = 9.9"
