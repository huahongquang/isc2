@echo off
chcp 65001 > nul
title ISC2 Certified in Cybersecurity (CC) - Study App
cls
echo ====================================================================
echo        ISC2 CERTIFIED IN CYBERSECURITY (CC) LEARNING PLATFORM
echo               Kho hoc tap & Luyen thi CC chinh hang
echo ====================================================================
echo.
echo [*] Dang khoi dong may chu web va mo trinh duyet...
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Khong tim thay Python tren he thong. Vui long cai dat Python 3.10+ de chay ung dung.
    pause
    exit /b 1
)

python "%~dp0app.py"
pause
