@echo off
:: Face Recognition Setup Script
:: This script helps new users set up face authentication with their own face

echo.
echo ========================================
echo   FACE RECOGNITION SETUP
echo ========================================
echo.
echo This will set up face authentication with YOUR face.
echo.

:: Check if Python is available
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found! Please install Python first.
    pause
    exit /b 1
)
echo Python found!
echo.

:: Activate virtual environment
echo [2/4] Activating virtual environment...
if exist "envjarvis\Scripts\activate.bat" (
    call envjarvis\Scripts\activate.bat
    echo Virtual environment activated!
) else (
    echo WARNING: Virtual environment not found. Using system Python.
)
echo.

:: Clean old training data
echo [3/4] Cleaning old training data...
if exist "assist\Engine\auth\samples" (
    del /Q "assist\Engine\auth\samples\*.jpg" 2>nul
    del /Q "assist\Engine\auth\samples\*.png" 2>nul
    echo Old samples removed.
) else (
    mkdir "assist\Engine\auth\samples"
    echo Samples folder created.
)

if exist "assist\Engine\auth\trainer" (
    del /Q "assist\Engine\auth\trainer\trainer.yml" 2>nul
    echo Old trainer model removed.
) else (
    mkdir "assist\Engine\auth\trainer"
    echo Trainer folder created.
)
echo.

:: Capture face samples
echo [4/4] Starting face capture...
echo.
echo INSTRUCTIONS:
echo - You will enter a User ID (any number, e.g., 0)
echo - Look at the camera from different angles
echo - The system will capture 100 images automatically
echo - Press ESC to stop early (min 50 images recommended)
echo.
pause
echo.

python assist\Engine\auth\sample.py

if errorlevel 1 (
    echo.
    echo ERROR: Face capture failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   TRAINING FACE RECOGNITION MODEL
echo ========================================
echo.
echo This will take a few seconds...
echo.

python assist\Engine\auth\trainer.py

if errorlevel 1 (
    echo.
    echo ERROR: Training failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SETUP COMPLETE!
echo ========================================
echo.
echo Your face has been registered successfully.
echo You can now use face authentication when starting the app.
echo.
echo To re-train with a different face, run this script again.
echo.
pause
