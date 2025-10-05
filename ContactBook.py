import json

# Adding comments for my own sanity

try: # Load previous laoded values
    with open("ContactList.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError: # For first run when file is not made yet
    contacts = {}

while(True):
    user_inp = input("\n ---------- CONTACT LIST ---------- \nWhat action do you want to perform?\n1 - Add item\n2 - Remove item\n3 - View full list\n4 - Search a name\n5 - Exit\nEnter from 1-5: ")
    try:
        final_input = int(user_inp)
    except ValueError: # In case the user inputs anything other than an integer
        print("\nError: Enter an integer!")
        continue
    
    if (final_input == 1):
        name = input("\nEnter a name: ")
        numb = input("Enter their contact: ")
        
        contacts[name.lower()] = numb # Lower so that no matter in what order the user types, lower or upper, the dictionary gives same value
        continue
    elif (final_input == 2):
        name = input("\nEnter a name: ")

        if name.lower() in contacts:
            del contacts[name.lower()] # In case the contact is not in dictionary
        else:
            print("\nContact not found!")
        continue
    elif (final_input == 3):
        print("\n")
        for name in contacts:
            numb = contacts[name]
            print(numb, name)
        continue
    elif (final_input == 4):
        name = input("\nEnter a name: ")

        if name.lower() in contacts: # In case the contact is not in dictionary
            print("\nContact:", contacts[name])
        else:
            print("Contact not found!")
        continue
    elif (final_input == 5):
        break
    else:
        print("Select from 1-5 only!") # So the user only puts inputs between 1-5
        continue

with open("ContactList.json", "w") as f: # To update the memory file with new list of dictionary
    json.dump(contacts, f)