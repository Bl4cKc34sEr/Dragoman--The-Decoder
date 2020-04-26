#!/usr/bin/env python
# coding: utf-8
import os
import sys
import re
def main():
    if os.name == 'nt':
        os.system('cls')
    banner = """\u001b[36m
         ___                               _    __       
        / _ \___ ________ ___ _  ___ ___  (_)__/ /__ ____
       / ___/ _ `/ __/ _ `/  ' \(_-</ _ \/ / _  / -_) __/
      /_/   \_,_/_/  \_,_/_/_/_/___/ .__/_/\_,_/\__/_/   
                                  /_/     \u001b[0m               
                            
                           \u001b[32m - coded with <3 by Devansh Batham\u001b[0m 
    """
    print(banner)

message = input("Enter ASCII codes: ") #Decoding ascii to text

decodedMessage = ""

for item in message.split():
    decodedMessage += chr(int(item))   

print ("Decoded Message: ", decodedMessage) 
message = input("Enter message to encode: ") #encoding text to ascii
for ch in message:
    print ("Decoded string (in ASCII):")
    print (ord(ch))

