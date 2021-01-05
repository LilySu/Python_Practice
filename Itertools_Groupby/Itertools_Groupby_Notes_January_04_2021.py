from itertools import groupby

elements = [100, 80, 80, 80, 80, 90, 90, 85, 85, 85]

new_list = []
# for i in groupby(elements):
#     new_list.append(i[0])

new_list = [i[0] for i in groupby(elements)]

from operator import itemgetter
new_mapped = list(map(itemgetter(0), groupby(elements)))


print(new_list)
print(new_mapped)