def swap(a, b, arr):
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
    Quick_Sort_Practice_January_25_2021.py    swap(pivot_index, end, elements)
    return end

def quickSort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quickSort(elements, start, pi - 1)
        quickSort(elements, pi + 1, end)

if __name__ == '__main__':
    elements = [53, 29, 83, 14, 70]
    quickSort(elements, 0, len(elements) - 1)
    print(elements)