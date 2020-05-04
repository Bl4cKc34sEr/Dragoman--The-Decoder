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

\u001b[35  __      __ __        __  __ __ __  __  __ __  
|__) /\ /  /  \|\ |  |  \|_ /  /  \|  \|_ |__) 
|__)/--\\__\__/| \|  |__/|__\__\__/|__/|__| \  
                                                                      
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
  [+] ROTn DECODER         -- Rot.py     | 
  [+] TRANSPOSITION CIPHER -- Trans.py   | 
  [+] VIGNERE DECODER      -- Vignere.py |
------------------------------------------s
\u001b[32;1m""" 
print(menu)


lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaaa', 
        'K':'abaab', 'L':'ababa', 'M':'ababb', 'N':'abbaa', 'O':'abbab', 
        'P':'abbba', 'Q':'abbbb', 'R':'baaaa', 'S':'baaab', 'T':'baaba', 
        'U':'baabb', 'V':'baabb', 'W':'babaa', 'X':'babab', 'Y':'babba', 'Z':'babbb'} 

def decrypt(message): 
    decipher = '' 
    i = 0


    while True : 

        if(i < len(message)-4): 

            substr = message[i:i + 5] 

            if(substr[0] != ' '): 
            
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)] 
                i += 5 
            else:
                decipher += ' '
                i += 1  
        else: 
            break 

    return decipher 

def main(): 
    

    message = input("Enter Your Cipher Text: " )
    result = decrypt(message.lower()) 
    print (result) 

if __name__ == '__main__': 
    main() 
