def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i  - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor



def insertion_sort(element):
    for i in range(1, len(element)):
        anchor = element[i]
        j = i - 1
        while j >=0 and anchor < element[j]:
            element[j+1] = element[j]
            j -= 1
        element[j + 1] = anchor


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print(elements)