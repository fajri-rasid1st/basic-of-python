# design door mat

size = list(map(int, input().split(" ")))

x = 1
y = -(size[0] - 2)

for i in range(size[0]):
    if (size[0] // 2 + 1) == i + 1:
        print("WELCOME".center(size[1], "-"))
        x = y
    else:
        print((".|." * abs(x)).center(size[1], "-"))
        x += 2
