
def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = array[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            high = mid - 1
        else:
            low = mid + 1
    return mid

def main():
    example_list = [2, 4, 6, 8, 10]
    target = 6
    index = binary_search(example_list, target)
    print(index)

if __name__ == '__main__':
    main()