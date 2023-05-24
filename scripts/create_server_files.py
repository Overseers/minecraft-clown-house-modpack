from distutils.dir_util import copy_tree
import subprocess
import requests
import json
import os

# Get structure setup
print("Setting up structure")
try:
	os.makedirs("./server_files")
except:
	print("\"server_files\" directory already exists")

try:
	os.makedirs("./server_files/mods")
except:
	print("\"server_files/mods\" directory already exists")

manifest = None
with open("./modpack/manifest.json", "r") as f:
	manifest = json.load(f)

# Setup forge
print("Setting up Forge")
minecraft_version = manifest['minecraft']['version']
forge_version = manifest['minecraft']['modLoaders'][0]['id'].split('forge-')[1]
forge_installer = requests.get(f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}/forge-{minecraft_version}-{forge_version}-installer.jar")
with open(f"./server_files/forge-installer.jar", "wb") as f:
	f.write(forge_installer.content)

# Get the mod jar files
print(f"Getting ({len(manifest["files"])}) mod files:")
headers = { "x-api-key": os.environ["CURSEFORGE_API_KEY"] }
for file_desc in manifest["files"]:
	mod_data = requests.get(f"https://api.curseforge.com/v1/mods/{file_desc['projectID']}/files/{file_desc['fileID']}", headers = headers).json()
	print(f"  - {mod_data['data']['displayName']}")
	mod_file = requests.get(mod_data["data"]["downloadUrl"])
	with open(f"./server_files/mods/{mod_data['data']['fileName']}", "wb") as f:
		f.write(mod_file.content)

# Copy startup scripts and configs over
copy_tree("./modpack/overrides", "./server_files")
copy_tree("./scripts/startup", "./server_files")
