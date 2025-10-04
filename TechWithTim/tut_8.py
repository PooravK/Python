# Lists and Tuples

fruits = ['apple', 'pear', 12] # List is a collection of different data types. Every comma separates an item
print(fruits)

# To access an indivisual item in the list: pear

print(fruits[1]) # 1 is a indice of the item pear. It starts from 0 to n

# To update a list:

fruits.append("Banana") # Append means to add to the end of the list

print(fruits)

# Another way is to use slice operator: Insert

# To remove an item example 12

fruits.remove(12)
print(fruits)
# Or fruits.pop(index) - Removes last element if no index given
# Or del fruits[index]

# Tuples: Used for coordinates or to hold information

position = (300, -49, 12) # Paranthesis used instead of square brackets