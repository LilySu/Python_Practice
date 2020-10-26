# Priority queue - items considered priority are extracted from the list first
# Python's heap implementation is a min-heap
# heapq expects item to be in list, using push and pop
# we construct binary tree out of list by calculating indexes left: 2*i+1 right: 2*i+2
#
# Time complexity:
# insertion: O(log(n))
# deletion: O(log(n))
# find min: O(1)
# sorting: O(nlog(n))
# searching: O(n)

from heapq import heapify

extList = [15,2,5,11,7,3,9,1,6,8]
print('Before : ', extList)
heapify(extList)
print('After heapify : ', extList)

from heapq import heappush
# adds element to heap maintaining heap property
minHeap = []
heappush(minHeap, 4)
heappush(minHeap, 9)
heappush(minHeap, 12)
heappush(minHeap, 7)
heappush(minHeap, 2)
heappush(minHeap, 5)
heappush(minHeap, 6)
heappush(minHeap, 10)
heappush(minHeap, 8)
heappush(minHeap, 3)
print('minHeap using heappush : ', minHeap)

from heapq import heappop
# removes min, restructures binary tree
# elements are internally shuffled
print('Before : ', minHeap)
print('heappop : ', heappop(minHeap))
print('After : ', minHeap)

from heapq import heappushpop
# inserts element first and pops min element after

from heapq import heapreplace
# extract min first, push in after

from heapq import merge
# merge(*iterables, key=None, reverse=False) : returns generator function which returns
# single sorted elements from given multiple sorted iterables
# merges 2 lists
f1 = ['Jasmine','Lavender','Lily','Lotus', 'Rose','Tulips']
f2 = ['Bougainvillea','Calendula','Dahlia','Peony']

print('merge : ', type(merge(f1,f2)))
optL = list(merge(f1,f2))
print('\nf1 : ', f1)
print('f2 : ', f2)
print('\nSorted merged list : ', optL)

# will sort by length
# optL = list(merge(f1,f2, key=len))


# returns list of n largest elements after sorting given iterable by key
from heapq import nlargest
print('minHeap : ', minHeap)
print('nlargest 3 : ',nlargest(3, minHeap))

