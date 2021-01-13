def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)
    while left <= right:
        mid = (left + right )// 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1,2,3,4,5,6,7,8], 4))