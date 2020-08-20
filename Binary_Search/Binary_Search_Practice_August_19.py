def BinarySearch(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = nums - 1
    mid = (left + right) // 2
    while left < right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            mid = left + 1
        else:
            mid = right - 1
    return -1