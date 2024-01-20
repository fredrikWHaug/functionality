# binary search

# binary search function
def binary_search(target, array):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = array[mid]
        if target == mid_value:
            return mid
        elif target < mid_value:
            high = mid - 1
        else:
            low = mid + 1

# main function
def main():
    my_list = [3, 4, 2, 1, 5, 8]
    my_list.sort()
    target = 1
    index = binary_search(target, my_list)
    print(f'The index of {target} in {my_list} is {index}')

# main execution
if __name__ == '__main__':
    main()