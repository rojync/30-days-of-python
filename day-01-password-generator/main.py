import string
import random

print ("Day 1 of my 30 days challenge \n")

# password length choosable  -> input of length
# lowercase uppercase differentiation
# numbers and signs
# check input
# use secrets


quest = input("Enter the length of the password: ")

if quest.isdigit():
    length = int(quest)
else:
    print("Invalid input")
    length = int(input("Enter a valid length for the password: "))


if type(length) != int:
    print("Password length must be a number between 8 and 25 ")
    length = int(input("Request a valid number for the password: "))

if length >25 or length < 8:
    print("Password length must be between 8 and 25 ")
    length = int(input("Request a valid length for the password: "))

password = ""

# length not too long check
# for loop ads the randomly chosen sign to the string
# throwing everything together and letting function random pick (wasn´t intentional idea)

signs_available = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
for i in range(length):
    password = password + random.choice(signs_available)
# add - between 4 signs
print(password)



