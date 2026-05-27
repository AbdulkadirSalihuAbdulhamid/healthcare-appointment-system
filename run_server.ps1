# Quick Start Script for DocBook Healthcare System
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting DocBook Healthcare System" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to project root
$projectRoot = "C:\Users\Abdul\secure-cloud-based-healthcare-appointment-system"
Set-Location $projectRoot

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
    Write-Host "[OK] Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please create one with: python -m venv venv" -ForegroundColor Yellow
    exit 1
}

# Navigate to Django project directory
Set-Location "secure-cloud-based-healthcare-appointment-system"

# Check if database exists
if (-not (Test-Path "db.sqlite3")) {
    Write-Host ""
    Write-Host "Running migrations..." -ForegroundColor Yellow
    python manage.py migrate
    Write-Host "[OK] Migrations completed" -ForegroundColor Green
}

# Check Django setup
Write-Host ""
Write-Host "Checking Django configuration..." -ForegroundColor Yellow
python manage.py check --deploy 2>&1 | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Django configuration is valid" -ForegroundColor Green
} else {
    Write-Host "[WARN] Some warnings detected (non-critical)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Development Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Server will be available at:" -ForegroundColor White
Write-Host "  Homepage: http://127.0.0.1:8000/" -ForegroundColor Green
Write-Host "  Admin:    http://127.0.0.1:8000/super-admin/" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start the server
python manage.py runserver




