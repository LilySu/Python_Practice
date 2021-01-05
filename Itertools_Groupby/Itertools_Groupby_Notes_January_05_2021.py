from operator import itemgetter
from itertools import groupby
#
# # iterator algebra is useful because of: improved memory efficiency (via lazy evaluation) and faster execuction time.
#
# # group a list of tuples based on repeat 2nd value
# test_list = [(1, 4), (2, 4), (6, 7), (5, 1), (6, 1), (8, 1)]
#
# new_list = [[i for i, j in temp] for key, temp in groupby(test_list, key = itemgetter(1))]
#
# print(new_list)
#
# # apply function to each element:
# print(list(map(len, ['abc', 'de', 'fghi'])))
# # map calls iter() on its second argument, advancing iterator with next() till exhausted
#
# print(list(map(sum, zip([1,2,3],[4,5,6]))))
#
# # zip(*iters) returns an iterator over pairs of corresponding elements of each iterator
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = 2
# iters = [iter(nums)] * n
# print(list(id(itr) for itr in iters))


s = [1,2,3,4,5,6,7,8,9]
n = 3
my_list=[[1,2,3],[4,5,6],[7,8,9,10]]
print(zip(*my_list))

# when an iterator yields (= returns) an item, you can imagine this item as "consumed".
# So the next time the iterator is called, it yields the next "unconsumed" item.