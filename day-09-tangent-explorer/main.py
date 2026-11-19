import matplotlib.pyplot as plt
import numpy as np


def gradient(x_cor, user_input):
    while x_cor < user_input:
        x_cor = + 0.001

    return

while(1):

    x = np.linspace(-50,50,100)

    while(1):
        try:
            x0_point = float(input("Which x coordinate you want to know the gradient of?"))
            if((x0_point>=50) and (x0_point<=-50)):
                print("Not acceptable Value")
            else:
                break
        except ValueError:
            print("Not acceptable input!")

    gradient(x,x0_point)


    fig, (ax1,ax2) = plt.subplots()

    plt.show()


