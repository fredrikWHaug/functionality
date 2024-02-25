
def fib(n):
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(a)
        a, b = b, a + b
    return result

def main():
    print(fib(10))

if __name__ == '__main__':
    main()