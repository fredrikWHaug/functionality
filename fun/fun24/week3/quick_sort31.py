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
    unordered_list = [3, 6, 1, 2, 0, 5]
    ordered_list = quick_sort(unordered_list)
    print(f'quick sort sorted {unordered_list} to {ordered_list}')

# main execution
if __name__ == '__main__':
    main()