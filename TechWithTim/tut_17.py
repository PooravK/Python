# Optional parameters

def func(x, text = "2"):
    print(x)
    if (text == "1"):
        print("Text is 1")
    else:
        print("Text is not 1")

func("Hello", "1")
func("Hello")

def func2(x, text = "2"):
    print(x)
    if (text == "1"):
        print("Text is 1")
    else:
        print(text)

func2("Hello", 69) # This is known as an optional parameter, just put an equal sign after the parameter

## Note: Learn more about optional parameters when more than 1 is present