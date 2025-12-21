@echo off
echo ========================================
echo   Virtual Assistant Buddy - Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo Python found. Creating virtual environment...
echo.

REM Create virtual environment if it doesn't exist
if not exist "envjarvis" (
    python -m venv envjarvis
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

REM Activate virtual environment
call envjarvis\Scripts\activate.bat

echo.
echo Installing/Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo To start the assistant, run: start.bat
echo.

deactivate
pause
