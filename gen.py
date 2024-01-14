import random
import os
import time

print('Welcome to the Generator v1')
print('''
░█▀▀░█▀▀░█▀█░█▀▀░█▀▄░█▀█░▀█▀░█▀█░█▀▄░░░█░█░▀█░
░█░█░█▀▀░█░█░█▀▀░█▀▄░█▀█░░█░░█░█░█▀▄░░░▀▄▀░░█░
░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀░░░░▀░░▀▀▀''')
print('''
[1] Proxis
[2] Discord Webhook URL
[3] Discord Nitro Codes''')
gen = input()


if gen == "1":
    chars = "10335171495678"

    for i in range(5000) :
        prvni = ''.join((random.choice(chars) for i in range(3)))
        druhe = ''.join((random.choice(chars) for i in range(2)))
        treti = ''.join((random.choice(chars) for i in range(3)))
        ctvrte = ''.join((random.choice(chars) for i in range(2)))
        pate = ''.join((random.choice(chars) for i in range(4)))


        result = prvni + "." + druhe + "." + treti + "." + ctvrte + ":" + pate

        output = open("proxis.txt", "a")
        output.write(result + "\n")

    print("5000 unchced proxies was generated in proxis.txt. \n Closing program...")
    time.sleep(2.5)
    exit()
        

if gen == "2":
    chars_web_code2 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNNM0123456789-"
    chars_web_code1 = "0123456789"

    for i in range(5000) :
        code1 = ''.join((random.choice(chars_web_code1) for i in range(18)))
        code2 = ''.join((random.choice(chars_web_code2) for i in range(68)))

        result = "https://discord.com/api/webhooks/" + code1 + "/" + code2

        output = open("webhooks.txt", "a")
        output.write(result + "\n")

    print("5000 unchced webhooks was generated in webhooks.txt. \n Closing program...")
    time.sleep(2.5)
    exit()

if gen == "3":
    
    chars_nitro_code2 = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM7894561230"

    for i in range(5000) :
        code1n = ''.join((random.choice(chars_nitro_code2) for i in range(16)))

        resultn = "https://discord.gg/gift/" + code1n

        output = open("nitro.txt", "a")
        output.write(resultn + "\n")

    print("5000 unchecked nitros was generated in nitro.txt. \n Closing program...")
    time.sleep(2.5)
    exit()
    