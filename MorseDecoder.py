#!/usr/bin/env python
# coding: utf-8

# In[6]:


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
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
   my_cipher = ''
   for myletter in message:
      if myletter != ' ':
         my_cipher += MORSE_CODE_DICT[myletter] + ' '
      else:
         my_cipher += ' '
      return my_cipher

def decryption(message):
   message += ' '
   decipher = ''
   mycitext = ''
   for myletter in message:
      if (myletter != ' '):
         i = 0
         mycitext += myletter
      else:
         i += 1
         if i == 2 :
            decipher += ' '
         else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
            .values()).index(mycitext)]
            mycitext = ''
   return decipher
def main():
   
   my_message = input()
   output = decryption(my_message)
   print (output)

if __name__ == '__main__':
   main()
