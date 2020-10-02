# get index of target if exists else print -1
# binary search is log(n)

def linear_search(nums, target):
    for index, element in enumerate(nums):
        if element == target:
            return index
    return -1

def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2 #floor division
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left  = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    while left < = right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search(nums, target):
    left_index = 0
    right_index = len(nums) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = nums[mid_index]
        if mid_number == target:
            return mid_index
        if mid_number < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

def binary_search_recursive(nums, target, left_index, right_index):
    if right_index < left_index:
        return -1
    mid_index = (left_index + right_index) // 2
    mid_number = nums[mid_index]
    if mid_number == target:
        return mid_index
    if mid_number < target:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    return binary_search_recursive(nums, target, left_index, right_index)


if __name__ == '__main__':
    nums = [2,4,6,7,9,12,15,18]
    target = 7
    print(binary_search(nums, target))

    index = binary_search_recursive(nums, target, 0, len(nums))
    print(index)