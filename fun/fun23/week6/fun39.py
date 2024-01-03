
# fibonacci sequence generator
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# main execution
if __name__ == '__main__':
    print(fib(100))