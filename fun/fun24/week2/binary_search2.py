# binary search

# binary search function
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
    return mid

# main function
def main():
    my_list = [0, 1, 2, 3, 4, 5]
    target = 1
    index = binary_search(my_list, target)
    print(f'The index of {target} in {my_list} is {index}')

# main execution
if __name__ == '__main__':
    main()