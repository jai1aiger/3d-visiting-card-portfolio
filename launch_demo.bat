@echo off
echo ========================================================
echo   VTKRO 3D Interactive Visiting Card Suite
echo ========================================================
echo.
echo Starting local web server...
start /B "" "%~dp0.venv\Scripts\python.exe" "%~dp0server.py"
timeout /t 1 >nul
echo Opening Vercel-style 3D Physics Lanyard Badge Demo...
start http://localhost:3000/3d-lanyard-card-demo.html
echo Opening 360-degree Standalone Digital Card...
start http://localhost:3000/
echo Done! Enjoy exploring both 3D interactive experiences.
