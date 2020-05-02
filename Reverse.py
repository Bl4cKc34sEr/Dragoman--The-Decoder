#!/usr/bin/env python
# coding: utf-8

# In[ ]:


message = input("Enter Text to Reverse: ")
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)


# In[ ]:




