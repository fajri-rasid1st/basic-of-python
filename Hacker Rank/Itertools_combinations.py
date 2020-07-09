# itertools.combinations()
import itertools

x = input().split()

for number in range(0, int(x[1])):
    data = [sorted(item) for item in itertools.combinations(x[0], number + 1)]
    for data in sorted(data):
        for sub_data in data:
            print(sub_data, end="")
        print()


# itertools.combinations_with_replacement()
x = input().split()
data = [
    sorted(i) for i in sorted(itertools.combinations_with_replacement(x[0], int(x[1])))
]

for item in sorted(data):
    for sub_item in item:
        print(sub_item, end="")
    print()
