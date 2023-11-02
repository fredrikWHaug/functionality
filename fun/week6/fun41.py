
# fibonacci sequence
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, b + a
    return result

# main execution
if __name__ == '__main__':
    print(fib(1000))