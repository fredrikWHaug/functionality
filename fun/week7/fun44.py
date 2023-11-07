import sys

def fun(x):
    return ((x**2) + 2) / ((x**4) + 32)

print(fun(int(sys.argv[1])))
