def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end:
        while start < len(elements) and pivot >= elements[start]:
            start += 1
        while pivot < elements[end]:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)
    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)

if __name__ == '__main__':
    elements = [68, 27, 4, 55, 3, 1]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)