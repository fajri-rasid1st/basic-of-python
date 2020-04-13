# Mengecek apakah bilangan x terdapat dalam list
from random import randrange as randomNumber

length = int(input("Masukkan total data: "))
list_number = [randomNumber(-50, 50) for i in range(0, length)]
print("Data :", list_number)

x = int(input("masukkan angka yang ingin di cari : "))

if list_number.count(x) != 0:
    print("angka %d ada dalam list pada index ke-%d" % (x, list_number.index(x)))
else:
    print("angka %d tidak ada dalam list" % x)
