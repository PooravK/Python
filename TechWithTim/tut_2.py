print("Hello what is your name? ")
name = input()
print("Welcome to 2nd tutorial ", name, ". Hope you enjoy it!", sep = "") # Did sep = "" so that there is nothing separating the 3 outputs

# Can also do that by string concatenation:
print("Welcome to the 2nd tutorial " + name + ". Hope you enjoy it!")

# Operators: + - / * 
# Advanced operators: ** (exponent) // (integer division - Gives quotient) % (Modulus - Gives remainder)

num1 = input()
num2 = input()
# input() always takes in as string, so if we wanted to input 2 numbers and add them,

Sum = int(num1) + int(num2) # Otherwise sum would just be a string concatenation of the 2 numbers

print(type(num2)) # Prints the type of num2