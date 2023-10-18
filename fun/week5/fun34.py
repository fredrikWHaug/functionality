
# fibonacci function with filling list
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# main execution
if __name__ == '__main__':
    fib_list = fib2(14)
    print(fib_list)