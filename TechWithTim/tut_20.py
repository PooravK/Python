# Objects and Classes

# Any variable we create is an object

x = "string"
y = 23 # y is an object of class integer

# Objects have certain attributes - Example we cant use .count() method on y because its an integer

class number():
    def __init__(self, num): # Initialization statement, automatically done
        self.var = num # Sets variable inside of a class as 23
    

    def display(self, x):
        print(x)

# Example:

num = number(23)
print(num) # Shows the location of object in the memory

num.display(num.var)