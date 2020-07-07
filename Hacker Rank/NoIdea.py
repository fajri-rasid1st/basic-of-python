# No Indea

a, b, c, d = (
    input(),
    list(map(int, input().split())),
    set(map(int, input().split())),
    set(map(int, input().split())),
)

happines = 0

for i in b:
    if i in c:
        happines += 1
    elif i in d:
        happines -= 1

print(happines)
