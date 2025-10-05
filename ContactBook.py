contacts = {}

while(True):
    user_inp = input("\n ---------- CONTACT LIST ---------- \nWhat action do you want to perform?\n1 - Add item\n2 - Remove item\n3 - View full list\n4 - Search a name\n5 - Exit\nEnter from 1-4: ")
    try:
        final_input = int(user_inp)
    except ValueError:
        print("\nError: Enter an integer!")
        continue
    
    if (final_input == 1):
        name = input("\nEnter a name: ")
        numb = input("Enter their contact: ")
        
        contacts[name.lower()] = numb
        continue
    elif (final_input == 2):
        name = input("\nEnter a name: ")

        del contacts[name.lower()]
        continue
    elif (final_input == 3):
        print("\n")
        for name in contacts:
            numb = contacts[name]
            print(numb, name)
        continue
    elif (final_input == 4):
        name = input("\nEnter a name: ")

        print("\nContact:", contacts[name])
        continue
    elif (final_input == 5):
        break
    else:
        print("Select from 1-5 only!")
        continue