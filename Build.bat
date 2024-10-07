@echo off
setlocal enabledelayedexpansion
title LLD Builder ^| Version 1.2 Loaded
set GREEN=[32m
set CYAN=[36m
set YELLOW=[33m
set RESET=[0m

:menu
cls
echo ====================================================================================
echo                                 %CYAN%LLD Version 1.2%RESET%                
echo ====================================================================================
echo  %GREEN%[X] %RESET%- %CYAN%Exit
echo  %GREEN%[G] %RESET%- %CYAN%Github
echo  %GREEN%[Y] %RESET%- %CYAN%Youtube
echo  %GREEN%[I] %RESET%- %CYAN%Start LLD%RESET%
echo ====================================================================================
echo                                    %CYAN%v1.2 %GREEN%BETA    %RESET%                
echo ====================================================================================
set /p choice="Select an option: "

if /i "%choice%"=="X" (
    exit
) else if /i "%choice%"=="G" (
    start https://github.com/questionMrk
    goto menu
) else if /i "%choice%"=="Y" (
    start https://www.youtube.com/@questionmark_3m
    goto menu
) else if /i "%choice%"=="I" (
    call :installPackage
    goto menu
) else (
    echo Invalid choice! Please try again.
    pause
    goto menu
)

:installPackage
cls
echo ====================================================================================
echo %CYAN%                                LLD Debug Page                 %RESET%
echo ====================================================================================
echo %GREEN%[+] %RESET%- %CYAN%LLD.py setting up! %RESET%
echo %GREEN%[+] %RESET%- %CYAN%Installing Packages %RESET%
echo %CYAN%
pip install colorama
pip install requests
pip install messagebox
echo %GREEN%[+] %RESET%- %CYAN%Finished Installing %RESET%
echo %GREEN%[+] %RESET%- %CYAN%Executing LLD.py %RESET%
echo %CYAN%
for /f "usebackq delims=" %%a in ("LLD.py") do (
        echo %%a
    )
echo %GREEN%[+] %RESET%- %CYAN%Fully Executed! %RESET%
echo %GREEN%[+] %RESET%- %CYAN%Welcome to the most simplest Multi-Tool! %RESET%
echo %GREEN%[+] %RESET%- %CYAN%You can now exit this script! %RESET%
echo ====================================================================================
call LLD.py
cls