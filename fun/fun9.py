# simple arithmetic 
def calculator(x, y, operation):
    if (operation == '+'):
        return x + y
    elif (operation == '-'):
        return x - y
    elif (operation == '*'):
        return x * y
    elif (operation == '/'):
        return x / y 
    else:
        print('You entered something wrong')

# execution example
if __name__ == "__main__":
    calculator(5, 5, "*")
    # returns 25
