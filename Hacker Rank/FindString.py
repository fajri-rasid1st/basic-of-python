# Find a String
def count_substring(string, sub_string):
    total_substring = 0
    index = 0

    while index < len(string):
        subs = string.find(sub_string, index)
        if subs == -1:
            return total_substring
        else:
            total_substring += 1
        index = subs + 1


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
