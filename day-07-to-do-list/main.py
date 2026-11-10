import string
# Create a list to store tasks.
# Each task should contain its description and completion status.
# Display a menu with the following options:
#   1. Add task
#   2. Show tasks
#   3. Complete task
#   4. Delete task
#   5. Exit

# Allow the user to add new tasks.
# Display all tasks with their numbers and completion status.
# Allow the user to mark a task as completed using its number.
# Allow the user to delete a task using its number.
# Keep displaying the menu until the user chooses to exit.
# Handle invalid menu options and task numbers without crashing.
# Handle an empty task list.
# Prevent users from adding empty tasks.
tasks = []
task_details = []

while(1):
    print("Pick an option \n")
    options = ["1. Add task", "2. Show task", "3. Complete task", "4. Delete task", "5. Exit"]

    for x in options:
        print(x)

    while(1):
        try:
            new_task = int(input("What option do you choose? Please pick a number."))
            if new_task >=1 and new_task<=5:
                break
            else:
                print("Not a valid option!")
        except ValueError:
            print("Not a valid option!")

    if (new_task == 1 ):
        added_task = input("What is the task you wanna add?")
        index = 0
        for pos in tasks:
            index =+ 1

        #insert
        task_details.append(added_task)
        task_details.append("to be done")
        tasks.append(task_details)
        task_details = []

    elif new_task == 2:
        for a in tasks:
            print(','.join(a))

    #elif new_task == 3:

    #elif new_task == 4:

    else:
        break













