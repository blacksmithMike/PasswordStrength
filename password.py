import math

# This program is used to test passwords input by the user and give the user the bit strength of the password

password = input("\n\nWhat password would you like to test? ")
alphabet = 0

# Lists to accumulate characters from the input password
special = []
numeral = []
uppercase = []
lowercase = []

# Look at each character and determine what kind of character it is
for x in password:
    # print(ord(x))
    if ord(x) in range(32, 48) or ord(x) in range(58, 65) or ord(x) in range(91, 97) or ord(x) in range(123, 127):
        # Special character
        special.append(x)
    if ord(x) in range(48, 58):
        # Numeral
        numeral.append(x)
    if ord(x) in range(65, 91):
        # Uppercase letters
        uppercase.append(x)
    if ord(x) in range(97, 123):
        # Lowercase letters
        lowercase.append(x)

# Alphabet starts at 0 and if any list has a length of 1 or more, alphabet is updated to include the number of characters in that type
alphabet = 0
if len(special) >= 1:
    alphabet += 33
if len(numeral) >= 1:    
    alphabet += 10
if len(uppercase) >= 1:    
    alphabet += 26
if len(lowercase) >= 1:
    alphabet += 26

# Bit strength formula n = length of alphabet and m = length of password
# strength = log base 2(n raised m)
n = alphabet
m = len(password)
bits = math.log2(n**m)

print("\nAlphabet length " + str(n))
print("Password length " + str(m))
print("Passwrod bit strength " + str(math.floor(bits)))
print("")