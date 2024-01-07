# binary search

# binary search function
def binary_search(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = array[mid]

        if mid_value == target:
            return target
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return mid

# main function
def main():
    my_list = [3, 4, 5, 1, 2, 6]
    print(f'my_list unsorted: {my_list}')
    my_list.sort()
    print(f'my_list sorted: {my_list}')
    target = 1
    index = binary_search(my_list, target)
    print(f'The index of {target} in sorted my_list is {index}')

# main execution
if __name__ == '__main__':
    main()