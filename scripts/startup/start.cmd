@ECHO off

:: Change these numbers to your requirements
SET RAM_MIN=1024
SET RAM_MAX=4096

:: !!! Do not change anything past this point !!!

SET FORGE_INSTALLER_FILE=forge-installer.jar
SET FORGE_UNIVERSAL_FILE=forge.jar

if exist %FORGE_INSTALLER_FILE% (
	ECHO Setting up Forge
	java -jar %FORGE_INSTALLER_FILE% --installServer
	DEL %FORGE_INSTALLER_FILE% %FORGE_INSTALLER_FILE%.log
	MOVE forge-*.jar forge.jar
	ECHO Forge setup
)

ECHO Starting the Forge server
java -Xms%RAM_MIN%M -Xmx%RAM_MAX%M -jar %FORGE_UNIVERSAL_FILE% nogui
