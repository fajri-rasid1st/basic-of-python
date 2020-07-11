# Collections.DefaultDict()

a_and_b = list(map(int, input().split()))

a = [input() for i in range(a_and_b[0])]
b = [input() for i in range(a_and_b[1])]

for item in b:
    if item not in a:
        print(-1)
        continue
    for i in range(len(a)):
        if item.__eq__(a[i]):
            print(i + 1, end=" ")
    print()
