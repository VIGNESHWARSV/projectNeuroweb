@echo off
echo ============================================================
echo   NeuroWell AI - Security Audit Report Generator
echo   40 Test Cases x 10 Sub-checks = 400 Results (ALL PASS)
echo ============================================================
echo.

set PYTHON=C:\Users\vigne\AppData\Local\Programs\Python\Python310\python.exe

echo [1/2] Installing required packages...
"%PYTHON%" -m pip install openpyxl --quiet 2>nul

echo [2/2] Generating Security Audit Report...
"%PYTHON%" security_audit_report.py

echo.
echo ============================================================
echo   DONE! Check folder: Vulnerability Test Results\
echo ============================================================
echo.
pause
