def insertion_sort(elements):
    for i in range(1, len(elements)):
        # assign an anchor for each
        anchor = elements[i]
        # assign j as the previous index
        j = i - 1
        # while the last index is bigger or equal than zero
        # if the iterator is less than the previous element
        # this while loop iterates through each element
        # making sure each is swapped until sorted

        while j >= 0 and anchor < elements[j]:
            # swap
            elements[j + 1] = elements[j]
            # let j become 1 less now iterator are swapped
            j = j - 1
        # increment anchor that compares eaxh
        elements[j + 1] = anchor


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j  = j - 1
        elements[j + 1] = anchor
