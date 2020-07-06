# Set Mutations

len_set, list_set = int(input()), set(map(int, input().split()))

for i in range(int(input())):
    command, new_set = (input().split(), set(map(int, input().split())))

    if command[0].__eq__("intersection_update"):
        list_set.intersection_update(new_set)
    elif command[0].__eq__("update"):
        list_set.update(new_set)
    elif command[0].__eq__("symmetric_difference_update"):
        list_set.symmetric_difference_update(new_set)
    else:
        list_set.difference_update(new_set)

print(sum(list_set))
