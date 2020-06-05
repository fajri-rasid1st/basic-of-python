# introduction to set


def average(array):
    my_set = set(array)
    total_number = 0

    for i in my_set:
        total_number += i

    return total_number / len(my_set)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
