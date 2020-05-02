#!/usr/bin/env python
# coding: utf-8

# In[12]:


alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Initiates either the encoding function or the decoding function.
def atbashPrompt():
    codeChoice = "d"
    if codeChoice == "d":
        print(decodeAtbash(str(input("Decode: "))))
    elif codeChoice == "e":
        print(encodeAtbash(str(input())))

#Atbash encoding function.
def encodeAtbash(sentence):
    word = ""
    for i in sentence:
        encodeIndex = 25 - alphabet.index(i)
        word += alphabet[encodeIndex]
    return word

#Atbash decoding function.
def decodeAtbash(code):
    solution = ''
    for l in code:
        solution += alphabet[25-alphabet.index(l)]
    return solution

atbashPrompt()


# In[8]:





# In[ ]:




