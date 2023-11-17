@echo off
@REM del db.sqlite3
del HomePage\migrations\0001_initial.py

call python manage.py flush --no-input
call migrate.bat
call python init_db.py

rmdir /s /q HomePage\migrations\__pycache__
rmdir /s /q HomePage\__pycache__
rmdir /s /q Vis4T_main\__pycache__
@REM call createsuperuser.bat