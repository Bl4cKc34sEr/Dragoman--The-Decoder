#!/usr/bin/env python
# coding: utf-8
banner = """\u001b[36;1m
 █████▄  ██▀███   ▄▄▄       ▄████  ▒█████    ███▄ ▄███    ▄███    ▓▓▄     █ 
▒██  ██▌▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▒██   ██▒ ██▒▀█▀█ █ ▒██   ██ ▄ ██ ▀█   █ 
░██   █▌▓██  ▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒██░  ██ ▓██    ▓██▒ ██   ▀█▄▓ ██  ▀█ ██▒
░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▒█░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░   ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░  ░   ░░   ░   ░   ▒   ░ ░   ░ ░ ░ ░ ▒  ░      ░     ░   ▒      ░   ░ ░ 
   ░       ░            ░  ░      ░    ░ ░         ░         ░  ░         ░ 
 ░                                                                         
                           
                           \u001b[32;1m - coded with <3 For CTF's by Shivanshu Sharma\u001b[0m 
    """
print(banner)  

def encryptRailFence(text, key): 

    rail = [['\n' for i in range(len(text))] 
                for j in range(key)] 

    dir_down = False
    row, col = 0, 0

    for i in range(len(text)): 

        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down 

        rail[row][col] = text[i] 
        col += 1

        if dir_down: 
            row += 1
        else: 
            row -= 1
	# now we can construct the cipher 
	# using the rail matrix 
    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    return("" . join(result)) 


def decryptRailFence(cipher, key): 


    rail = [['\n' for i in range(len(cipher))] 
                for j in range(key)] 

    dir_down = None
    row, col = 0, 0
    

    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down: 
            row += 1
        else: 
            row -= 1

    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
            (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
 
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 

        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False

        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1

        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 

if __name__ == "__main__": 
  
    print(encryptRailFence(input("Encode your message to key 2: "),2)) 
    print(decryptRailFence(input("Decode your message to key 2: "),2)) 
    print(encryptRailFence(input("Encode your message to key 3: "),3)) 
    print(decryptRailFence(input("Decode your message to key 3: "),3)) 
    print(encryptRailFence(input("Encode your message to key 4: "),4)) 
    print(decryptRailFence(input("Decode your message to key 4: "),4)) 
    print(encryptRailFence(input("Encode your message to key 5: "),5)) 
    print(decryptRailFence(input("Decode your message to key 5: "),5))
    print(encryptRailFence(input("Encode your message to key 6: "),6)) 
    print(decryptRailFence(input("Decode your message to key 6: "),6)) 
    print(encryptRailFence(input("Encode your message to key 7: "),7)) 
    print(decryptRailFence(input("Decode your message to key 7: "),7)) 
# In[ ]:




