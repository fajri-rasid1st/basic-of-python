# The minion game


def minion_game(s):

    # # Solution 1 (Memory error in some testcase)
    # stuart, kevin = 0, 0
    # vowels = "AIUEO"

    # for i in [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]:
    #     if i[0] in vowels:
    #         kevin += 1
    #     else:
    #         stuart += 1

    # if stuart > kevin:
    #     print(f"Stuart {stuart}")
    # elif kevin > stuart:
    #     print(f"Kevin {kevin}")
    # else:
    #     print("Draw")

    # solution 2
    stuart, kevin = 0, 0
    vowels = "AIUEO"

    for i in range(len(s)):
        if s[i] in vowels:
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
