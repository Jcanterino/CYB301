import random

def gen(file):
    key = ""
    for i in range (0, 14):
        key += str(random.randint(0, 9))
    with open(file, "w") as file:
        file.write(str(key))

def encrypt(password, key):
    ePassword = ""
    for i in range (0, 14):
        shift = ((ord(password[i]) + int(key[i]))%126)
        if shift < 32:
            shift += 31
        ePassword += chr(shift)
    return ePassword

def decrypt(password, key):
    dPassword = ""
    for i in range (0, 14):
        shift = ((ord(password[i]) - int(key[i]))%126)
        if shift < 32:
            shift += 95
        dPassword += chr(shift)
    return dPassword