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
                \u001b[32;1m
\u001b[35;1m                 ___   _ _                  __       
        / _ | ___ ____(_|_) / _ \___ _______  ___/ /__ ____
       / __ |(_-</ __/ / / / // / -_) __/ _ \/ _  / -_) __/
      /_/ |_/___/\__/_/_/ /____/\__/\__/\___/\_,_/\__/_/  

                              \u001b[32;1m --Presented with <3 by Shivanshu Sharma\u001b[0m 
    """
print(banner) 
menu=""" \u001b[33;1m
----------------------------------------
            OTHER DECODERS             |
----------------------------------------
  [+] CEASER DECODER     -- Ceaser.py  |
  [+] BACON DECODER      -- Bacon.py   |
  [+] BASE64 DECODER     -- Base64.py  |
  [+] DNA DECODER        -- Dna.py     | 
  [+] MORSE DECODER      -- Morse.py   | 
  [+] NUMBER SYSTEM      -- Num.py     | 
        [!] BINARY TO TEXT             | 
        [!] HEX TO TEXT                | 
        [!] OCTAL TO TEXT              |  
  [+] RAILFENCE DECODER  -- Rail.py    |  
  [+] ROT13 DECODER      -- Rot.py     | 
  [+] VIGNERE DECODER    -- Vignere.py |
---------------------------------------
\u001b[32;1m""" 
print(menu)

message = input("Enter ASCII codes: ") #Decoding ascii to text

decodedMessage = ""

for item in message.split():
    decodedMessage += chr(int(item))   

print ("Decoded Message: ", decodedMessage) 
message = input("Enter message to encode: ") #encoding text to ascii
for ch in message:
    print ("Decoded string (in ASCII):")
    print (ord(ch))

