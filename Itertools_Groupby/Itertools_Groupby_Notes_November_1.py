# notes from https://www.youtube.com/watch?v=jijYnDqhY9w&ab_channel=RyanNoonan
import itertools

data1 = [100, 80, 80, 80, 80, 90, 90, 85, 85, 85]

keys = []
groups = []
sorted_data1 = sorted(data1)
for k, g, in itertools.groupby(sorted_data1):
    keys.append(k)
    groups.append(list(g))

print('groups', groups)
print('keys', keys) # get just unique values

# get count
count_per_group = [len(i) for i in groups]
print('count per group', count_per_group)

zip_values = dict(zip(keys, count_per_group))
print('zip values', zip_values)

data2 = 'AAAAABBBCCCDAAAABBB'
sorted_data2 = sorted(data2)

comprehension1 = [k for k, g in itertools.groupby(sorted_data2)]
print('group by letter', comprehension1) # get only unique elements

comprehension2 = [len(list(g)) for k, g in itertools.groupby(sorted_data2)]
print('count per group', comprehension2) # get counts for each item


s = "cbb"
a = "".join(c for c, _ in itertools.groupby(s))
print('s', a)