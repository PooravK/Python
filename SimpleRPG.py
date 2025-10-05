player = { # Learnt new thing: List inside dictionaries
    "health": 100,
    "attack": 10,
    "inventory":[],
    "location":"start"
    }

world = { # Learnt new thing: Nested dictionaries
    "start":{
        "desc":"You are in a dark room",
        "exits":{
            "north":"hallway"   
            }
        },
    "hallway":{
        "desc":"You entered a hallway",
        "exits":{
            "south":"start"
            }
        }
    }

while (True):
    position = player["location"]
    description = world[position]["desc"] # Learnt new thing: Calling 2 values inside dictionary
    print(description)

    print("Where do you want to go?")

    for direc in world[position]["exits"]:
        print(direc)

    direction = input("Enter your choice: ").lower()

    if direction in world[position]["exits"]:
        player["location"] = world[position]["exits"][direction] # First bracket: dictionary of current room Second bracket: exits dictionary of that room Third bracket: gets the new destination
    else:
        print("Error! Enter a valid direction")
        continue
