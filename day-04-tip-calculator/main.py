
import string
import math

# DAY 4 - TIP CALCULATOR

# Welcome the user to the Tip Calculator.
# Ask the user to enter the total bill amount.
# Ask the user what percentage they want to tip (e.g. 10%, 15%, 20%).
# Calculate the tip amount based on the percentage.
# Calculate the total bill including the tip.
# Ask how many people are splitting the bill.
# Calculate how much each person needs to pay.
# Display the tip amount.
# Display the total bill including the tip.
# Display how much each person needs to pay.
# Round all monetary results to two decimal places.
# Handle invalid inputs without crashing.
# Do not accept negative bill amounts.
# Do not accept negative tip percentages.
# Do not allow zero or negative people when splitting the bill.
# Allow decimal numbers for the bill amount.
# Display all monetary values with the € symbol.

# BONUS CHALLENGES
# Allow the user to choose between a percentage tip and a fixed tip amount.
# Ask the user whether they want to calculate another bill.
# If yes, restart the calculator.
# If no, display a goodbye message and end the program.

print("Welcome to the Tip Calculator")

while(1):
    try:
        bill_amount = float(input("How much is the bill?"))
        if (bill_amount < 0):
            print("The amount is invalid")

        break
    except ValueError:
        print("Invalid input!")

#if (tip_percentage != )
#remove the percentage sign if there is one
#float(string[1:]
#float(string.replace("$", "")
tip_percentage= input("How much percentage do you wanna tip?")
while (1):
    try:
        tip_percentage = float(tip_percentage.replace("$", ""))*0.01
        if (tip_percentage < 0):
            print("Invalid input")

        break
    except ValueError:
        print("Invalid input")

tip_amount = float(bill_amount*tip_percentage)

while (1):
    try:
        number_people = int(input("How many people are paying the bill?"))
        if (number_people < 1):
            print("Invalid input")

        break
    except ValueError:
        print("Invalid input")

total_bill = bill_amount+tip_amount


#amount = str(total_bill) + "€" can also use this as the string
bill_per_person = total_bill/number_people
print(f"The total bill is: {total_bill}€")
print(tip_amount)
print(total_bill)
