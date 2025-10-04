# Python error handeling - Try and Except

text = input("Username: ") # Say I want my username to only be umbers no strings

# number = int(text)
# print(number) # This gives error cause you cant convert string into number, so in this case we use try and except block

try:
    number = int(text)
    print(number)
except:
    print("Invalid username") # Runs if try block fails instead of crashing the whole program