# fibonacci sequence

# fibonacci function with print
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b

# main function
def main():
    fib(10)

# main execution
if __name__ == '__main__':
    main()