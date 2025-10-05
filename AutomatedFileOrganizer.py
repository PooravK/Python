import os

# Path to the folder I wanna organise
folder_path = "C:\\Users\\poora\\Desktop\\APKs" # Because single \ is a special esscape charactor in python
# or can also do folder_path = r"C:\Users\poora\Desktop\APKs"

# Look inside and return a list of all items
items = os.listdir(folder_path)

# Go through each item name one by one
for item_name in items:

    # Unlike os.listdir() which only returns item names, this returns the complete path to those items and combines it with item name
    full_path = os.path.join(folder_path, item_name) # Created full pat by joining folder path and item name

    # Checks if the full path leads to a folder or a file
    if os.path.isfile(full_path):
        print(item_name, "is a file")
    else:
        print(item_name, "is a folder")