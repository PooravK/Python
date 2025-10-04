# Conditional statements

# if condition == True:
#     do this

print("Enter your age")
age = input()

if (int(age) < 18):
    print("Not eligible to drink and drive")
elif (int(age) == 18):
    print("Get a drivers liscnence first")
else:
    print("ELigible to drink and drive")