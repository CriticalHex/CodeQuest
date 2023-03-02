@echo off
set formatted_input=%*
set formatted_input=%formatted_input:-=_%
mkdir %formatted_input%
set top_dir=%CD%
cd %formatted_input%
powershell -C "wget "https://lmcodequestacademy.com/api/static/problems/%*" -O "%formatted_input%.pdf"">nul
powershell -C "wget "https://lmcodequestacademy.com/api/static/samples/%*" -O "samples.zip"">nul
powershell -C "Expand-Archive -Force samples.zip samples">nul
del samples.zip
copy "samples\1.in" "input.txt">nul
copy "samples\1.out" "output.txt">nul
rmdir /S /Q samples
copy "%top_dir%\template.py" "%formatted_input%.py">nul
rem break>input.txt
cd %top_dir%
call code %formatted_input%\%formatted_input%.py
call code %formatted_input%\%formatted_input%.pdf
call code %formatted_input%\input.txt