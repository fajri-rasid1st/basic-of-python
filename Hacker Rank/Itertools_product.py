# itertools.product()
import itertools

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

for item in itertools.product(a, b):
    print(item, end=" ")
