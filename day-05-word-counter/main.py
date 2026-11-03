# DAY 5 - WORD COUNTER

import string
# Welcome the user to the Word Counter. //
# Ask the user to enter a sentence or text. //
# Count the total number of words. //
# Count the total number of characters. //
# Count the number of characters without spaces. //
# Count how many sentences the text contains. //
# Find the longest word in the text.
# Find the shortest word in the text.
# Display all results clearly. //
# Handle empty inputs without crashing. //
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
characters_without_spaces=0
sentences_count=1

length_input = len(input_user)
y=0

longest_word=""
temp_longest_word = ""
longest_words=[]

shortest_word=""
temp_shortest_word = ""
shortest_words=[]

for x in input_user:
    y+=1
    characters_without_spaces += 1
    temp_longest_word = temp_longest_word + x
    temp_shortest_word = temp_shortest_word + x

    if x == " ":
        word_count +=1
        characters_without_spaces -= 1
        temp_longest_word = temp_longest_word.replace(" ", "")
        temp_shortest_word = temp_shortest_word.replace(" ", "")

        if shortest_word == "":
            shortest_word = temp_shortest_word

        if len(temp_longest_word)>len(longest_word):
            longest_word = temp_longest_word
            temp_longest_word = ""
        elif len(temp_longest_word) == len(longest_word):
            longest_words.append(temp_longest_word)
            longest_words.append(longest_word)
            temp_longest_word=""
        else:
            temp_longest_word = ""

        if len(temp_shortest_word)<len(shortest_word):
            shortest_word = temp_shortest_word
            temp_shortest_word = ""
        elif len(temp_shortest_word) == len(shortest_word):
            shortest_words.append(temp_shortest_word)
            shortest_words.append(shortest_word)
            temp_shortest_word = ""
        else:
            temp_shortest_word= ""

    if x == ".":
        sentences_count += 1
        longest_word = longest_word.replace(".","")

longest_word = temp_longest_word
shortest_word = temp_shortest_word


# counts space as words different approach
for y in reversed(input_user):
    if y != " ":
        break
    elif y==" ":
        word_count -= 1

print(f"The character count is {length_input}.")
print(f"The word count is {word_count}.")
print(f"The characters without space in between count is {characters_without_spaces}.")
print(f"The sentence count is {sentences_count}.")

longest_words = list(set(longest_words))
if longest_words!=[]:
    print("The longest words are:", " ".join(longest_words), ".")
else:
    print(f"The longest word is: {longest_word}.")

shortest_words = list(set(shortest_words))
if shortest_words!=[]:
    print("The shortest words are:", " ".join(shortest_words), ".")
elif shortest_words == [] or len(shortest_words)==1:
    print("The shortest word is:", " ".join(shortest_words), ".")
