# Check Subset

checksubset = lambda x, y: x.issubset(y)

for i in range(int(input())):
    a, b = int(input()), set(map(int, input().split()))
    c, d = int(input()), set(map(int, input().split()))
    print(checksubset(b, d))
