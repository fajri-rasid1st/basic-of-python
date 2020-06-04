def print_formatted(number):

    binary_len = len("{0:b}".format(number))

    for i in range(number):
        print(
            f"{i+1:{binary_len}d} {i+1:{binary_len}o} {i+1:{binary_len}X} {i+1:{binary_len}b}"
        )


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
