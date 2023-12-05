# fibonacci with recursion

# fib function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
# main function
def main():
    for i in range(10):
        print(fib(i))

# main execution
if __name__ == '__main__':
    main()