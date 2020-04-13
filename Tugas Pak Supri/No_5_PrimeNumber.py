# mengecek apakah bilangan x adalah prima
x = int(input("masukkan angka : "))

check = [i for i in range(2, x + 1) if x % i == 0]

if len(check) == 1:
    print("%d adalah bilangan prima" % x)
else:
    print("%d bukan bilangan prima" % x)
