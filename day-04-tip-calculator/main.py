
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
bill_amount = float(input("How much is the bill?"))
tip_percentage= input("How much percentage do you wanna tip?")

#if (tip_percentage != )
#remove the percentage sign if there is one
#float(string[1:]
#float(string.replace("$", "")
tip_percentage = float(tip_percentage.replace("$", ""))*0.01

tip_amount = float(bill_amount*tip_percentage)
total_bill = bill_amount+tip_amount
print(bill_amount)
print(tip_amount)
print(total_bill)
