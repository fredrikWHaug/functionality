# write Fibbonaci sequence up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, b+a
        print()

# main execution
if __name__ == '__main__':
    fib(100)