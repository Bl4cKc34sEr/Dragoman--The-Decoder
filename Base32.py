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
                                             --Presented with <3 by Shivanshu Sharma

\u001b[35   ____                   _________  
 | __ )  __ _ ___  ___  |___ /___ \ 
 |  _ \ / _` / __|/ _ \   |_ \ __) |
 | |_) | (_| \__ \  __/  ___) / __/ 
 |____/ \__,_|___/\___| |____/_____|
                                    
\u001b[32;1m \u001b[0m    """
print(banner) 
menu=""" \u001b[33;1m
------------------------------------------
            LIST OF DECODERS             |
------------------------------------------
  [+] ASCII CONVERTER      -- Ascii.py   |
  [+] ATBASH DECODER       -- Atbash.py  |
  [+] CAESER DECODER       -- Caeser.py  |
  [+] BACON DECODER        -- Bacon.py   |
  [+] BASE32 DECODER       -- Base32.py  |
  [+] BASE64 DECODER       -- Base64.py  |
  [+] BASE85 DECODER       -- Base85.py  |
  [+] DNA DECODER          -- Dna.py     | 
  [+] MORSE DECODER        -- Morse.py   | 
  [+] NUMBER SYSTEM        -- Num.py     | 
        [!] BINARY TO TEXT               | 
        [!] HEX TO TEXT                  | 
        [!] OCTAL TO TEXT                |  
  [+] RAILFENCE DECODER    -- Rail.py    |
  [+] REVERSE CIPHER       -- Reverse.py |  
  [+] ROTn DECODER        -- Rot.py     | 
  [+] TRANSPOSITION CIPHER -- Trans.py   | 
  [+] VIGNERE DECODER      -- Vignere.py |
------------------------------------------s
\u001b[32;1m""" 
print(menu)


import base64
print("[!]Your Plain-Text will be dispalyed as b'Yourtext'")
print (base64.b32decode(input("Enter Base32 String: ")))


