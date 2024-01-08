# fibonacci

#fibonacci function w/o recursion
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# fibonacci with recursion
def fibr(n):
    if n <= 1:
        return n
    else:
        return fibr(n - 1) + fibr(n - 2)

# main function
def main():
    # no recursion 
    print(f'No recursion fib numbers: {fib(100)}')
    # recursion
    result = []
    for i in range(12):
        result.append(fibr(i))
    print(f'Recursion fib numbers:{result}')

# main execution
if __name__ == '__main__':
    main()