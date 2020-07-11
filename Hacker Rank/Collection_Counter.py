# Collections.counter()

from collections import Counter


def amount_of_money(size=list(), customers=list()):
    total = 0
    counter = Counter(size)

    for item in customers:
        if item[0] in list(counter.keys()) and counter[item[0]] != 0:
            total += item[1]
            counter.subtract({item[0]: 1})
    return total


if __name__ == "__main__":
    x = int(input())
    shoes_size = list(map(int, input().split()))
    customers = [list(map(int, input().split())) for i in range(int(input()))]
    print(amount_of_money(shoes_size, customers))
