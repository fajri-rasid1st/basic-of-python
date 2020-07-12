# Zipped

x, y = map(int, input().split())

zipped = []

for i in range(y):
    zipped.append(list(map(float, input().split())))


for item in list(zip(*zipped)):
    print(sum(item) / x)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [a] + [b]
# print(list(zip(*c)))
