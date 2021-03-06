def BinarySearch(nums, target):
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

if __name__ == '__main__':
    nums = [2,4,6,7,9,12,15,18]
    target = 15
    print(BinarySearch(nums, target))




def binary_search(elements, target):
    left = 0
    right = len(elements) - 1
    while left <= right:
        mid = (left + right) // 2
        if elements[mid] == target:
            return mid
        elif elements[mid] < target:
            left = left + 1
        else:
            right = mid - 1
    return -1