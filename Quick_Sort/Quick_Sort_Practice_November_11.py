def swap(a, b, arr):
    arr[b], arr[a] = arr[a], arr[b]

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < len(elements) and elements[start] <= pivot:
        