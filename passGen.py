import string
import random
import os
import re
import keyGen

def find_codes(file_path, keyword):
    pattern = re.compile(rf"{re.escape(keyword)}:\s([ -~]{{14}})")
    
    codes = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    codes.append(match.group(1))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    return codes

def passGen(rules):
    n = len(rules)
    pool = string.ascii_lowercase
    #password always contains lowercases
    if rules[0] == 'Y':
        pool += string.ascii_uppercase
    if rules[1] == 'Y':
        pool += string.digits
    if rules[2] == 'Y':
        pool += string.punctuation
    #using system inputs to decide what to include

    for i in range (3, n):
        for x in range (0, len(pool)):
            pool = pool.replace(rules[i], "")
    #removing the exclusions from the pool

    p = "" #initializing password
    for i in range(14):
        p += random.choice(pool) #choosing a random character from the pool of options to create a 14 character password
    print("Password: "+p)
    return p

def passCreate(keyP, passP):
    keyword = input("Please enter a keyword for the password: ")
    exclusion = []

    result = str(input("Y: include uppercase (default)\nN: exclude uppercase:").strip().upper())
    exclusion.append(result if result in ["Y", "N"] else "Y")
    result = str(input("Y: include numbers (default)\nN: exclude numbers:").strip().upper())
    exclusion.append(result if result in ["Y", "N"] else "Y")
    result = str(input("Y: include symbols (default)\nN: exclude symbols:").strip().upper())
    exclusion.append(result if result in ["Y", "N"] else "Y")
    while True:
        result = str(input("Exclude (input individually, press enter to continue: )"))
        if (result == ""):
            break
        else:
            exclusion.append(result)

    try:
        with open(keyP, "r") as file:
            key = file.read()
    except:
        keyGen.gen(keyP)
        with open(keyP, "r") as file:
            key = file.read()

    password = passGen(exclusion)
    ePassword = keyGen.encrypt(password, key)
    with open(passP, "a", encoding="utf-8") as file:
            file.write("\n"+keyword+": "+ePassword)

def passRetrieve(keyP, passP):
    keyword = input("Enter keyword: ")
    try:
        with open(keyP, "r") as file:
            key = file.read()
    except:
        print("No such key exists")
    ePassword = str(find_codes(passP, keyword))
    ePassword = ePassword[2:-2]
    print(ePassword)
    print(keyGen.decrypt(ePassword, key))

keyDir = r"C:\test"
passDir = r"C:\test"
#specify the location of your key and passwords
#if you have not created a key/password file input where you would like the key/password to be created
os.makedirs(keyDir, exist_ok=True)
os.makedirs(passDir, exist_ok=True)
keyPath = os.path.join(keyDir, "key.txt")
passPath = os.path.join(passDir, "passwords.txt")

while True:
    choice = int(input("Generate password(1):\nRetrieve password(2): "))
    if(choice == 1):
        passCreate(keyPath, passPath)
        break
    elif(choice == 2):
        passRetrieve(keyPath, passPath)
        break





