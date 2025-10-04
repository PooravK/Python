# Chained conditionals and nested statements

# and: Both statements true
# or: Atleast one of the statements is true
# not: Returns False is statement is True

print(2 < 3 and 3 < 4)
print(3 < 4 or 4 > 5)
print(not(1 < 2))

print("Enter your age:")
age = input()

if (int(age) <= 100):
    if (int(age) < 18):
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("Invalid age")