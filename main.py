import json
import subprocess
import os
import shutil
import requests

un=raw_input("GitHub Username > ")
r=requests.get("https://api.github.com/users/"+un+"/repos")
dat=json.loads(r.text)
for repo in dat:
	url=repo["ssh_url"]
	subprocess.call(["git","clone",url])
	os.chdir(repo["name"])
	shutil.copy("../LICENSE.txt",".")
	subprocess.call(["git","add","LICENSE.txt"])
	subprocess.call(["git","commit","-m","Added LICENSE."])
	subprocess.call(["git","push"])
	os.chdir("..")
