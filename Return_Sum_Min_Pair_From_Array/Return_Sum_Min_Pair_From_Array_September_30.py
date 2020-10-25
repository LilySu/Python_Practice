import sys


def smallest_pair(nums):
    min_number = nums[0]
    second_min = nums[1]
    for ind, i in enumerate(nums[2:]):
        if i < min_number:
            second_min = min_number
            min_number = i
        elif (i < second_min) and (i != min_number):
            second_min = nums[j]
    return second_min + min_number


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(smallest_pair(nums))
