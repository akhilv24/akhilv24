@echo off
REM Portfolio Dashboard Application Launcher for Windows
REM This script sets up and runs the Streamlit application

echo.
echo 🚀 Starting Portfolio Dashboard Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed.
    echo Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✓ Python found
python --version

REM Check if virtual environment exists
if not exist "venv" (
    echo.
    echo 📦 Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ❌ Error: Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo ✓ Virtual environment created
)

REM Activate virtual environment
echo.
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Error: Failed to activate virtual environment.
    pause
    exit /b 1
)

REM Install/Update dependencies
echo.
echo 📥 Installing dependencies...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ❌ Error: Failed to install dependencies.
    pause
    exit /b 1
)

echo ✓ Dependencies installed

REM Run the Streamlit app
echo.
echo 🎉 Launching application...
echo 📍 The app will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server.
echo.

streamlit run app.py
