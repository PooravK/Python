# How to read a text file

file = open("tut_13.txt", "r") # AnyName = open("File name", "Mode")

# r = Read
# w = Write

f = file.readlines()

print(f)

newlist = []
for line in f:
    newlist.append(line[:-1]) # Take all of line except the last charactor that is \n

print(newlist) # Main error is we removed the last letter of the last line

# Fix:
newlist = []
for line in f:
    if line[-1] == "\n":
        newlist.append(line[:-1])
    else:
        newlist.append(line)

print(newlist)

# Another way is to use the string method: Strip

newlist = []
for line in f:
    newlist.append(line.strip())
print(newlist)

file.close()