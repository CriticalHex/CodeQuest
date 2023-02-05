@echo off
set formatted_input=%*
set formatted_input=%formatted_input:-=_%
mkdir %formatted_input%
set top_dir=%CD%
cd %formatted_input%
powershell.exe -C "wget "https://lmcodequestacademy.com/api/static/problems/%*" -O "%formatted_input%.pdf""
copy "%top_dir%\template.py" "%formatted_input%.py"
> input.txt
cd %top_dir%
call code %formatted_input%\%formatted_input%.py
call code %formatted_input%\%formatted_input%.pdf
call code %formatted_input%\input.txt