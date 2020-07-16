# # 1
# for i in range(2, 4):
#     # akan di print list dari index ke 1 sampai 4
#     print([1, 2, 3, 4, 5][i])

# # 2
# # menggabungkan 2 atau lebih iterable
# import itertools

# print(list(itertools.chain([1, 2, 3], [4, 5, 6])))

# # 3
# # mengurutkan string tanpa mengubah ke list terlebih dahulu
# s = "".join(sorted(input()))
# t = "".join(reversed(sorted(input())))
# print(s)
# print(t)

import re

pattern = re.split(r"[-]*", input())
print(len("".join(pattern)))
