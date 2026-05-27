# Interactive Server Start Script
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting DocBook Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to project root
$projectRoot = "C:\Users\Abdul\secure-cloud-based-healthcare-appointment-system"
Set-Location $projectRoot

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Navigate to Django project
Set-Location "secure-cloud-based-healthcare-appointment-system"

Write-Host ""
Write-Host "Checking Django setup..." -ForegroundColor Yellow
python manage.py check

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Server on Port 8000" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Server URLs:" -ForegroundColor Green
Write-Host "  http://127.0.0.1:8000" -ForegroundColor White
Write-Host "  http://localhost:8000" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
Write-Host ""

# Start server - this will run in foreground so you can see any errors
python manage.py runserver 127.0.0.1:8000

