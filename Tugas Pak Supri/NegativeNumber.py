# mencetak banyak bilangan negatif dari sebuah list
length = int(input("Masukkan total data: "))
print("Masukkan data : ", end="\n")

negative_number = 0
list_number = [int(input()) for i in range(0, length)]

for i in list_number:
    if i < 0:
        negative_number += 1

print("Data :", list_number)
print("Banyak bilangan negatif ada", negative_number)
