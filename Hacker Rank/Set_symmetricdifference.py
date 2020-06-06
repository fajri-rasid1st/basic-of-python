# Set.symmetric_difference()

a, b = int(input()), set(map(int, input().split(" ")))
c, d = int(input()), set(map(int, input().split(" ")))
print(len(b ^ d))
# b ^ d equal to b.symmetric_difference(d)
