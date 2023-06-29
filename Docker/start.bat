@echo off

set CMD=%*
IF ["%CMD%"] == [""] set CMD=up

docker-compose ^
	-f "%~dp0\docker-compose.yml" ^
	%CMD%
