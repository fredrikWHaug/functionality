# fibonacci recursion

# fiobonacci function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
# main function
def main():
    result = []
    for i in range(10):
        result.append(fib(i))
    print(result)

# main execution
if __name__ == '__main__':
    main()