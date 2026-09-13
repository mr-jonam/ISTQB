@echo off
setlocal
cd /d "%~dp0"

where docker >nul 2>&1
if errorlevel 1 (
  echo Docker non trovato. Installa e avvia Docker Desktop, poi riprova.
  exit /b 1
)

docker info >nul 2>&1
if errorlevel 1 (
  echo Docker Desktop non e avviato.
  exit /b 1
)

echo Avvio Quality Engineering Learning Hub...
docker compose up --build --detach
if errorlevel 1 exit /b 1

echo Web app disponibile su http://127.0.0.1:8000
start "" http://127.0.0.1:8000
endlocal
