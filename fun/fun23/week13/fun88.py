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

    return -1 # target not found

# quick sort function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# main function
def main():
    example_array = [0, 8, 6, 1, 2, 3, 4, 0, 0, 2, 7]
    sorted_array = quick_sort(example_array)
    print(sorted_array)
    target = 3

    result = binary_search(sorted_array, target)

    if result != -1:
        print(f'Target found at index {result}')
    else:
        print(f'The target value {target} was not found in the sorted array')

if __name__ == '__main__':
    main()