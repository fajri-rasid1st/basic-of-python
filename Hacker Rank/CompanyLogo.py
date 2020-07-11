from collections import Counter

s_count = Counter(sorted(input(), reverse=False))

for item in list(s_count.most_common(3)):
    print(item[0], item[1])
