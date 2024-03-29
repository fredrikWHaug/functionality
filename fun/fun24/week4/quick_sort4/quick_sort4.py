# quick sort

# quick sort function
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x < pivot ]
        greater = [x for x in array[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
# main functon
def main():
    unordered_list = [3, 2, 1]
    ordered_list = quick_sort(unordered_list)
    print(ordered_list)

# main execution
if __name__ == '__main__':
    main()