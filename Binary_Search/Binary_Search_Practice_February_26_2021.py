def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target[mid] == target:
            return mid
        elif target[mid] < target:
            left = mid + 1
        elif target[mid] > target:
            right = mid - 1
    return -1