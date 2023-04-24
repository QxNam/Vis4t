@echo off
del db.sqlite3
del HomePage\migrations\0001_initial.py
rmdir /s /q HomePage\migrations\__pycache__
rmdir /s /q HomePage\__pycache__
rmdir /s /q Vis4T_main\__pycache__
call migrate.bat
call python init_db.py
@REM call createsuperuser.bat