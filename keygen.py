from random import randint
keygen = ""
for i in range(9):
    keygen += chr(randint(112, 125))
print(keygen)
