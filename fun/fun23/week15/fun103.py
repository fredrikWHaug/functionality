
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array [1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def binary_search(target, array):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = len(array) // 2
        mid_value = array[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def main():
    unordered_list = [2, 55, 6, 22, 5, 21, 2]
    ordered_list = quick_sort(unordered_list)
    print('unordered list', unordered_list, end=' ')
    print()
    print('ordered list', ordered_list, end=' ')

    binary_search(22, ordered_list)

if __name__ == '__main__':
    main()