@REM @echo off
setlocal EnableDelayedExpansion

IF EXIST ImageMagick (
    set "path=%~dp0ImageMagick"
) ELSE (
    set /p "path=Enter ImageMagick folder location: "
)
@REM choices:
set /p "ext=Enter file extension (empty for png): "
IF "%ext%"=="" (
    set converter = ""
    set ext=png
    echo !ext!
) ELSE (
    set converter = "%path%\convert.exe %%a out/%%~na.%ext%"
)

set /p "name=Rename? (empty for no): "
@REM IF "%name%"=="" (
@REM     set renamer = ""
@REM ) 
@REM ELSE (
@REM     set /A counter=""
@REM     set renamer = "rename "%%a" "%name%!counter!%ext%" set /A counter+=1"
@REM )

set /p "resize=Resize? (empty for no, leave x in between): "


for /r "%~dp0in" %%a in (*) do (
    IF "%name%"=="" set name %%~na
    %converter%
    %resizer%
)

@REM for /r "%~dp0in" %%a in (*) do (
@REM     IF "%name%"=="" set name %%~na
@REM     %path%\convert.exe %%a out/%%~na.%ext%
@REM     @REM rename "%%a" "%name%!counter!%%~xa"
@REM     %path%\convert.exe %%a -resize %resize% out/%name%!counter!%%~xa
@REM     set /A counter+=1
@REM )

@REM for /r "%~dp0in" %%a in (*) do %path%\convert.exe %%a out/%%~na.%ext%

@REM set /p "name=Rename? (empty for no): "
@REM IF "%name%"=="" (
@REM   echo "skipping"
@REM ) ELSE (
@REM     set /A counter=""
@REM     for /r "%~dp0out" %%r in (*) do (
@REM         rename "%%r" "%name%!counter!%%~xr"
@REM         set /A counter+=1
@REM     )
@REM )

@REM set /p "resize=Resize? (empty for no, leave x in between): "
@REM IF "%resize%"=="" (
@REM   echo "skipping"
@REM ) ELSE (
@REM     for /r "%~dp0out" %%r in (*) do %path%\convert.exe %%r -resize %resize% out_resized/%%~nr.%ext%
@REM )