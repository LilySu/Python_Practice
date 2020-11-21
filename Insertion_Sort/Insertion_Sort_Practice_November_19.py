
# def insertion_sort(elements):
#     for i in range(1, len(elements)):
#         anchor = elements[i]
#         j = i - 1
#         while j >= 0 and anchor < elements[j]:
#             elements[j + 1] = elements[j]
#             j = j - 1
#         elements[j + 1] = anchor
#
#
# def insertion_sort(elements):
#     for i range(1, len(elements)):
#         anchor = elements[i]
#         j = i - 1
#         while j >= 0 and anchor < elements[j]:
#             elements[j + 1] = elements[j]
#             j = j - 1
#         elements[j + 1] = anchor
#
#
# def insertion_sort(elements):
#     for i in range(1, len(elements)):
#         anchor = elements[i]
#         j = i - 1
#         while j >= 0 and anchor < elements[j]:
#             elements[j + 1] = elements[j]
#             j = j - 1
#         elements[j + 1] = anchor
#
#
#
#
# def insertion_sort(elements):
#     for i in range(1, len(elements)):
#         anchor = elements[i]
#         j = i - 1
#         while j >= 0 and anchor < elements[j]:
#             elements[j + 1] = elements[j]
#             j -= 1
#         elements[j + 1] = anchor
#
#
# def insertion_sort(elements):
#     for i in range(1, len(elements)):
#         anchor = elements[i]
#         j = i - 1
#         while j >= 0 and anchor < elements[j]:
#             elements[j + 1] = elements[j]
#             j = j - 1
#         elements[j + 1] = anchor




def insertion_sort(elements):
    for i in range(len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor

def insertion_sort(elements):
    for i in range(len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor

















def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = elements[j]


if __name__ == "__main__":
    elements = [9, 27,2, 5,1, 84]
    insertion_sort(elements)
    print(elements)