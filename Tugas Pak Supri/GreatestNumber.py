# mencetak bilangan terbesar dari sebuah list
length = int(input("Masukkan total data: "))
print("Masukkan data : ", end="\n")

greatestNumber = 0
list_number = [int(input()) for i in range(0, length)]

for i in list_number:
    if i > greatestNumber:
        greatestNumber = i

print("Data :", list_number)
print("Bilangan terbesar adalah :", greatestNumber)
