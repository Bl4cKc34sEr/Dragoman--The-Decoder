import detectEnglish,vigenereCipher,pyperclip

def main():
	ciphertext = "CNVUT"
 	hackedMessage =hackVigenere(ciphertext)

	if hackedMessage !=None:
		print 'Copying hacked message to clipboard:'
		print(hackedMessage)
		pyperclip.copy(hackedMessage)
	else:
	    print 'Failed to hack'


def hackVigenere(ciphertext):
	fo=open('dictionary.txt')
	words=fo.readlines()
	fo.close()

	for word in words:
		word=word.strip()
		decryptedText=vigenereCipher.decryptMessage(word,ciphertext)


		if detectEnglish.isEnglish(decryptedText,wordPercentage=40):
			#print()
			#print 'Possible encryption break:'
			#print 'Key' , str(word) , ':' , decryptedText[:100]
			vigenereCipher.main(str(word))
			#print 'Enter D for done'
			#response = raw_input('')

			#if response.upper().startswith('D'):
			#	return decryptedText


if __name__ == '__main__':
    main()
