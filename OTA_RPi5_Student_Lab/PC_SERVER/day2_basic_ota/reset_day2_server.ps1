$ErrorActionPreference = "Stop"
Copy-Item (Join-Path $PSScriptRoot "templates\manifest.json") (Join-Path $PSScriptRoot "server\manifest.json") -Force
Copy-Item (Join-Path $PSScriptRoot "templates\firmware_v2.json") (Join-Path $PSScriptRoot "server\firmware_v2.json") -Force
Write-Host "Day 2 PC server reset complete: release=v2 NORMAL"
