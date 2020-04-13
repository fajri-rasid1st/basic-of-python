# mencari 3 terbesar dari nilai siswa
n = int(input("masukkan banyak siswa: "))
print("masukkan nama<spasi>nilai :", end="\n")

ranking = []

for i in range(0, n):
    student = input().split(" ")
    ranking.append([student[0], int(student[1])])

print(15 * "-", "Hasil", 15 * "-")

a = 0
for i in reversed(sorted(ranking, key=lambda index: index[1])):
    if a == 3:
        break
    print(f"{a+1}. {i[0]} dengan nilai {i[1]}")
    a += 1
