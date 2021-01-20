from itertools import groupby

s = [1,1,1,2,2,3,4,4,4]
print([i[0] for i in groupby(s)])

from itertools import product

sublists = [[1,2,3],[4,5,6],[7,8,9]]
print(list(product(*sublists)))

not_all_sublists =  [[1,2,3],[4,5,6],[7,8,9],10,11]
not_all_sublists_result = []
for i in not_all_sublists:
    if isinstance(i, list):
        not_all_sublists_result.append(i)
    else:
        not_all_sublists_result.append([i])

from itertools import chain, combinations

def powerset(iterable):
    iterable_list = list(iterable)
    return chain.from_iterable(combinations(iterable_list, i) for i in range(len(iterable_list) + 1))

print([i for i in powerset(not_all_sublists_result)])