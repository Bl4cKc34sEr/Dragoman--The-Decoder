#!/usr/bin/env python
# coding: utf-8


# In[ ]:



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
                   " $$:    "))
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


# In[ ]:




