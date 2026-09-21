param(
    [int]$Port = 8000,
    [string]$Root = (Join-Path $PSScriptRoot "server")
)

$ErrorActionPreference = "Stop"
$rootFull = [System.IO.Path]::GetFullPath($Root)
$listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Any, $Port)
$listener.Start()
Write-Host "[SERVER] Root : $rootFull"
Write-Host "[SERVER] Listen: http://0.0.0.0:$Port/"
Write-Host "[SERVER] Stop  : Ctrl + C"
Write-Host "[TIP] Windows Firewall prompt appears -> allow Private networks only."

function Send-Response($stream, [int]$status, [string]$statusText, [byte[]]$body, [string]$contentType) {
    $header = "HTTP/1.1 $status $statusText`r`nContent-Length: $($body.Length)`r`nContent-Type: $contentType`r`nConnection: close`r`n`r`n"
    $headerBytes = [System.Text.Encoding]::ASCII.GetBytes($header)
    $stream.Write($headerBytes, 0, $headerBytes.Length)
    if ($body.Length -gt 0) { $stream.Write($body, 0, $body.Length) }
    $stream.Flush()
}

try {
    while ($true) {
        if (-not $listener.Pending()) {
            Start-Sleep -Milliseconds 100
            continue
        }

        $client = $listener.AcceptTcpClient()
        try {
            $stream = $client.GetStream()
            $reader = New-Object System.IO.StreamReader($stream, [System.Text.Encoding]::ASCII, $false, 4096, $true)
            $requestLine = $reader.ReadLine()
            if ([string]::IsNullOrWhiteSpace($requestLine)) { continue }
            do { $line = $reader.ReadLine() } while ($null -ne $line -and $line -ne "")

            if ($requestLine -match '^GET\s+([^\s]+)') {
                $urlPath = $Matches[1].Split('?')[0]
                $rel = [System.Uri]::UnescapeDataString($urlPath).TrimStart('/')
                if ([string]::IsNullOrWhiteSpace($rel)) { $rel = "manifest.json" }
                $candidate = [System.IO.Path]::GetFullPath((Join-Path $rootFull $rel))
                if (-not $candidate.StartsWith($rootFull, [System.StringComparison]::OrdinalIgnoreCase)) {
                    $body = [System.Text.Encoding]::UTF8.GetBytes("Forbidden")
                    Send-Response $stream 403 "Forbidden" $body "text/plain; charset=utf-8"
                    Write-Host "[HTTP] GET /$rel -> 403"
                }
                elseif (Test-Path $candidate -PathType Leaf) {
                    $body = [System.IO.File]::ReadAllBytes($candidate)
                    $ext = [System.IO.Path]::GetExtension($candidate).ToLowerInvariant()
                    $ct = if ($ext -eq ".json") { "application/json; charset=utf-8" } elseif ($ext -eq ".sig") { "application/octet-stream" } else { "application/octet-stream" }
                    Send-Response $stream 200 "OK" $body $ct
                    Write-Host "[HTTP] GET /$rel -> 200 ($($body.Length) bytes)"
                }
                else {
                    $body = [System.Text.Encoding]::UTF8.GetBytes("Not Found")
                    Send-Response $stream 404 "Not Found" $body "text/plain; charset=utf-8"
                    Write-Host "[HTTP] GET /$rel -> 404"
                }
            }
            else {
                $body = [System.Text.Encoding]::UTF8.GetBytes("Method Not Allowed")
                Send-Response $stream 405 "Method Not Allowed" $body "text/plain; charset=utf-8"
                Write-Host "[HTTP] Unsupported request: $requestLine"
            }
        }
        catch {
            Write-Warning $_.Exception.Message
        }
        finally {
            $client.Close()
        }
    }
}
finally {
    $listener.Stop()
    Write-Host "[SERVER] stopped"
}
