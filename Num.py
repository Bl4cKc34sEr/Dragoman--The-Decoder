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

\u001b[35  
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


def toDecimal(con):
    declist = []
    charlist = []
    text = ''
    print(" [!!!!] Warning: Be sure to remove the last trailing space of your message.")
    numlist = list(map(str, input(" Enter the space separated %s Cipher Text: \n"
                                  " ====>> " %typ).split(" ")))
    if con != 10:
        for i in numlist:
            a = int(str(i),con)
            declist.append(a)
    else:
        declist = numlist
    for j in declist:
        dec = chr(int(j))
        charlist.append(dec)
    text = ''.join(charlist)
    print("\nDECODED TEXT: ", text)


choice = int(input(" Enter the number type to convert to text:\n"
                   " 2  --> Decode-Binary\n"
                   " 8  --> Decode-Octal\n"
                   " 10 --> Decode-Decimal\n"
                   " 16 --> Decode-Hex\n"
                   " Enter Choice: "))
if choice == 2:
    con = 2
    typ = "Binary"
elif choice == 8:
    con = 8
    typ = "Octal"
elif choice == 10:
    con = 10
    typ = "Decimal"
elif choice == 16:
    con = 16
    typ = "Hexadecimal"
else:
    print(">> INVALID CHOICE!")
toDecimal(con)
