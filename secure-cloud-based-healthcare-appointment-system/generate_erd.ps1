# Generate DocBook ER diagram (Figure 4) using django-extensions + Graphviz.
# Run from this folder with venv activated.

$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot
$DotExe = "C:\Program Files\Graphviz\bin\dot.exe"

Set-Location $ProjectRoot

if (-not (Test-Path ".\venv\Scripts\python.exe")) {
    Write-Host "Create venv first: python -m venv venv"
    exit 1
}

Write-Host "Generating docbook_erd.dot ..."
.\venv\Scripts\python manage.py graph_models accounts bookings core -g --dot -o docbook_erd.dot

if (-not (Test-Path $DotExe)) {
    Write-Host "Graphviz not found at: $DotExe"
    Write-Host "Install: winget install Graphviz.Graphviz"
    Write-Host "Then re-run this script, or open docbook_erd.dot in https://dreampuf.github.io/GraphvizOnline/"
    exit 1
}

Write-Host "Rendering docbook_erd.png ..."
& $DotExe -Tpng docbook_erd.dot -o docbook_erd.png

$ThesisFigures = Join-Path $ProjectRoot "..\thesis-latex\figures\docbook_erd.png"
Copy-Item docbook_erd.png $ThesisFigures -Force

Write-Host "Done:"
Write-Host "  $ProjectRoot\docbook_erd.png"
Write-Host "  $ThesisFigures"
