'''
Rules of the game
Snake beats Water (Snake drinks Water).
Water beats Gun (Water rusts Gun).
Gun beats Snake (Gun shoots Snake).
'''

import random

'''
1 for snake
-1 for water
0 for gun
'''

# Computer randomly chooses between snake, water, and gun
computer = random.choice([1, -1, 0])

# User input for choice
your_choice = input("Enter your choice (s for snake, w for water, g for gun): ")

# Dictionary to map user input to game choices
you_Dict = {"s": 1, "w": -1, "g": 0}

# Dictionary to map game choices to their corresponding strings
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get the user's choice based on input
you = you_Dict[your_choice]

# Print choices made by user and computer
print(f"You chose: {reverse_dict[you]}\nComputer chose: {reverse_dict[computer]}")

# Check if it's a draw
if computer == you:  # when computer and user both choose the same
    print("It's a draw")
else:
    # Determine the outcome based on the rules of the game
    if computer == 1 and you == -1:
        print("You lose!")
    elif computer == -1 and you == 1:
        print("You won!")
    elif computer == 0 and you == 1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You won!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == 0 and you == -1:
        print("You won!")
    else:
        print("Something went wrong")
