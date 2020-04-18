# Find the runner-up score!

n = int(input())
score = [int(i) for i in input().split(" ")]
result = sorted(list(set(score)))
print(result[len(result) - 2])
