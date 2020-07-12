# Map and Lambda
cube = lambda x: x * x * x


def fibonacci(n):
    fibo_list = [0]

    x, y = 0, 1

    if n == 0:
        return list()

    for i in range(n - 1):
        fibo_list.append(x + y)
        x = fibo_list[i]
        y = fibo_list[i + 1]

    return fibo_list


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
