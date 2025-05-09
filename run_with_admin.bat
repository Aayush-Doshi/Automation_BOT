@echo off
set "PYTHON_SCRIPT=C:\Users\Aayush Doshi\OneDrive\Desktop\Python\main.py"
powershell -Command "Start-Process python -ArgumentList '\"%PYTHON_SCRIPT%\"' -Verb RunAs"
