# Symmetric Difference

if __name__ == "__main__":

    symmetric_difference = lambda m, n: set(m).symmetric_difference(n)

    a, b = int(input()), list(map(int, input().split(" ")))
    c, d = int(input()), list(map(int, input().split(" ")))

    for i in sorted(symmetric_difference(b, d)):
        print(i)
