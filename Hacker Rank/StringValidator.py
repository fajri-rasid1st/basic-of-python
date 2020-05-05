# String validator
def check(totalV):
    if totalV != 0:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    s = input()
    totalValidator = 0
    for i in s:
        if i.isalnum():
            totalValidator += 1
    check(totalValidator)
    totalValidator = 0
    for i in s:
        if i.isalpha():
            totalValidator += 1
    check(totalValidator)
    totalValidator = 0
    for i in s:
        if i.isdigit():
            totalValidator += 1
    check(totalValidator)
    totalValidator = 0
    for i in s:
        if i.islower():
            totalValidator += 1
    check(totalValidator)
    totalValidator = 0
    for i in s:
        if i.isupper():
            totalValidator += 1
    check(totalValidator)
