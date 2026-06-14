@echo off
title NeuroWell AI — Selenium E2E Test Runner
color 0A
echo.
echo  =====================================================
echo   NeuroWell AI Live E2E Selenium Test Suite
echo   Target: https://neurowellai-49389.web.app
echo  =====================================================
echo.

REM Change to script directory
cd /d "%~dp0"

REM Run the test
python neurowellai_live_test.py

echo.
echo  =====================================================
echo   Tests complete! Check the selenium-tests folder
echo   for the NeuroWellAI_E2E_Report_*.xlsx file.
echo  =====================================================
echo.
pause
