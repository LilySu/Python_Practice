def insertion_sort(elements):
    for i in range(1, len(elements)): # for each item from after the first to last
        anchor = elements[i] # set up an anchor for each of i
        j = i - 1 # look at the 1 before it
        # while the one we are looking at is within bounds
        # and we are less than the one we are looking at
        while j >= 0 and anchor < elements[j]:
            # move to the left by increasing the index that we were looking at
            elements[j + 1] = elements[j]
            # increment one to the left
            j = j - 1 #
        # if we are greater than the one we are looking at
        # then we belong in this position, we are their plus one
        elements[j + 1] = anchor


def insertion_sort(elements):
    for i in range(1, len(elements)):
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
        elements[j + 1] = anchor

if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print(elements)