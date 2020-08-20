def binarySearch(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == '__main__':
    # nums = [-1,0,3,5,9,12]
    # target = 9
    nums = [-1, 0, 3, 5, 9, 12]
    target = 5
    print(binarySearch(nums, target))