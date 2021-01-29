def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > anchor:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor

if __name__ == '__main__':
    elements = [9, 3, 7, 1, 8, 2]
    insertion_sort(elements)
    print(elements)