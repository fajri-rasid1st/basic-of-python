# Mod DivMod

x, y = int(input()), int(input())
print("{a}\n{b}\n{c}".format(a=x // y, b=x % y, c=x.__divmod__(y)))
