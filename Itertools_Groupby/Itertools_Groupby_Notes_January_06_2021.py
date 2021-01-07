from itertools import groupby
import itertools as it

l = [2,4,4,4,6,6,7,8]
print([i[0] for i in groupby(l)])

x = ['a', 'b', 'c']
y = [1, 2, 3, 4, 5]
print(list(it.zip_longest(x, y)))

iters = [iter(l)] * 4
print(list(zip(*iters)))

a = [iter(l)] * 5
print(list(zip(*a)))