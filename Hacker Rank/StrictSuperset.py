# Check Strict Superset

# a > b = a.isstrictsuperset(b)
# strict superset has at least one element that does not exist in its subset.

a = set(input().split())
result = all([a > set(input().split()) for i in range(int(input()))])
print(result)

# another solution without all()
# result = [a > set(input().split()) for i in range(int(input()))]
# print(result[len(result) - 1])
