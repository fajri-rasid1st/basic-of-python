# Collections.OrderedDict()

from collections import OrderedDict, Counter

order_dict = OrderedDict()
count = []

for i in range(int(input())):
    item = input().split()

    item_name = ""
    for j in range(len(item) - 1):
        item_name += "{} ".format(item[j])

    order_dict[item_name] = int(item[len(item) - 1])
    count.append((item_name, int(item[len(item) - 1])))

item_counter = Counter(count)

for key, value in order_dict.items():
    print("{}{}".format(key, (value * item_counter[(key, value)])))
