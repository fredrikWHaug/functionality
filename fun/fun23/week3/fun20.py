
# initial l numbers in fibonacci sequence
def fibonacci(l):
    fibonacci_container = []
    a, b = 0, 1
    while a < l:
        fibonacci_container.append(a);
        a, b = b, a + b
    return fibonacci_container

# main execution
if __name__ == '__main__':
    fib_numbers = fibonacci(100);
    for i in fib_numbers:
        print(i)