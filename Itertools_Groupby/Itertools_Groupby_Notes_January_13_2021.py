from itertools import groupby

s = [1,1,1,2,2,3,4,4,4]
# print([i[0] for i in groupby(s)])

from itertools import product
sublists = [[1,2,3],[4,5,6],[7,8,9]]
# print(list(product(*sublists)))

from itertools import chain, combinations
lists_and_nonlists = [[1,2,3],[4,5,6],[7,8,9], 10, 11]
clean_list_of_lists = []
for i in lists_and_nonlists:
    if isinstance(i, list):
        clean_list_of_lists.append(i)
    else:
        clean_list_of_lists.append([i])

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, i) for i in range(len(s) + 1))

# for i in powerset(clean_list_of_lists):
#     print(i)
print([i for i in powerset(clean_list_of_lists)])

# chain.from_iterable(combinations(s, i) for i in range(len(s) + 1))
