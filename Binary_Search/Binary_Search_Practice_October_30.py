def binarySearch(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            mid = left + 1
        else:
            mid = left - 1
        return -1