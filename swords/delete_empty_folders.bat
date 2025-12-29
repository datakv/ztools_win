

@echo off

REM Parameters passed to this batch file
set PARAM1=%1

echo Deleting empty folders in  %PARAM1%


cd ../pysp

uv run delete_empty_folders\deleter.py %PARAM1%

pause
