# fibonacci

# fib function without recursion
def fib(n):
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(a)
        a, b = b, a + b
    return result 

# with recursion
def fibr(n):
    if n <= 1:
        return n
    else:
        return fibr(n - 1) + fibr(n - 2)

# main function
def main():
    print(fib(100))

    rec_result = []
    for i in range(12):
        rec_result.append(fibr(i))
    print(rec_result)

# main execution
if __name__ == '__main__':
    main()