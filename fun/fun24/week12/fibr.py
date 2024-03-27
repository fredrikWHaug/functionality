
def fibr(n):
    if n <= 1:
        return n
    else:
        return (n - 1) + (n - 2)
    
def main():
    for i in range(10):
        print(fibr(i))

if __name__ == '__main__':
    main()