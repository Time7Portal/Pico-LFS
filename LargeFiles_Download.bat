@echo off
setlocal

color 0C
echo A-Frame LARGE_FILES downloading...
echo !!! DO NOT CLOSE THIS WINDOW !!!

rem download zip file from google drive
powershell "(new-Object System.Net.WebClient).DownloadFile('https://drive.google.com/u/0/uc?id=1ALQUyWJ4IPgAFj2vhHH5E1ztQsq6TOKj&export=download', '.\LARGE_FILES.zip')"


rem check LARGE_FILES floder exists
IF EXIST ".\LARGE_FILES\" (
	:LOOP
	cls
	color 0C
	echo LARGE_FILES already exists. Shall I overwrite???
	set /p YN=[y/n]
	if /i "%YN%" == "y" goto YES
	if /i "%YN%" == "n" goto NO
	goto LOOP
	
	:YES
	color 02
	echo A-Frame LARGE_FILES removing...
	powershell Remove-Item -path '.\LARGE_FILES' -recurse
	
	color 02
	echo A-Frame LARGE_FILES extracting...
	powershell Expand-Archive -LiteralPath '.\LARGE_FILES.zip'  -DestinationPath '.\'
	goto QUIT
	
	:NO
	color 0C
	echo Please run it after your preperation.
	pause
	goto QUIT
	
) else (
    rem floder does not exists
	
	color 02
	echo A-Frame LARGE_FILES extracting...
	powershell Expand-Archive -LiteralPath '.\LARGE_FILES.zip'  -DestinationPath '.\'
)


:QUIT


