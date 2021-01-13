from itertools import groupby

# elements = [4,4,4,4,2,2,2,2,2,2,5,5,5]
# print([i[0] for i in groupby(elements)])

from itertools import product
# sublists = [[1,2,3],[4,5,6],[7,8,9]]
# print(list(product(*sublists)))

some_sublists = [10,[1,2,3],11,[4,5,6],12,[7,8,9]]

proper_sublists = []
for i in some_sublists:
    if isinstance(i, list):
        proper_sublists.append(i)
    else:
        proper_sublists.append([i])

# print(proper_sublists)
sub = proper_sublists
print(sorted(sub.extend(i) for i in product(*proper_sublists)))