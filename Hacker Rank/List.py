# Lists

if __name__ == "__main__":
    n = int(input())

    lists = []

    for i in range(n):
        command, *number = input().split(" ")
        parameter = list(map(int, number))
        if command == "insert":
            lists.insert(parameter[0], parameter[1])
        elif command == "print":
            print(lists)
        elif command == "remove":
            lists.remove(parameter[0])
        elif command == "append":
            lists.append(parameter[0])
        elif command == "sort":
            lists.sort()
        elif command == "pop":
            lists.pop()
        else:
            lists.reverse()
