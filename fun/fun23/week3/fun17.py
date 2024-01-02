
# function derclaration
def safety_first(a, b):
    if a < b:
        return 0
    else:
        return 1
    
# main program execution
if __name__ == '__main__':
    x = 2 
    y = 4
    print(safety_first(x, y))