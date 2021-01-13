from itertools import groupby

elements = [4,4,4,4,2,2,2,2,2,2,5,5,5]
print([i[0] for i in groupby(elements)])

from itertools import product
sublists = [[1,2,3],[4,5,6],[7,8,9]]
# print(list(product(*sublists)))


from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, i) for i in range(len(s) + 1))

# for i in powerset([1,2,3,4,5,6]):
#     print(i)
#
# print(list(powerset([1,2,3,4,5,6])))

for i in powerset(sublists):
    print(i)

print(list(powerset(sublists)))

some_sublists = [10,[1,2,3],11,[4,5,6],12,[7,8,9]]
newList = []
for i in some_sublists:
    if isinstance(i, list):
        newList.append(i)
    else:
        newList.append([i])

# print(newList)

secondnewList = newList
# print(sorted(secondnewList.extend(i) for i in product(*newList)))

