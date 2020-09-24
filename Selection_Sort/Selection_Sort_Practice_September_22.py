list_a = [5,6,0,1,2,4,3,9,8,7]

indexing_length = range(0, len(list_a)-1) # we don't compare the last item
for i in indexing_length:
    min_value = i
    for j in range(i+1, len(list_a)):
        if list_a[j] < list_a[min_value]:
            min_value = j # do swap at min_value's position at the very end
    if min_value != i: # if we find a value lower than our default, then we need to switch items
        list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

print(list_a)