@echo off

set CMD=%*
IF ["%CMD%"] == [""] set CMD=up

docker-compose ^
	-f "%~dp0\hadsag_platforms\docker-compose.yml" ^
	%CMD%
