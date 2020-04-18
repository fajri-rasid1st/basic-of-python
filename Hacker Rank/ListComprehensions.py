# List Comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# alternative 1
result = [
    [i, j, k]
    for i in range(0, x + 1)
    for j in range(0, y + 1)
    for k in range(0, z + 1)
    if (i + j + k) != n
]

print(result)
# alternative 1 equals to:
# for i in range(0, x + 1):
#     for j in range(0, y + 1):
#         for k in range(0, z + 1):
#             if (i + j + k) != n:
