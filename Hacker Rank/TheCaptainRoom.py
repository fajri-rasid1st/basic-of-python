# The Captain Room


def captain_room(k, list_room):
    set_room = set(list_room)
    return ((sum(set_room) * k) - (sum(list_room))) // (k - 1)


k = int(input())
print(captain_room(k, list(map(int, input().split()))))

# Another Solution (time limit)
# x = list(map(int, input().split()))
# y = set(x)

# for i in y:
#     if x.count(i) == 1:
#         print(i)
#         break
