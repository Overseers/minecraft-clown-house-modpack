# Change these numbers to your requirements

RAM_MIN=1024
RAM_MAX=4096

# !!! Do not change anything past this point !!!

FORGE_INSTALLER_FILE="forge-installer.jar"
FORGE_UNIVERSAL_FILE="forge.jar"

if [ -f ${FORGE_INSTALLER_FILE} ]
then
	echo 'Setting up Forge'
	java -jar ${FORGE_INSTALLER_FILE} --installServer
	rm ${FORGE_INSTALLER_FILE} "${FORGE_INSTALLER_FILE}.log"
	mv forge-*.jar forge.jar
	echo 'Forge setup'
fi

echo 'Starting the Forge server'
java -Xms${RAM_MIN}M -Xmx${RAM_MAX}M -jar ${FORGE_UNIVERSAL_FILE} nogui
