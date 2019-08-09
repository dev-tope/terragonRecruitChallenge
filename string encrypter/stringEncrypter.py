plainText = input("What do you want to encrypt?")
plainText = plainText.lower()
cipherText = ""
shiftValue = 0


#To secure the cipher agains brute force, 
#characters of string should have different shift value,
#based on the nature (Even or Odd) of their ASCII codes
for character in plainText:
    if ord(character) % 2 == 0:
        shiftValue = 3
    else:
        shiftValue = 5

#Loop over characters while checking if the character is an alphabet
for character in plainText:
    if character.isalpha() is True:
        i = ord(character) - 97
        i += shiftValue
        i = i % 26
        cipherText += chr(i + 97)
    else:
        cipherText += character

print(cipherText)
