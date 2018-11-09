@ECHO OFF

:start
SET /P video=YouTube Link?: 
youtube-dl.exe --format bestvideo+bestaudio %video%

:choice
echo.
set /P c=More videos? [Y/N]? 
if /I "%c%" EQU "Y" goto :start
if /I "%c%" EQU "" goto :start
if /I "%c%" EQU "N" exit
goto :choice