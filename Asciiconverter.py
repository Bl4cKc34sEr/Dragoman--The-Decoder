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

message = input("Enter ASCII codes: ") #Decoding ascii to text

decodedMessage = ""

for item in message.split():
    decodedMessage += chr(int(item))   

print ("Decoded Message: ", decodedMessage) 
message = input("Enter message to encode: ") #encoding text to ascii
for ch in message:
    print ("Decoded string (in ASCII):")
    print (ord(ch))
