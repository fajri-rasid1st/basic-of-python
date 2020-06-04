# alphabet rangoli

import string


def print_rangoli(size):

    letter = list(reversed(list(string.ascii_lowercase[0:size])))
    center_align = ((len(letter) * 2) - 1) + (((len(letter) * 2) - 1) - 1)
    rangoli_list = []

    for i in range(0, size):
        normal_letter = letter[0 : i + 1]
        reverse_letter = list(reversed(normal_letter))
        line = ""
        if len(normal_letter) == 1:
            line += normal_letter[0]
        else:
            for j in range(0, len(normal_letter) + 1):
                if j == len(normal_letter):
                    for k in range(1, len(reverse_letter)):
                        line += reverse_letter[k]
                else:
                    line += normal_letter[j]

        rangoli_list.append("-".join(list(line)).center(center_align, "-"))

    rangoli_list += list(reversed(rangoli_list[0 : size - 1]))

    for i in rangoli_list:
        print(i)


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
