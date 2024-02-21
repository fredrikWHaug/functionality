# binary search

# binary search function
def binary_search(target, array):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = array[mid]
        
        if mid_value == target:
            return mid
        elif mid_value > target:
            low = mid + 1
        else:
            high = mid - 1
    return mid

# main function
def main():
    my_list = [1, 2, 3, 4]
    target = 3
    index = binary_search(target, my_list)
    print(index)

# main execution
if __name__ == '__main__':
    main()