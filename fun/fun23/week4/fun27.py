
# function finding prime numbers
def finding_primes(r):
    for n in range(2, r):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n //x)
                break
        else:
            print(n, 'is a prime number')

# main execution
if __name__ == '__main__':
    r = 100
    finding_primes(r)