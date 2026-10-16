import random #use random when needed random
import string
#Guess the Number betweeen 0 and 500
#Programm picks a number
#you guess the number
#tells you higher or lower
#counts attempts

number = random.randint(0,500)
attempt_count = 0
guess = input("Guess a number between 0 and 500:")

def turning_guess_int(guess):
    while type(guess)!=int:
        if guess.isdigit():
            guess = int(guess)
            return guess
        else:
            print("Invalid guess")
            guess = input("Guess a number between 0 and 500:")

#asks if guess is digit if not then invalid guess asks again and checks again if
# guess is digit until guess is int

#if i ask to pick again the check if its a digit will not be done
while (guess != number):
    guess = turning_guess_int(guess)
    if guess == number:
        print("You are correct")
        print("Total attempts:" + str(attempt_count))
        sys.exit()
    elif guess > number:
        print("Too high")
        guess = input("Next guess:")
        attempt_count =+ 1
    else:
        print("Too low")
        guess = input("Next guess:")
        attempt_count =+ 1



