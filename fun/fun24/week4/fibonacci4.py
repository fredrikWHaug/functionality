# fibonacci 

# fibonacci function without recursion
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b 
    return result

# fib function with recursion 
def fibr(n):
    if n <= 1:
        return n 
    else:
        return fibr(n - 1) + fibr(n - 2) 
    
# main function 
def main():
    print(fib(100))
    result = []
    for i in range(12):
        result.append(fibr(i))
    print(result)

# main execution
if __name__ == '__main__':
    main()