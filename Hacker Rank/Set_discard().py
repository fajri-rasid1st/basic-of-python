# Set.discard(), remove(), pop()

total_element = int(input())
sets = set(map(int, input().split(" ")))

total_command = int(input())

for i in range(total_command):
    command = input().split(" ")
    if command[0].__eq__("pop"):
        sets.pop()
    elif command[0].__eq__("remove"):
        sets.remove(int(command[1]))
    else:
        sets.discard(int(command[1]))

print(sum(sets))
