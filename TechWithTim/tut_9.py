# For loops continued

fruits = ["apples", "bananas", "strawberries"]

for fruit in fruits:
    if (fruit == "apples"):
        print("Apples")
    else:
        print("Not apples")

# Another way was to iterate through each index by counting the range

# Or:

for x in range (len(fruits)):
    if fruits[x] == "apples":
        print("Apples")
    else:
        print("Not apples")