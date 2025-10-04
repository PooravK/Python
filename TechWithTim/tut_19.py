# Global v/s Local variables

var1 = 9
loop = True

def func1(x):
    var2 = 7
    global loop
    loop = 7

    if (x == 5):
        return var2

# print(var2) # Gives var2 is not defined as error: This is because var2 was declared as a local variable to func1, only func1 can access var2
print(var1) # This works because var1 was declared as a global variable
print(loop)

# global keyword allows the variable to take its global value