# NestedList

n = int(input())

ranking = []

for i in range(n):
    name = input()
    score = float(input())
    ranking.append([name, score])

for j in range(0, 2):
    ranking = sorted(ranking, key=lambda index: index[j])

value = []
for k in ranking:
    value.append(k[1])

second_lowest = ranking[value.count(value[0])][1]

for l in ranking:
    if l[1] == second_lowest:
        print(l[0])
