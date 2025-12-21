@echo off
echo ========================================
echo   Virtual Assistant Buddy - Launcher
echo ========================================
echo.

REM Activate virtual environment
call envjarvis\Scripts\activate.bat

REM Check if activation was successful
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to activate virtual environment
    echo Please run setup.bat first
    pause
    exit /b 1
)

echo Virtual environment activated successfully
echo.
echo Starting Buddy Assistant...
echo.

REM Run the main application
python run.py

REM Deactivate virtual environment on exit
deactivate

pause
