#!/usr/bin/env python
# coding: utf-8

# In[ ]:


message = input("Enter ASCII codes: ") #Decoding ascii to text

decodedMessage = ""

for item in message.split():
    decodedMessage += chr(int(item))   

print ("Decoded Message: ", decodedMessage) 
message = input("Enter message to encode: ") #encoding text to ascii
for ch in message:
    print ("Decoded string (in ASCII):")
    print (ord(ch))

