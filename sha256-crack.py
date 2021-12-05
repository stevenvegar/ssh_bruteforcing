import pwn
import sys

if len(sys.argv) != 2:
	print ("Falta ingresar el hash !\n")
	print ("Uso: " + sys.argv[0] + " <sha256sum>\n")
	sys.exit()

hash_decode = sys.argv[1]
pass_file = "pass-list-10000.txt"
attempts = 0


with pwn.log.progress("Intentando decodificar: " + hash_decode) as p:
	with open(pass_file, "r", encoding="utf-8") as passlist:
		for passw in passlist:
			passw = passw.strip("\n").encode("utf-8")
			pass_hash = pwn.sha256sumhex(passw)
			p.status("\n[" + str(attempts) + "] " + str(passw.decode("utf-8") + " == " + str(pass_hash)))
			if pass_hash == hash_decode:
				p.success("\nHash encontrado de la contraseña: " + str(passw.decode("utf-8")))
				exit()
			attempts += 1
		p.failure("Hash no encontrado!!!") 	