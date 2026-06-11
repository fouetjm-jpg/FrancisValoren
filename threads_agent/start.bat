@echo off
cd /d "%~dp0"

:: Charger le .env
for /f "tokens=1,2 delims==" %%A in (.env) do set %%A=%%B

python agent.py
pause
