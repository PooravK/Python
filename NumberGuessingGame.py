import random

random_num = random.randint(0, 100)
count = 0

while (True):
    user_input = input("Enter a number: ")
    try:
        inp = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer!")
        continue
    if (inp != random_num):
        count += 1
        if (inp > random_num):
            print("You guessed higher!")
        else:
            print("You guseed lower!")
    else:
        count += 1
        print("Correct! You guessed in", count, "turns.")
        break

# Project outcomes:
# Understood forever loops to run applications
# Understood modular programming
# Understood using try and except for error handeling