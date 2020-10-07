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

\u001b[35 █▀▄ █▄░█ ▄▀█   █▀▄ █▀▀ █▀▀ █▀█ █▀▄ █▀▀ █▀█
█▄▀ █░▀█ █▀█   █▄▀ ██▄ █▄▄ █▄█ █▄▀ ██▄ █▀▄
                                       
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
  [+] ROTn DECODER        -- Rot.py      | 
  [+] TRANSPOSITION CIPHER -- Trans.py   | 
  [+] VIGNERE DECODER      -- Vignere.py |
------------------------------------------s
\u001b[32;1m""" 
print(menu)


mapping = {
        
'AAA':'a',
'AAC':'b',
'AAG':'c',
'AAT':'d',
'ACA':'e',
'ACC':'f', 
'ACG':'g',
'ACT':'h',
'AGA':'i',
'AGC':'j',
'AGG':'k',
'AGT':'l',
'ATA':'m',
'ATC':'n',
'ATG':'o',
'ATT':'p',
'CAA':'q',
'CAC':'r',
'CAG':'s',
'CAT':'t',
'CCA':'u',
'CCC':'v',
'CCG':'w',
'CCT':'x',
'CGA':'y',
'CGC':'z',
'CGG':'A',
'CGT':'B',
'CTA':'C',
'CTC':'D',
'CTG':'E',
'CTT':'F',
'GAA':'G',
'GAC':'H',
'GAG':'I',
'GAT':'J',
'GCA':'K',
'GCC':'L',
'GCG':'M',
'GCT':'N',
'GGA':'O',
'GGC':'P',
'GGG':'Q',
'GGT':'R',
'GTA':'S',
'GTC':'T',
'GTG':'U',
'GTT':'V',
'TAA':'W',
'TAC':'X',
'TAG':'Y',
'TAT':'Z',
'TCA':'1',
'TCC':'2',
'TCG':'3',
'TCT':'4',
'TGA':'5',
'TGC':'6',
'TGG':'7',
'TGT':'8',
'TTA':'9',
'TTC':'0',
'TTG':' ',
'TTT':'.'

    
    
}





string = input("Enter DNA string: ")
def decode_dna( string ):

    pieces = []
    for i in range( 0, len(string), 3 ):
        piece =  string[i:i+3]
        # pieces.append()
        pieces.append( mapping[piece] )

    return "".join(pieces)
   
print (decode_dna(string))

