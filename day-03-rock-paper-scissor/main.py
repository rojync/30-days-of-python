# DAY 3 - ROCK, PAPER, SCISSORS
import random
import string

#Ask the player to choose rock, paper, or scissors.
#Make the computer randomly choose rock, paper, or scissors.
#Display the computer's choice.
#Compare the player's choice with the computer's choice.
#Apply the rules:
#    - Rock beats scissors.
#    - Scissors beats paper.
#    - Paper beats rock.
#    - Identical choices result in a draw.
#Display whether the player wins, loses, or draws.
#Keep track of the player's and computer's scores.
#After each round, display the current score.
#Ask the player whether they want to play again.
#If yes, start another round without resetting the score.
#If no, display the final score and end the program.
#Handle invalid inputs without crashing.
#Accept uppercase and lowercase inputs.

options = ['Rock', 'Paper', 'Scissor']
score = 0
choice = input("Rock, Paper, Scissor, SHOOT:")
choice = choice.capitalize()
#valid choice
for pos in options:
    if(choice != options):
        print("Invalid input")

#letting computer choose

comp_choice = random.choice(options)
print(comp_choice)

#comparison computer and player

if (choice == 'Rock' and