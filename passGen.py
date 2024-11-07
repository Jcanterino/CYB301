#Based on rainbow tables a password with 14 characters with:
#numbers, upper/lower letters, and symbols will take 1 million years to crack
import random
import string
import sys

p = ""

n = len(sys.argv)
for i in range(1, n):
    if i == 1:
        a = int(sys.argv[i])
    elif i == 2:
        b = int(sys.argv[i])
    elif i == 3:
        c = int(sys.argv[i])
# a, b, c = (int(arg) if i < len(sys.argv) else 1 for i, arg in enumerate(sys.argv[1:], start=1))

pool = string.ascii_lowercase

if a == 1:
    pool += string.ascii_uppercase
if b == 1:
    pool += string.digits
if c == 1:
    pool += string.punctuation

for i in range(14):
    p += random.choice(pool)
print(p)