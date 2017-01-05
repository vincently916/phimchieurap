import random
import string
passwd_len = int(raw_input("Enter the lenght of the password: "))

symbols = "~!@#$%^&*()_|<>?=+-"
char = string.uppercase + string.lowercase +  symbols + string.digits
password = " "
counter = 0
while counter < passwd_len:
 temp = random.choice(char)
 password = password + temp 
 counter +=1

print password 
