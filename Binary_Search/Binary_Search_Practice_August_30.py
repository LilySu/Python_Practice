# get index of target if exists else print -1

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

if __name__ == '__main__':
    nums = [2,4,6,7,9,12,15,18]
    target = 7
    print(binary_search(nums, target))