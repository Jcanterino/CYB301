from passGen import *

exclusion = []

result = str(input("Y: include uppercase (default)\nN: exclude uppercase:").strip().upper())
exclusion.append(result if result in ["Y", "N"] else "Y")
result = str(input("Y: include numbers (default)\nN: exclude numbers:").strip().upper())
exclusion.append(result if result in ["Y", "N"] else "Y")
result = str(input("Y: include symbols (default)\nN: exclude symbols:").strip().upper())
exclusion.append(result if result in ["Y", "N"] else "Y")

print(exclusion)
