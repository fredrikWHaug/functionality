# quick sort

# quick sort function
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
# main function
def main():
    unsorted_list = [7, 2, 3, 1, 4, 5, 1]
    sorted_list = quick_sort(unsorted_list)
    print(f'Unsorted list: {unsorted_list}')
    print(f'List sorted with quick sort: {sorted_list}')

# main execution
if __name__ == '__main__':
    main()