# Athlete Sort
attribute = [
    list(map(int, input().split())) for i in range(list(map(int, input().split()))[0])
]

sort_by = int(input())

for item in sorted(attribute, key=lambda index: index[sort_by], reverse=False):
    for sub_item in item:
        print(sub_item, end=" ")
    print()