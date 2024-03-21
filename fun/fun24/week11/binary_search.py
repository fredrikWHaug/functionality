
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return mid 
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return mid 

def main():
    nums = [1, 2, 3, 4, 5]
    target = 3
    index = binary_search(nums, target)
    print(index)

if __name__ == '__main__':
    main()