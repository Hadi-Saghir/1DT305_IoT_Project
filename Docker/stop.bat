@echo off

docker-compose ^
	-f "%~dp0\docker-compose.yml" ^
	stop
