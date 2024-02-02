# binary search

def binary_search(target, array):
    low, high = 0, len(array) - 1
    while low < high:
        mid = (low + high) // 2
        mid_value = array[mid]
        if target == mid_value:
            return mid
        elif target > mid_value:
            low = mid + 1
        else:
            high = mid - 1
    return mid

# main function
def main():
    my_list = [1, 2, 3, 4]
    target = 2
    index = binary_search(target, my_list)
    print(index)

# main execution
if __name__ == '__main__':
    main()