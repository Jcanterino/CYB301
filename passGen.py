#Based on rainbow tables a password with 14 characters with:
#numbers, upper/lower letters, and symbols will take 1 million years to crack
import random
import string
import sys

def passGen(rules):
    n = len(sys.argv)
    for i in range(1, n):
        if i == 1:
            rules.append(int(sys.argv[i]))
        elif i == 2:
            rules.append(int(sys.argv[i]))
        elif i == 3:
            rules.append(int(sys.argv[i]))
    #creating an array to be used when determining what character types to include
    exclusion = []
    for i in range (4, n):
        exclusion.append(str(sys.argv[i]))
    #using system arguments to create a list of exclusions

    pool = string.ascii_lowercase
    #password always contains lowercases
    if rules[0] == 1:
        pool += string.ascii_uppercase
    if rules[1] == 1:
        pool += string.digits
    if rules[2] == 1:
        pool += string.punctuation
    #using system inputs to decide what to include

    for i in range (0, n-4):
        for x in range (0, len(pool)):
            pool = pool.replace(exclusion[i], "")
    #removing the exclusions from the pool

    p = "" #initializing password
    for i in range(14):
        p += random.choice(pool) #choosing a random character from the pool of options to create a 14 character password
    print(p)
