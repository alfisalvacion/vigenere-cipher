# James Alfon M. Salvacion
# University of the Philippines Cebu

# ADDITIONAL INFO ABOUT SPACES
# The space ' ' isn't included in the alphabet
# Strings with spaces ' ' in them will be filtered off of spaces first

def encrypt(text, key):
	# returns the encrypted text based on original text and key

	e = "" # accumulated encrypted string
	i = 0  # start index for keystring

	for ch in text:
		e += encryptChar(ch, key[i])	# e accumulates every encrypted character
		if i == len(key) - 1: 				# if ever key is shorter than text: 
			i = 0												# then index of the key should reset if it reaches
		else:													# the length of the key - 1
			i += 1
	return e

def encryptChar(textChar, keyChar):
	# E = val(textchar) + val(keychar), where E is the new character
	# ord is a function that returns the ASCII int of a given character
	# chr is a function that returns the character of a given ASCII int

	textVal = (ord(textChar) - ord('A'))	
	keyVal = (ord(keyChar) - ord('A'))

	newVal = ord('A') + textVal + keyVal

	if newVal > ord('Z'):							# if the new value exceeds the ascii of the last character, Z
		textVal -= 26										# the textVal should be -26 because the ASCII values will not be the same

	return chr(ord('A') + textVal + keyVal)	

def decrypt(encrypted, key):
	# returns the encrypted text based on original text and key

	e = "" # accumulated encrypted string
	i = 0  # start index for keystring

	for ch in encrypted:
		e += decryptChar(ch, key[i])	# e accumulates every encrypted character
		if i == len(key) - 1: 				# if ever key is shorter than text: 
			i = 0												# then index of the key should reset if it reaches
		else:													# the length of the key - 1
			i += 1
	return e

def decryptChar(encryptedChar, keyChar):
	# D = val(E) - val(keychar), where E is the encrypted character and D is the decrypted char
	# ord is a function that returns the ASCII int of a given character
	# chr is a function that returns the character of a given ASCII int

	encryptedVal = (ord(encryptedChar) - ord('A'))	
	keyVal = (ord(keyChar) - ord('A'))

	newVal = ord('A') + encryptedVal - keyVal

	if newVal < ord('A'):							# if the new value is less than the ascii of the first character, A
		encryptedVal += 26							# the textVal should be -26 because the ASCII values will not be the same

	return chr(ord('A') + encryptedVal - keyVal)	

def main():
	choice = 1
	while(choice != 1 or choice != 2):
		print "\n<------------------------------ Vigenere Cipher ------------------------------>"
		print "This program decrypts and encrypts a string using the Vigenere Cipher.\nWhat do you want to do?"
		print "[1] ENCRYPT    [2] DECRYPT"
		choice = raw_input()

		if choice == "1":
			print "\nVIGENERE ENCRYPTION\nEnter the string(ALL CAPS ONLY): "
			eText = raw_input()
			print "Enter the key: "
			kText = raw_input()
			encText = encrypt(eText.replace(' ', ''), kText)
			print "\nEncrypt: " + eText + " with key: " + kText
			print "Encrypted string: " + encText

		elif choice == "2":
			print "\nVIGENERE DECRYPTION\nEnter the string(ALL CAPS ONLY): "
			eText = raw_input()
			print "Enter the key: "
			kText = raw_input()
			decText = decrypt(eText.replace(' ', ''), kText)
			print "\nDecrypt: " + eText + " with key: " + kText
			print "Decrypted string: " + decText

		else:
			print "Please choose between 1 and 2 only.\n"

main()