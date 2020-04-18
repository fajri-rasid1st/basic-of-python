# Find Median
def median(data):
    if len(data) % 2 == 1:
        return data[(len(data) // 2)]
    else:
        return (data[(len(data) // 2)] + data[(len(data) // 2) - 1]) / 2


# Main class
n = input()
data = [int(i) for i in input().split(" ")]
print(median(sorted(data)))
