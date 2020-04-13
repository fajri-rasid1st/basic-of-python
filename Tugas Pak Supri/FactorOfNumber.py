# mengecek faktor dari sebuah bilangan x dan tentukan banyak faktornya
x = int(input("masukkan angka : "))

total_factor = [i for i in range(1, x + 1) if x % i == 0]

print("faktor dari %d adalah :" % x, total_factor)
print("banyak faktor ada :", len(total_factor))
