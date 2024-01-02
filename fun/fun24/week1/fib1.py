# fibonacci with  and without recursion

# fib function (recursion)
def fibr(n):
    if n <= 1:
        return n
    else:
        return fibr(n - 1) + fibr(n - 2)
    
# fib function (no recursion)
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
    
# main function
def main():
    #recursion output
    print('Fibonacci list produced with recursion: ')
    result = []
    for i in range(12):
        result.append(fibr(i))
    print(result)

    # no recursion output
    print(f'Here is a fibonacci list produced without recursion: ')
    print(fib(100))
    
# main execution
if __name__ == '__main__':
    main()