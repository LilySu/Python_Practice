def merge_sort(A):
    merge_sort2(A, 0, len(A)-1) # recursive, pass in list, first and last index

def merge_sort2(A, first, last):
    if first < last: # there is more than 1 item in the list
        middle = (first + last)//2 # break the item in half
        merge_sort2(A, first, middle) # work on 1st half of the list
        merge_sort2(A, middle+1, last) # work on 2nd half of the list
        merge(A, first, middle, last) # combine the sorted list together

def merge(A, first, middle, last):
    L = A[first:middle] # left half
    R = A[middle:last+1] # right half
    L.append(99999999) # attach on some large number to end of list
    R.append(99999999)
    i = j = 0
    for k in range(first, last+1):
        if L[i] <= R[j]: # if the left is smaller
            A[k] = L[i] # copy left item to A
            i += 1 # increment our index
        else:
            A[k] = R[j]
            j += 1
