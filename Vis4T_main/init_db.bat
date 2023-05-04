@echo off
del db.sqlite3
del HomePage\migrations\0001_initial.py

call migrate.bat
call python init_db.py
@REM call createsuperuser.bat