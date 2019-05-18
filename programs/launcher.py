#! /usr/bin/python3
import sys, os
import json
import urllib.request, urllib.parse, urllib.error
from zipfile import ZipFile, BadZipfile		# JARs are secretly ZIP files.

currentOS = None
platform = sys.platform
if platform.startswith("win"):
	currentOS = "windows"
elif platform == "darwin":
	currentOS = "osx"
else:
	currentOS = "linux"

bits = "32"
if sys.maxsize == 9223372036854775807:
	bits = "64"

print("Detected OS: %s-bit %s" % (bits, currentOS))

def makeDir(dirname):
	if currentOS == "windows":
		os.system("MD " + dirname.replace("/", "\\") + " 2>NUL")
	else:
		os.system("mkdir -p " + dirname)

# We will use this default "launcher_profiles.json" template if no file is found yet.
launcherProfiles = {
	"selectedProfile":	"N/A",
	"profiles":	{}
}

class Profile:
	def __init__(self, data):
		self.data = data
		self.name = data["name"]
		self.version = data["lastVersionId"]
		self.libs = []
		self.fileIndex = [("mcdata/versions/%s/%s.json" % (self.version, self.version),
					"http://s3.amazonaws.com/Minecraft.Download/versions/%s/%s.json" % (self.version, self.version)),

					("mcdata/versions/%s/%s.jar" % (self.version, self.version),
					"http://s3.amazonaws.com/Minecraft.Download/versions/%s/%s.jar" % (self.version, self.version))
		]

		# Try loading the version info so that we can launch.
		f = None
		try:
			f = open("mcdata/versions/%s/%s.json" % (self.version, self.version), "rb")
		except IOError:
			makeDir("mcdata/versions/%s" % self.version)
			self.downloadFile("mcdata/versions/%s/%s.json" % (self.version, self.version),
					"http://s3.amazonaws.com/Minecraft.Download/versions/%s/%s.json" % (self.version, self.version)
			)
			f = open("mcdata/versions/%s/%s.json" % (self.version, self.version), "rb")
		sdata = f.read()
		f.close()

		self.versionInfo = json.loads(sdata)
		self.mainClass = self.versionInfo["mainClass"]
		self.mcargs = self.versionInfo["minecraftArguments"]
		self.jar = "versions/%s/%s.jar" % (self.version, self.version)
		for libinfo in self.versionInfo["libraries"]:
			librep = libinfo.get("url", "https://libraries.minecraft.net/")
			name = libinfo["name"]
			package, name, version = name.split(":")
			relpath = package.replace(".", "/") + "/" + name + "/" + version + "/" + name + "-" + version + ".jar"
			self.fileIndex.append(("mcdata/libraries/" + relpath, librep + relpath))
			self.libs.append("libraries/" + relpath)

			if "natives" in libinfo:
				if currentOS in libinfo["natives"]:
					makeDir("mcdata/natives")
					natstr = libinfo["natives"][currentOS].replace("${arch}", bits)
					relpath = package.replace(".", "/") + "/" + name + "/" + version + "/" + name + "-" + version + "-" + natstr + ".jar"
					libpath = "mcdata/libraries/" + relpath
					liburl = librep + relpath
					if not os.path.exists(libpath):
						self.downloadFile(libpath, liburl)
						print(">Extract " + libpath)
						try:
							zipfile = ZipFile(libpath, "r")
							for name in zipfile.namelist():
								if not (name.startswith("META-INF") or name.startswith(".")):
									zipfile.extract(name, "mcdata/natives")
							zipfile.close()
						except BadZipfile:
							print("!!! NOT A REAL JAR/ZIP FILE  !!!")
							print("!!! SKIPPING, BUT BEWARE     !!!")
							print("!!! WILL TRY AGAIN NEXT TIME !!!")
							try:
								os.remove(libpath)
							except:
								pass

		# We must also get the assets index.
		assetsName = self.versionInfo.get("assets", "legacy")
		assetsIndexFile = "mcdata/assets/indexes/%s.json" % assetsName
		assetsIndexLink = "https://s3.amazonaws.com/Minecraft.Download/indexes/%s.json" % assetsName
		self.downloadFile(assetsIndexFile, assetsIndexLink)

		f = open(assetsIndexFile, "rb")
		assetsData = json.loads(f.read())
		f.close()

		for key, value in list(assetsData["objects"].items()):
			hash = value["hash"]
			pref = hash[:2]
			self.fileIndex.append((
				"mcdata/assets/objects/%s/%s" % (pref, hash),
				"http://resources.download.minecraft.net/%s/%s" % (pref, hash)
			))

	def downloadFile(self, filename, url):
		print(">Download " + url)
		dirname = filename.rsplit("/", 1)[0]
		makeDir(dirname)

		inf = urllib.request.urlopen(url)
		outf = open(filename, "wb")
		while 1:
			b = inf.read(1)
			if len(b) == 0:
				break
			else:
				outf.write(b)
		inf.close()
		outf.close()

	def downloadMissingFiles(self):
		for filename, url in self.fileIndex:
			if not os.path.exists(filename):
				self.downloadFile(filename, url)

	def launchcmd(self, username = "MinecraftPlayer"):
		libs = [self.jar]
		libs.extend(self.libs)
		cp = ":".join(libs)
		if currentOS == "windows":
			# LOL
			cp = ";".join(libs).replace("/", "\\")
		args = self.mcargs
		args = args.replace("${auth_player_name}", username)
		args = args.replace("${version_name}", self.version)
		args = args.replace("${game_directory}", ".")
		args = args.replace("${game_assets}", "assets")		# Not even used.
		args = args.replace("${assets_root}", "assets")		# Not even used.
		args = args.replace("${auth_uuid}", "null")
		args = args.replace("${auth_access_token}", "null")
		args = args.replace("${assets_index_name}", self.versionInfo.get("assets", "legacy"))
		args = args.replace("${user_properties}", "{}")
		args = args.replace("${user_type}", "offline")

		return 'java -cp "%s" -Djava.library.path=natives %s %s' % (cp, self.mainClass, args)

launcherProfiles = {
	"selectedProfile": "N/A",
	"profiles": {
		"teachcraft": {
			"name": "teachcraft",
			"lastVersionId": "1.12"
		}
	}
}

username = input("Username: ")
p = Profile(launcherProfiles["profiles"]["teachcraft"])
p.downloadMissingFiles()
print("> Starting Minecraft...")
os.system("cd mcdata && %s" % p.launchcmd(username))
