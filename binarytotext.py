#!/usr/bin/env python
# coding: utf-8

# In[ ]:
banner = """\u001b[36m
 █████▄  ██▀███   ▄▄▄       ▄████  ▒█████    ███▄ ▄███    ▄███    ▓▓▄     █ 
▒██▀ ██▌▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▒██▒  ██▒▓██▒▀█▀█ █▒▒██   ██ ▄ ██ ▀█   █ 
░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒██░  ██▒▓██    ▓██░▒██   ▀█▄▓ ██  ▀█ ██▒
░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▒█░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░   ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░  ░   ░░   ░   ░   ▒   ░ ░   ░ ░ ░ ░ ▒  ░      ░     ░   ▒      ░   ░ ░ 
   ░       ░           ░  ░      ░     ░ ░         ░         ░  ░         ░ 
 ░                                                                          
                            
                           \u001b[32m - coded with <3 For CTF's by Shivanshu Sharma\u001b[0m 
    """
print(banner)

word=input("Enter the text you want to be converted : ")
output = ""
for ch in word:
    output = output + "" + bin(ord(ch))[2:].zfill(8) 
print("Binary: ")
print(output)
word= input("Enter the binary text you want to convert: ")
bword= [word[i:i+8] for i in range(0, len(word), 8)]
output= ""
for bword in bword:
    a = int(bword, 2)
    ch = chr(a)
    output += ch
print(output)

