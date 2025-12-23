@echo off
cd /d "%~dp0"
call envjarvis\Scripts\activate.bat
python main.py
