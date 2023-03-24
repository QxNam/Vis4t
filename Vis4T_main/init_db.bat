@echo off

call migrate.bat
call python init_db.py
@REM call createsuperuser.bat