# any() = This expression returns True if any element of the iterable is true.
# all() = This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.
x = int(input())

items = list(map(int, input().split()))

if all(list(map(lambda x: x > 0, items))):
    if any(list(map(lambda x: list(str(x)).__eq__(list(reversed(str(x)))), items))):
        print(True)
    else:
        print(False)
else:
    print(False)
