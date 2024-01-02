# fib

# fibonacci function
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# main function
def main():
    print(fib(69))

# main execution
if __name__ == '__main__':
    main()