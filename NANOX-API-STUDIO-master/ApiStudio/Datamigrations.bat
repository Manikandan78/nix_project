@echo off

REM Set the path to your virtual environment
set VENV_PATH=C:\B2E\NANOX-API-STUDIO-master\Datamigration\venv

REM Activate the virtual environment
call %VENV_PATH%\Scripts\activate.bat

cd /d C:\B2E\NANOX-API-STUDIO-master\Datamigration


REM Run the Python service command
python manage.py runserver 127.0.0.1:8012