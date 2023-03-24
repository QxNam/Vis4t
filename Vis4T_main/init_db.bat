@echo off

call migrate.bat
call python init_db.py
call createsuperuser.bat