x = map(lambda x: str(x).lower(), "FAJRI")

y = [i for i in list(x)]

for i in y:
    print(ord(i))
