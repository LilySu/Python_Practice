import heapq

li = [5,7,9, 1, 3]
heapq.heapify(li)
print(li)

heapq.heappush(li, 4) # push item to current tree, perform shuffling
print(li)

heapq.heappop(li)
print(li)

print(heapq.heappushpop(li,2)) # pushes 3 to array, then pops the top values and sorts again
# doesn't change
print(li)

