# Priority Queues - elements with higher priority come out of priority queue first.
# uses a heap - a tree-based structure max is top for max heap and vice versa

# priority queue to fetch shortest path algorithm
# dynamically fetch next best or next worst
# Best First Search Algorithms BFS uses priorty queue to grab next best
# lossless data compression

# min heap

# from heapq import heapify
#
# extList = [15, 2, 5, 11, 7, 3, 9, 1, 6, 8]
# print('Before:', extList)
# heapify(extList)
# print('After:', extList)

from queue import PriorityQueue
q = PriorityQueue()
# q.empty()
q.put((3, 'python'))
q.put((4, 'java'))
q.put((2, 'ruby'))
q.put((1, 'golang'))

print(q.get())
print(q.get())