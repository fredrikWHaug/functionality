
# fib function with list return
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# main execution
if __name__ == '__main__':
    fib_list = fib(1000)
    print(fib_list)