# itertools.permutations()
import itertools

input_user = input().split()

for item in sorted(itertools.permutations(input_user[0], int(input_user[1]))):
    for sub_item in item:
        print(sub_item, end="")
    print()
