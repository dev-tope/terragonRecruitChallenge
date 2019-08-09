# terragonRecruitChallenge

Snack 2:
This is a python program that takes a string and encrypts it using Caesar Cipher.

The tool starts by asking for an Input string, then it converts the input string to lowercase to eliminate complications that might arise with conflicting ASCII codes as upper-case and lower-case of same letters do not have the same ASCII codes.

Then an initial shift value of 0 is assigned to the tool.

The second block is a defence against brute force. The for loop changes the shift value based on the nature of the ASCII equivalent of the character in the given string. So, characters that have an even ASCII number have a diffrent value from values with odd ASCII characters.

The third block simply loops over the characters in a string, checks if the character is an alphabet (according to caesar cipher) then adds and subtract 97(the ASCII code for "a") then mods by 26 (the total nuber of alphabets + 1 ) this is to prevent the inclusion of non-alphabet characters in the cipher text and to keep the cipher text within the lower-case alphabet range.

