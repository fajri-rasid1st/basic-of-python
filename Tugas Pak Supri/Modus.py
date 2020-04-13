# menentukan modus dalam list
length = int(input("Masukkan total data: "))
print("Masukkan data : ", end="\n")

list_number = [int(input()) for i in range(0, length)]

modus = 0
data_modus = 0
for i in set(list_number.copy()):
    if list_number.count(i) > data_modus:
        modus = i
        data_modus = list_number.count(i)

print("data setelah diurutkan =", sorted(list_number))
print("modus =", modus)
