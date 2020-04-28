#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

# Sets alphabet characters for comparison.

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", 
	"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Performs ROTation based on user input.
	
def rotCalc(userStr):
	output = ""
	for i in range(len(userStr)):
	
		# Handles whitespace.
	
		if userStr[i] == " ":
			output = output + " "
			
		# Handles digits - in default ROT encoding these do not rotate.
		
		elif userStr[i].isdigit():
			output = output + userStr[i]
			
		# Handles alphabetical characters.
		
		elif userStr[i].isalpha():
			for j in range(len(alphabet)):
			
				# Handles uppercase characters.
				
				if userStr[i].isupper():
					if userStr[i].lower() == alphabet[j]:
						if encOrDec == 1:
							if j + rotNum > 25:
									diff = (j + rotNum) - 25
									output = output + (alphabet[diff - 1].upper())
							else:
								output = output + (alphabet[j + rotNum].upper())
						elif encOrDec == 2:
							if j - rotNum < 0:
								diff = (j - rotNum) + 25
								output = output + (alphabet[diff + 1].upper())
							else:
								output = output + (alphabet[j - rotNum].upper())

				# Handles lowercase characters.
								
				elif userStr[i] == alphabet[j]:
					if encOrDec == 1:
						if j + rotNum > 25:
							diff = (j + rotNum) - 25
							output = output + (alphabet[diff - 1])
						else:
							output = output + (alphabet[j + rotNum])
					elif encOrDec == 2:
						if j - rotNum < 0:
							diff = (j - rotNum) + 25
							output = output + (alphabet[diff + 1])
						else:
							output = output + (alphabet[j - rotNum])
							
		# Handles anything else (special characters like !@#$, etc).
		
		else:
			output = output + userStr[i]
	return output	
	
# Main program loop requests encode/decode, ROTation number, and user string.  Then sends to rotCalc function.
# The main program implements input validation ensuring legal input from the user; quits on illegal input.
	
while True:
	encOrDec = input("Enter 1 to ENCODE, 2 to DECODE, OR anything else to quit: ")
	if encOrDec.isdigit() == False:
		print ("You Quit!!")
	
	else:
		encOrDec = int(encOrDec)
		if encOrDec == 1 or encOrDec == 2:
			rotNum = input("Enter numbers to ROT,1-25, OR anything else to quit: ")
			if rotNum.isdigit() == False:
                print ("You Quit!!")
            else:
				rotNum = int(rotNum)
				if rotNum >= 1 and rotNum < 26:
					userStr = input("Enter your message: ")
                    if encOrDec == 1:
						print (userStr, ("ROT-" + str(rotNum)), "encoded:", rotCalc(userStr))
					elif encOrDec == 2:
						print (userStr, ("ROT-" + str(rotNum)), "decoded:", rotCalc(userStr))
                else:
                     print ("Got your Flag!!")
                    sys.exit()
        else:
            print ("Got your Flag!!")
            sys.exit()


# In[ ]:





# In[ ]:




