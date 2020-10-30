# time complexity is O(n^2)
# space complexity O(1) # 1 extra variable, no extra space

def bubble_sort(elements):
    size = len(elements)
    for k in range(len(elements) - 1):
        swapped = False
        for i in range(size - 1 - k): # don't go to the end, same some time
            if elements[i] > elements[i + 1]:
                # swap
                tmp = elements[i]
                elements[i] = elements[i + 1]
                elements[i+1] = tmp
                # now the highest element is sorted up to this point without outer loop
                swapped = True
        # the inner loop after completing, if not swapped is already sorted
        if not swapped:
            break
# now time complexity is O(n) for sorted list


def bubble_sort(elements):
    size = len(elements)
    for k in range(len(elements) - 1):
        swapped = False
        for i in range(size - 1 - k):
            if elements[i] > elements[i + 1]:
                tmp = elements[i]
                elements[i] = elements[i + 1]
                elements[i+1] = tmp
                swapped = True
    if not swapped:
        break

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    bubble_sort(elements)
    print(elements)