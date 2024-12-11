# CYB301
Cybersecurity tool development for CYB301(Cybersecurity Fundamentals)

My current plan is to make a password managing software.
My main fear with using password managers online is that the passwords are stored in a server and not locally.
By creating my own password manager all the passwords can be saved and encrypted locally instead.
I plan to program in python because it's a simple option for what I'm looking to do

The final product consists of 2 programs
In passGen.py you can input your preferred directory for poth your key and your password list.
It is recommended that you put your key on a secure device (ie: a thumbprint locked usb drive)
The program when run prompts you to choose if you are creating or retrieving a password

Creating:
  In the password creation prompt, it will ask about the types of ascii characters you would like included/excluded in your password.
  Upon inputting the exclusions it will generate a 14 character password based on the pool of options you gave to it
  The password will then be sent to the keyGen file to be encrypted using your generated key
  The encrypted password is then saved to the password.txt file alongside the keyword you assigned it
Retrieving:
  The password retrieval process prompts you to enter the keyword you assigned to your password then searches the password.txt file to grab the encrypted password
  The program then retrieves the key from the key.txt file and sends it to the  keyGen program to decrypt the password
  The decrypted password is then printed in the terminal
