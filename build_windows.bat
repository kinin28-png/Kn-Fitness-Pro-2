@echo off
echo =======================================================
echo   Kn Fitness Pro 2 - Windows .EXE Builder
echo =======================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in your system PATH!
    echo Please install Python 3.10+ from https://www.python.org and check "Add Python to PATH".
    pause
    exit /b 1
)

echo [1/3] Setting up Python virtual environment...
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate

echo [2/3] Installing dependencies (PySide6, PyInstaller)...
pip install --upgrade pip
pip install -r requirements.txt

echo [3/3] Building standalone Windows executable...
pyinstaller Kn_Fitness_Pro_Windows.spec --clean --noconfirm

echo.
echo =======================================================
echo   BUILD COMPLETED SUCCESSFULLY!
echo   Your standalone .exe is ready in:
echo   dist\Kn Fitness Pro.exe
echo =======================================================
echo.
pause

