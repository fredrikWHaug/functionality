
def binary_search(target, nums):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2 
        mid_value = nums[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            high = mid - 1
        else:
            low = mid + 1
    return mid

def main():
    nums = [0, 1, 2, 3, 4]
    target = 3
    index = binary_search(target, nums)
    print(index)

if __name__ == '__main__':
    main()