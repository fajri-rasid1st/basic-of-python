polinom = lambda sources: eval(sources)

x, y = map(int, input().split())

if polinom(input()) == y:
    print(True)
else:
    print(False)
