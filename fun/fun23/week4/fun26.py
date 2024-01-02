
# function summing the numbers in a range
# with specified range and increment
def sum_range(s, e, i):
    return sum(range(s, e, i))

# main execution
if __name__ == '__main__':
    sum_range_value = sum_range(0, 100, 50)
    print(sum_range_value)