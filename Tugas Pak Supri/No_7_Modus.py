# menentukan modus dalam list
length = int(input("Masukkan total data: "))
print("Masukkan data : ", end="\n")

list_number = [int(input()) for i in range(0, length)]
list_number.sort()

data_modus = []
for i in list(set(list_number.copy())):
    data_modus.append([i, list_number.count(i)])

data = 0
result = []
for i in reversed(sorted(data_modus, key=lambda index: index[1])):
    if i[1] >= data:
        result.append(i[0])
        data = i[1]
print("modus dari data adalah :", sorted(result))
