# day 01 - 07 was kinda the same thing all over again so i dropped and skipped day 06 and 07
# wanted to do something that i had fun with in uni and in school - analysis
# so i decided to change the challenges that i was about to do
# do something fun instead of forcing myself because i feel like i could really like programming
# if i use and learn it through something i liked

import matplotlib.pyplot as plt
import numpy as np


while(1):
    while(1):
        try:
            starting_point = float(input("What is your starting point?"))
            break
        except ValueError:
            print("Not acceptable start number!")

    while(1):
        try:
            ending_point = float(input("What is your ending point?"))
            break
        except ValueError:
            print("Not acceptable end number!")

    while(1):
        try:
            steps = int(input("How many steps do you want ploted?(No floats accepted."))
            break
        except ValueError:
            print("Not acceptable step number!")

    x = np.linspace(starting_point, ending_point, steps)

    while(1):
        function = input("What function do you want ploted? (x, x², x³)?")
        if (function == "x"):
            y = x
            break
        elif function == "x²":
            y = x ** 2
            break
        elif function == "x³":
            y = x**3
            break
        else:
            print("Function can't be ploted! Choose one of the three options (x, x², x³)")

    coordinates = list(zip(x,y))
    column_names = ['x','f(x)']

    fig, (ax1,ax2) = plt.subplots(2,1,figsize=(6,6))   #creates a figure and axes

    ax1.plot(x, y)
    ax2.axis("off")
    table = ax2.table(cellText=coordinates, colLabels=column_names, loc="center")

    plt.show()
    print(coordinates[0])
    print(coordinates[0][0])
    print(coordinates[0][1])
