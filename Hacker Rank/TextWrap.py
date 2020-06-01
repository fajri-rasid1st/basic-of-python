import textwrap


def wrap(string, max_width):
    # opsi 1
    # wrap = ""
    # for i in textwrap.wrap(string, max_width):
    #     wrap += i + "\n"
    # return wrap

    # opsi 2
    return textwrap.fill(string, max_width)


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
