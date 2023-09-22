# function squaring every other element in a list
def every_other_is_squared(nums):
    for i in range(len(nums)):
        if (i % 2 == 0):
            nums[i] = nums[i] ** 2
    return nums

#example run
if __name__ == '__main__':
    numsi = [1, 2, 3, 4]
    print(every_other_is_squared(numsi))
