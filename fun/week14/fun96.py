# binary search

# search function
def binary_search(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = array[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# main function
def main():
    ordered_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    target = 5

    result = binary_search(ordered_list, target)
    
    if result != -1:
        print(f'Target found at index {result}')
    else:
        print(f'Target not found in given list')

# main execution
if __name__ == '__main__':
    main()