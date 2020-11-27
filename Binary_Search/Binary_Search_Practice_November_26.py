def BinarySearch(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1
    return -1

elements = [981, 34, 72, 10, 46, 82, 1]
elements = sorted(elements)
print(elements)
print(BinarySearch(elements, 34))