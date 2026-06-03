# DocBook use case diagram (Chapter 4.4) — Graphviz DOT -> PNG
$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot
$DotExe = "C:\Program Files\Graphviz\bin\dot.exe"
$DotFile = Join-Path $ProjectRoot "docbook_use_case.dot"
$PngFile = Join-Path $ProjectRoot "docbook_use_case.png"
$ThesisCopy = Join-Path $ProjectRoot "..\thesis-latex\figures\docbook_use_case.png"

if (-not (Test-Path $DotExe)) {
    Write-Host "Install Graphviz: winget install Graphviz.Graphviz"
    exit 1
}

& $DotExe -Gdpi=300 -Tpng $DotFile -o $PngFile
Copy-Item $PngFile $ThesisCopy -Force

Write-Host "Created:"
Write-Host "  $PngFile"
Write-Host "  $ThesisCopy"
