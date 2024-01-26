# binary search

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
    return mid

def main():
    ordered_list = [1, 2, 3, 4, 5]
    target = 1
    index = binary_search(target, ordered_list)
    print(index)

if __name__ == '__main__':
    main()