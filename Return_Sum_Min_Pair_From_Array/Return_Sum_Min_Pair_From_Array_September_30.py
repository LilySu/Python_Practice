import sys

# def smallest_pair(nums):
#     min = sys.maxsize
#     secondMin = sys.maxsize
#     for j in range(len(nums)):
#         if nums[j] < min:
#             secondMin = min
#             min = nums[j]
#         elif (nums[j] < secondMin) and (nums[j] != min):
#             secondMin = nums[j]
#     return secondMin + min

def smallest_pair(nums):
    min = float('inf')
    secondMin = float('inf')
    for j in range(len(nums)):
        if nums[j] < min:
            secondMin = min
            min = nums[j]
        elif (nums[j] < secondMin) and (nums[j] != min):
            secondMin = nums[j]
    return secondMin + min


def smallest_pair(nums):
    min = float('inf')
    secondMin = float('inf')
    for j in range(len(nums)):
        if nums[j] < min:
            secondMin = min
            min = nums[j]
        elif (nums[j] < secondMin) and (nums[j] != min):
            secondMin = nums[j]
    return secondMin + min


def smallest_pair(nums):
    min = float('inf')
    secondMin = float('inf')
    for j in range(len(nums)):
        if nums[j] < min:
            secondMin = min
            min = nums[j]
        elif (nums[j] < secondMin) and (nums[j] != min):
            secondMin = nums[j]
    return secondMin + min

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(smallest_pair(nums))