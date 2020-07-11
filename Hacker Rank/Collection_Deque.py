# Collections.Deque()

from collections import deque

deq = deque()

for i in range(int(input())):
    command = input().split()
    if command[0].__eq__("append"):
        deq.append(command[1])
    elif command[0].__eq__("appendleft"):
        deq.appendleft(command[1])
    elif command[0].__eq__("pop"):
        deq.pop()
    else:
        deq.popleft()

for item in list(map(int, deq)):
    print(item, end=" ")
