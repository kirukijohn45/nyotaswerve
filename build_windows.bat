@echo off
REM =====================================================
REM  Nyotaswerve CRM - Windows Build Script
REM  Run this on a Windows machine with Python 3.10+
REM  It will create a standalone NyotaswerveCRM.exe
REM =====================================================

echo.
echo ╔══════════════════════════════════════════════╗
echo ║   Building Nyotaswerve CRM for Windows        ║
echo ╚══════════════════════════════════════════════╝
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python 3.10+ from python.org
    pause
    exit /b 1
)
echo ✅ Python found: 
python --version

REM Install dependencies
echo.
echo 📦 Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)
echo ✅ Dependencies installed

REM Install PyInstaller
pip install pyinstaller
if %errorlevel% neq 0 (
    echo ❌ Failed to install PyInstaller
    pause
    exit /b 1
)
echo ✅ PyInstaller installed

REM Clean previous builds
echo.
echo 🧹 Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM Build the executable
echo.
echo 🏗️  Building executable (this may take 3-5 minutes)...
echo.

pyinstaller --onefile --windowed --name NyotaswerveCRM ^
    --add-data "templates;templates" ^
    --add-data "static;static" ^
    --add-data "config;config" ^
    --add-data "accounts;accounts" ^
    --add-data "contacts;contacts" ^
    --add-data "leads;leads" ^
    --add-data "deals;deals" ^
    --add-data "tasks;tasks" ^
    --add-data "products;products" ^
    --add-data "invoices;invoices" ^
    --add-data "tally;tally" ^
    --add-data "dashboard;dashboard" ^
    --add-data "seed_data.py;." ^
    --add-data "requirements.txt;." ^
    --hidden-import django ^
    --hidden-import django.contrib.admin ^
    --hidden-import django.contrib.auth ^
    --hidden-import django.contrib.contenttypes ^
    --hidden-import django.contrib.sessions ^
    --hidden-import django.contrib.messages ^
    --hidden-import django.contrib.staticfiles ^
    --hidden-import django.contrib.humanize ^
    --hidden-import rest_framework ^
    --hidden-import corsheaders ^
    --hidden-import django_filters ^
    --hidden-import import_export ^
    --hidden-import PIL ^
    --hidden-import sqlparse ^
    --hidden-import asgiref ^
    --hidden-import whitenoise ^
    --hidden-import accounts ^
    --hidden-import contacts ^
    --hidden-import leads ^
    --hidden-import deals ^
    --hidden-import tasks ^
    --hidden-import products ^
    --hidden-import invoices ^
    --hidden-import tally ^
    --hidden-import dashboard ^
    --hidden-import config ^
    --collect-submodules django ^
    --exclude-module tkinter ^
    --exclude-module matplotlib ^
    --exclude-module scipy ^
    --exclude-module pandas ^
    --exclude-module notebook ^
    --exclude-module jupyter ^
    --exclude-module test ^
    --exclude-module unittest ^
    crm_launcher.py

if %errorlevel% neq 0 (
    echo ❌ Build failed!
    pause
    exit /b 1
)

echo.
echo ✅ BUILD SUCCESSFUL!
echo.
echo 📍 Your executable is at: dist\NyotaswerveCRM.exe
echo 📦 Size: 
for %%I in (dist\NyotaswerveCRM.exe) do echo    %%~zI bytes
echo.
echo To run, double-click NyotaswerveCRM.exe
echo The CRM will open in your browser at http://localhost:8000
echo Login: admin / admin123
echo.

pause