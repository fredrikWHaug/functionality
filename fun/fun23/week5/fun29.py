
# implementing prime number finder with the continue built in function
def prime_continuation_implementation(n):
    even_numbers = []
    odd_numbers = []
    for i in range(0, n):
        if i % 2 == 0:
            even_numbers.append(i)
            continue
        odd_numbers.append(i)
    return [len(even_numbers), len(odd_numbers)]

# main implementation
if __name__ ==  '__main__':
    looking_distance = 100
    result = prime_continuation_implementation(looking_distance)
    print(f'There are {result[0]} even numbers and {result[1]} odd numbers from 2-100')