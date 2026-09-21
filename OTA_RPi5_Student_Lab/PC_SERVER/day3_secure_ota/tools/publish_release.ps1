param([Parameter(Mandatory=$true)][string]$Release)
$ErrorActionPreference = "Stop"
$day3 = Split-Path $PSScriptRoot -Parent
$src = Join-Path $day3 ("releases\" + $Release)
$dst = Join-Path $day3 "current"
if (-not (Test-Path $src -PathType Container)) { throw "Release not found: $Release" }
Remove-Item (Join-Path $dst '*') -Force -ErrorAction SilentlyContinue
Copy-Item (Join-Path $src '*') $dst -Force
Write-Host "[PUBLISH] $Release -> current"
