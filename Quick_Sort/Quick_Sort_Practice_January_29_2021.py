def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot_ind = start
    pivot = elements[start]
    while start < end:
        while start < len(elements) and pivot >= elements[start]:
            start += 1
        while pivot < elements[end]:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(pivot_ind, end, elements)
    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)

if __name__ == '__main__':
    elements = [9, 1, 8, 2, 7, 3, 6]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)