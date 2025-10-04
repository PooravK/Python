#Loops in Python

#2: While loops

# while condition == true:
#     do this

loop = True
while (loop):
    name = input("Enter an item: ")
    if name == "Stop":
        loop = False
        break