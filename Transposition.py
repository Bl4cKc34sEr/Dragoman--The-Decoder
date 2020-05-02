#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

def decrypt(message, keyword):
  matrix = new1(ordering(keyword), message)

  plaintext = "";
  for r in range(len(matrix)):
    for c in range (len(matrix[r])):
      plaintext += matrix[r][c]
  return plaintext


def new1(keySeq, message):
  width = len(keySeq)
  height = math.ceil(len(message) / width)
  if height * width < len(message):
    height += 1

  matrix = new2(width, height, len(message))

  pos = 0
  for num in range(len(keySeq)):
    column = keySeq.index(num+1)

    r = 0
    while (r < len(matrix)) and (len(matrix[r]) > column):
      matrix[r][column] = message[pos]
      r += 1
      pos += 1

  return matrix


def new2(width, height, length):
  matrix = []
  totalAdded = 0
  for r in range(height):
    matrix.append([])
    for c in range(width):
      if totalAdded >= length:
        return matrix
      matrix[r].append('')
      totalAdded += 1
  return matrix


def ordering(keyword):
  sequence = []
  for pos, ch in enumerate(keyword):
    previousLetters = keyword[:pos]
    newNumber = 1
    for previousPos, previousCh in enumerate(previousLetters):
      if previousCh > ch:
        sequence[previousPos] += 1
      else:
        newNumber += 1
    sequence.append(newNumber)
  return sequence

cipher = input("Enter Ciphertext :")
key = input("Enter the Key :")
dec = decrypt(cipher,key)
print(dec)


# In[ ]:




