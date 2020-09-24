lst = [5,6,0,1,2,4,3,9,8,7]

for i in range(1, len(lst)):
    key = lst[i]
    j = i-1
    while j >= 0 and key < lst[j]:
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = key

print(lst)