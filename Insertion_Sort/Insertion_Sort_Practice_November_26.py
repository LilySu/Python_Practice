def InsertionSort(elements):
    for i in range(len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor

def InsertionSort(elements):
    for i in range(len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor

if __name__ == "__main__":
    elements = [6, 2, 1, 8, 3, 9, 7]
    InsertionSort(elements)
    print(elements)