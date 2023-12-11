# fibonacci with recursion

# fibonacci function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
# main function
def main():
    for i in range(11):
        print(fib(i))

# main execution
if __name__ == '__main__':
    main()