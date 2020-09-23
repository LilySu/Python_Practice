lst = [5,6,0,1,2,4,3,9,8,7]

while True:
    check_for_swap = False
    for i in range(0, 9):
        if lst[i] > lst[i + 1]:
            swap = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = swap
            check_for_swap = True
    if check_for_swap == False:
        break
print(lst)
