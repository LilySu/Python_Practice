# from itertools import groupby
# import itertools as it
#
# elements = [5,6,6,6,2,2,2]
# print([i[0] for i in groupby(elements)])
#
# nonnested = [1,2,3,4,5,6,7,8,9]
# # for L in range(0, len(nonnested) + 1):
# #     for subset in it.combinations(nonnested, L):
# #         print(subset)
#
# # from itertools import chain, combinations
# #
# # def powerset(iterable):
# #     s = list(iterable)
# #     return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
# #
# # for result in powerset([1,2,3]):
# #     print(result)
# #
# # results = list(powerset([1,2,3]))
# # print(results)
#
# nested = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]]
from itertools import product

# print(list(product(*nested)))

nested = ['1', ['2', '2x'], '3', '4', ['5', '5x'],['6','6x']]
nonlist = []
li = []
for i in nested:
    if isinstance(i, list):
        li.append(i)
    else:
        nonlist.append(i)
print(nonlist)
print(li)
for i in product(*nested):
    sub = nonlist[:]
#     sub.extend(i)
#     print(sorted(sub))