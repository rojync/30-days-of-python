import string
import random

print ("Day 1 of my 30 days challenge \n")

# password length choosable  -> input of length
# lowercase uppercase differentiation
# numbers and signs
# check input
# use secrets

length = int(input("Enter the length of the password: "))

if length.type != int:
    print("Password length must be a number between 8 and 25 ")
    length = int(input("Request a valid number for the password: "))

if length >25 or length < 8:
    print("Password length must be less than 25")
    length = int(input("Request a valid length for the password: "))

password = ""

# length not too long check

password = ""
# for loop ads the randomly chosen sign to the string
# throwing everything together and letting function random pick (wasn´t intentional idea)

signs_available = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
for i in range(length):
    password = password + random.choice(signs_available)
# add - between 4 signs
print(password)



