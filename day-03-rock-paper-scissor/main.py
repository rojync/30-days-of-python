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

options = ['Rock', 'Paper','Scissor']
score = 0
comp_score = 0
choice = input("Rock, Paper, Scissor, SHOOT:")
choice = choice.capitalize()

#valid choice
for x in range(2):
    y = options[x]
    if(choice != y):
        print("Invalid input")
        choice = input("Rock, Paper, Scissor, SHOOT:")
        choice = choice.capitalize()
    else:
        break
#letting computer choose

comp_choice = random.choice(options)
print(comp_choice)

def output(score,comp_score):
    x = str(score) + ":" + str(comp_score)
    return x

# all cases or is there a more efficient way?
while score<= 3 or comp_score <= 3:
    if choice==comp_choice:
        print("Draw! " + str(score) + ":" + str(comp_score))
    elif choice=='Rock' and comp_choice=='Paper':
        comp_score = comp_score + 1
        print(output(score, comp_score))
    elif choice=='Paper' and comp_choice=='Rock':
        score = score + 1
        print(output(score, comp_score))
    elif choice=='Rock' and comp_choice=='Scissor':
        score = score + 1
        print(output(score, comp_score))
    elif choice=='Scissor' and comp_choice=='Rock':
        comp_score = comp_score + 1
        print(output(score, comp_score))
    elif choice=='Paper' and comp_choice=='Scissor':
        comp_choice = comp_choice + 1
        print(output(score, comp_score))
    else:
        score = score + 1
        print(output(score, comp_score))


#comparison computer and player
