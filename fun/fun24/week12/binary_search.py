
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return mid
        elif target > mid_value:
            low = mid + 1
        else:
            high = mid - 1

def main():
    nums = [0, 1, 2, 3, 4]
    target = 4
    index = binary_search(nums, target)
    print(index)

if __name__ == '__main__':
    main()