# Compress The String
import itertools


def get_length(n):
    return n


s = input()

group_s = itertools.groupby(s, get_length)
data = [(len(list(group)), int(key)) for key, group in group_s]

for sub_data in data:
    print(sub_data, end=" ")
