# Merge The tools


def merge_the_tools(string, k):
    y = k
    s_list = []
    index = 0

    for i in range(int(len(string) / k)):
        s_list.append(string[y - k : y])
        y += k

    for j in s_list:
        new_str = ""
        for l in j:
            if l not in new_str:
                new_str += l

        s_list[index] = new_str
        index += 1
        print(new_str)


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
