# DAY 5 - WORD COUNTER

import string
# Welcome the user to the Word Counter.
# Ask the user to enter a sentence or text.
# Count the total number of words.
# Count the total number of characters.
# Count the number of characters without spaces.
# Count how many sentences the text contains.
# Find the longest word in the text.
# Find the shortest word in the text.
# Display all results clearly.
# Handle empty inputs without crashing.
# Ignore punctuation when comparing word lengths.

# BONUS CHALLENGES
# Count how often each word appears.
# Find the most frequently used word.
# Make word counting case-insensitive.
# Allow the user to analyze another text.
# Calculate the average word length.
name= input("Hello User, what's your name?")
print(f"Welcome to the Word Counter {name}!")

while(1):
    input_user = input("Please enter a text you want me to count the words and characters of:")
    if(input_user == ""):
        print("Input can't be empty")
    else:
        break

word_count=1
character_count=0
characters_without_spaces=0
sentences_count=0

longest_word=""
shortest_word=""

for x in input_user:
    character_count += 1
    if x == " ":
        word_count +=1

print(f"The character count is {character_count}.")
print(f"The word count is {word_count}.")