# .find() and .count() method

string = "Hello"

print(string.find("e"))
print(string.find("a")) # Returns -1 if not found any matches - Can be used in passwords when we are not allowing or NEED a specific charactor in the string

# Cound does the same thing but instead of finding the index it counts how many of those characters are in the strings

print(string.count("l"))
z = "ajauhiuhigigjawaw"

print(z.count("w"))
print(z.count("z"))

# Say I dont want to allow any _ in my password

string = input("Enter a password:")
if string.count("_") > 0:
    print("Invalid password!")
else:
    print("Accepted")