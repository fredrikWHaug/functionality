
# simple calculator function
def calc(x, y, operation):
    if (operation == "*"):
        return x * y
    elif (operation == "?"):
        return x / y
    elif (operation == "+"):
        return x + y
    elif (operation == "-"):
        return x - y
    else:
        return ("Something went wrong")
    
# main execution
if __name__ == "__main__":
    multiplication = calc(5, 5, "*")
    print(multiplication)
    addition = calc(7, 4, "+")
    print(addition)
    error = calc(5, 5, ")")
    print(error)