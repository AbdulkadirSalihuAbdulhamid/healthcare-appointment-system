# Render cloud architecture diagram (Figure 1) — Graphviz DOT -> PNG
$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot
$DotExe = "C:\Program Files\Graphviz\bin\dot.exe"
$DotFile = Join-Path $ProjectRoot "docbook_architecture.dot"
$PngFile = Join-Path $ProjectRoot "docbook_architecture.png"
$ThesisCopy = Join-Path $ProjectRoot "..\thesis-latex\figures\docbook_architecture.png"

if (-not (Test-Path $DotExe)) {
    Write-Host "Install Graphviz: winget install Graphviz.Graphviz"
    exit 1
}

# High DPI for readable text in Word thesis
& $DotExe -Gdpi=300 -Tpng $DotFile -o $PngFile
Copy-Item $PngFile $ThesisCopy -Force

Write-Host "Created:"
Write-Host "  $PngFile"
Write-Host "  $ThesisCopy"
