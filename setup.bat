@echo off
set dir_name=%*
mkdir %dir_name%
set top_dir=%CD%
cd %dir_name%
powershell.exe -C "wget "https://lmcodequestacademy.com/api/static/problems/%*" -O "%dir_name%.pdf"" >nul
copy "%top_dir%\template.py" "%*.py" >nul
nul> input.txt
cd %top_dir%