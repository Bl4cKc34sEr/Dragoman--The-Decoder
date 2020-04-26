#!/usr/bin/env python
# coding: utf-8

# In[6]:


MORSE_CODE = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}
def encryption(message):
   cipher_text = ''
   for mymessage in message:
      if mymessage != ' ':
         cipher_text += MORSE_CODE[mymessage] + ' '
      else:
         cipher_text += ' '
      return cipher_text

def decryption(message):
   message += ' '
   decipher = ''
   mycitext = ''
   for mymessage in message:
      if (mymessage != ' '):
         i = 0
         mycitext += mymessage
      else:
         i += 1
         if i == 2 :
            decipher += ' '
         else:
            decipher += list(MORSE_CODE.keys())[list(MORSE_CODE
            .values()).index(mycitext)]
            mycitext = ''
   return decipher
def main():
   
   my_message = input()
   output = decryption(my_message)
   print (output)

if __name__ == '__main__':
   main()


# In[ ]:




