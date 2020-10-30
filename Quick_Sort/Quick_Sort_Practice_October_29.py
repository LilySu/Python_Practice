def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
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



























def swap(a, b, nums):
    nums[a], nums[b] = nums[b], nums[a]

def partition(elements):
    pivot_index = 0
    pivot = elements[pivot_index]
    start = pivot_index + 1
    end = len(elements) - 1
    while elements[start] <= pivot: # when greater, swap
        start += 1
    while elements[end] > pivot: # when less swap
        end -= 1
    if start < end:
        swap(start, end, elements)

def quick_sort(elements):
    partition(elements)

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements)
    print(elements)