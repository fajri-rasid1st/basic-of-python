# string split and join
def split_and_join(line):
    strArr = line.split(" ")

    return "-".join(strArr)


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
