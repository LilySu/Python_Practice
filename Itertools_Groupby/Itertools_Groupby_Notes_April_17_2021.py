from itertools import groupby

s = [1,1,1,2,2,3,4,4,4]
print([i[0] for i in groupby(s)])
from itertools import product

sublists = [[1,2,3],[4,5,6],[7,8,9]]
print(list(product(*sublists)))



not_all_sublists =  [[1,2,3],[4,5,6],[7,8,9],10,11]

# from itertools import chain, combinations
#
#
# def powerset(iterable):
#     a = list(iterable)
#     return chain.from_iterable(combinations(a, i) for i in range(len(a) +1))
#
# [print(i) for i in powerset(not_all_sublists )]


# print(list(product(*sublists)))