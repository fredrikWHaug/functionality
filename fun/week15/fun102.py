# quick sort

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
# main function (test)
def main():
    unordered_list = [3, 5, 6, 1, 6, 7, 8]
    ordered_list = quicksort(unordered_list)
    print('unordered list', unordered_list, end=' ')
    print()
    print('ordered list', ordered_list, end=' ')

# main execution
if __name__ == '__main__':
    main()