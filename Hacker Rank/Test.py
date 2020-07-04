x = map(lambda x: str(x).lower(), input())
y = [ord(i) for i in list(x) if ord(i) % 2 == 0]
