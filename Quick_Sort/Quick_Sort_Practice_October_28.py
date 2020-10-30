# divide a conquer problem
# indicate the midpoint as a pivot point
# work on left and right partitions
# recursively sort on partitions by comparing each element to the pivot

# Hoare
# start pointer increments until it find an element greater than pivot
# end pointer increments towards start until finding element less than pivot
# numbers that meet above 2 conditions are swapped
# stop when end before start, then swap end with pivot

def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    # find a place where element is greater than pivot
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)
    return end


def quick_sort(elements, start, end):
    if start < end:
        pivot = partition(elements, start, end)
        quick_sort(elements, start, pivot - 1)
        quick_sort(elements, pivot + 1, end)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)