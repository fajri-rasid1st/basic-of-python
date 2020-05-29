from TodoList import TodoList


class TodoListHandle(TodoList):
    # implemented
    def showList(self):
        # membuka file.txt dan otomatis akan close file.txt jika perintah selesai
        with open("kegiatan.txt", "r") as openFile:
            # data perbaris akan ditampung disini
            data = openFile.readline().replace("\n", "")
            number = 1
            # membuat tata letak tabel
            print("+{}+".format("-" * 106))
            print(
                "| No. | Nama kegiatan\t\t\t          | Jadwal\t   | Prioritas\t      | Status\t           |"
            )
            print("+{}+".format("-" * 106))
            # jika data pada file.txt kosong, maka akan muncul tampilan seperti ini
            if data.__eq__(""):
                print("|\t\t\t\t      Daftar kegiatan masih kosong!\t\t\t\t\t   |")
            # jika data pada file.txt ada, maka dibuat perulangan untuk membaca seluruh baris
            while not data.__eq__(""):
                dataPerline = data.split(";")
                print("|  %d  " % number, end="")
                print("| %-42s" % dataPerline[0], end="")
                print("| %-15s" % dataPerline[1], end="")
                print("| %-17s" % dataPerline[2], end="")
                print("| %-19s|" % dataPerline[3])
                data = openFile.readline().replace("\n", "")
                number += 1
            print("+{}+".format("-" * 106))

    # implemented
    def addList(self):
        # user menginput keterangan dari kegiatan yang akan ditambahkan
        activityName = input("\nNama kegiatan : ")
        schedule = input("Jadwal        : ")
        self._TodoList__priorityChoice()
        priority = int(input("Prioritas     : "))
        getPriority = self._TodoList__getPriority(priority)
        self._TodoList__statusChoice()
        status = int(input("Status        : "))
        getStatus = self._TodoList__getStatus(status)
        description = input("Deskripsi     : ")
        # menampilkan keterangan kegiatan yang akan ditambahkan
        print("\n+-------- Kegiatan yang akan ditambah --------+\n")
        print(
            "Nama kegiatan : {}\nJadwal        : {}\nPrioritas     : {}\nStatus        : {}\nDeskripsi     : {}".format(
                activityName, schedule, getPriority, getStatus, description
            )
        )
        # menentukan pilihan user saat menambahkan data ke file
        isAdd = self._TodoList__getYesOrNo("Yakin ingin menambahkan kegiatan? (y/n)")
        # membuka file.txt dan otomatis akan close file.txt jika perintah selesai
        with open("kegiatan.txt", "a") as openFile:
            if isAdd:
                # jika user menekan y, maka kegiatan akan ditulis ke file
                openFile.write(
                    "{};{};{};{};{}\n".format(
                        activityName, schedule, getPriority, getStatus, description
                    )
                )
                print("\nBerhasil menambahkan kegiatan!")
            else:
                print("\nTambah kegiatan dibatalkan!")

    # implemented
    def deleteList(self):
        # mengecek terlebih dahulu banyak baris pada file.txt
        totalLines = self._TodoList__checkTotalLineAtFile()
        # jika banyak baris adalah 0, artinya file.txt masih kosong
        if totalLines == 0:
            print("\nDaftar kegiatan masih kosong!")
        while totalLines != 0:
            # user menentukan kegiatan yang akan dihapus
            deleteActivity = int(input("\nMasukkan nomor kegiatan : "))
            if deleteActivity == 0 or deleteActivity > totalLines or 1 > deleteActivity:
                print("\nKegiatan tidak ada")
                break
            else:
                with open("kegiatan.txt", "r") as readFile:
                    # membaca semua baris dan memasukkannya kedalam list
                    lines = readFile.readlines()
                    # menampilkan kegiatan yang akan dihapus
                    lineToDelete = lines[deleteActivity - 1].strip("\n").split(";")
                    print("\n+-------- Kegiatan yang akan dihapus ---------+\n")
                    print(
                        "Nama kegiatan : {}\nJadwal        : {}\nPrioritas     : {}\nStatus        : {}\nDeskripsi     : {}".format(
                            lineToDelete[0],
                            lineToDelete[1],
                            lineToDelete[2],
                            lineToDelete[3],
                            lineToDelete[4],
                        )
                    )
                    # konfirmasi kegiatan yang akan dihapus
                    isDelete = self._TodoList__getYesOrNo(
                        "Yakin ingin menghapus kegiatan? (y/n)"
                    )
                    if isDelete:
                        with open("kegiatan.txt", "w") as writeFile:
                            for line in lines:
                                # jika baris pada file.txt tidak sama dengan baris yang akan dihapus, maka akan ditulis ulang
                                # secara otomatis baris yang sama tidak akan ditulis
                                if line.strip("\n") != lines[deleteActivity - 1].strip(
                                    "\n"
                                ):
                                    writeFile.write(line)
                        print("\nBerhasil menghapus kegiatan!")
                        break
                    else:
                        print("\nMenghapus kegiatan dibatalkan!")
                        break

    # implemented
    def editList(self):
        # mengecek terlebih dahulu banyak baris pada file.txt
        totalLines = self._TodoList__checkTotalLineAtFile()
        # jika banyak baris adalah 0, artinya file.txt masih kosong
        if totalLines == 0:
            print("\nDaftar kegiatan masih kosong!")
        while totalLines != 0:
            # user menentukan kegiatan yang akan diedit
            editActivity = int(input("\nMasukkan nomor kegiatan : "))
            if editActivity == 0 or editActivity > totalLines or 1 > editActivity:
                print("\nKegiatan tidak ada")
                break
            else:
                # membuka file.txt dan otomatis akan close file.txt jika perintah selesai
                with open("kegiatan.txt", "r") as readFile:
                    # membaca semua baris dan memasukkannya kedalam list
                    lines = readFile.readlines()
                    # menampilkan kegiatan yang akan diedit
                    lineToEdit = lines[editActivity - 1].strip("\n").split(";")
                    print("\n+--------- Kegiatan yang akan diedit ---------+\n")
                    print(
                        "Nama kegiatan : {}\nJadwal        : {}\nPrioritas     : {}\nStatus        : {}\nDeskripsi     : {}".format(
                            lineToEdit[0],
                            lineToEdit[1],
                            lineToEdit[2],
                            lineToEdit[3],
                            lineToEdit[4],
                        )
                    )
                    # buat list untuk edit keterangan kegiatan
                    field = ["nama", "jadwal", "prioritas", "status", "deskripsi"]
                    dataField = lineToEdit.copy()
                    # kegiatan hasil edit akan ditampung disini
                    newField = []
                    # buat perulangan untuk mengedit tiap field
                    for i in range(0, 5):
                        isEdit = self._TodoList__getYesOrNo(
                            "Ubah {} kegiatan? (y/n)".format(field[i])
                        )
                        if isEdit:
                            # jika user menekan y, maka user harus menginput kegiatan yang baru
                            print(
                                "masukkan {} kegiatan baru : ".format(field[i]), end=""
                            )
                            if i == 2:
                                print()
                                self._TodoList__priorityChoice()
                                newField.append(
                                    self._TodoList__getPriority(int(input("> ")))
                                )
                            elif i == 3:
                                print()
                                self._TodoList__statusChoice()
                                newField.append(
                                    self._TodoList__getStatus(int(input("> ")))
                                )
                            else:
                                newField.append(input())
                        else:
                            # jika user menekan n, kegiatan sebelumnya akan di masukkan ke newField
                            newField.append(dataField[i])
                    # menampilkan data yang telah diedit
                    print("\n+------------ Kegiatan baru anda -------------+")
                    print("Nama kegiatan : {} --> {}".format(dataField[0], newField[0]))
                    print("Jadwal        : {} --> {}".format(dataField[1], newField[1]))
                    print("Prioritas     : {} --> {}".format(dataField[2], newField[2]))
                    print("Status        : {} --> {}".format(dataField[3], newField[3]))
                    print("Deskripsi     : {} --> {}".format(dataField[4], newField[4]))
                    # konfirmasi apakah data ingin diedit atau tidak
                    confirmEdit = self._TodoList__getYesOrNo(
                        "Tekan 'y' untuk lanjut dan tekan 'n' untuk membatalkan"
                    )
                    if confirmEdit:
                        with open("kegiatan.txt", "w") as writeFile:
                            for line in lines:
                                if line.strip("\n") == lines[editActivity - 1].strip(
                                    "\n"
                                ):
                                    # jika user setuju mengedit file, maka newField akan di write pada file
                                    writeFile.write(
                                        "{};{};{};{};{}\n".format(
                                            newField[0],
                                            newField[1],
                                            newField[2],
                                            newField[3],
                                            newField[4],
                                        )
                                    )
                                else:
                                    # sedangkan data pada baris yang lain akan tetap ditulis ulang
                                    writeFile.write(line)
                        print("\nBerhasil mengedit kegiatan!")
                        break
                    else:
                        print("\nEdit kegiatan dibatalkan")
                        break

    # implemented
    def descriptionList(self):
        # mengecek terlebih dahulu banyak baris pada file
        totalLines = self._TodoList__checkTotalLineAtFile()
        # jika baris pada file.txt kosong, maka akan muncul tampilan berikut
        if totalLines == 0:
            print("\nDaftar kegiatan masih kosong!")
        while totalLines != 0:
            # cek kegiatan nomor berapa yang ingin dilihat deskripsinya
            print("\nTekan 0 untuk kembali ke menu utama")
            desc = int(input("Masukkan nomor kegiatan : "))
            # cek apakah nomor yang dipilih ada pada baris yang ada di database
            if desc == 0:
                break
            elif desc > totalLines or 1 > desc:
                print("\nKegiatan tidak ada")
            else:
                with open("kegiatan.txt", "r") as openFile:
                    data = openFile.readline().replace("\n", "")
                    currentEntry = 0
                    # jika pilihan baris user sudah benar, maka akan di cek satu-satu baris yang sesuai
                    while not data.__eq__(""):
                        currentEntry += 1
                        dataPerLine = data.split(";")
                        # jika nilai pilihan user sudah sama dengan current entry, maka akan ditampilkan deskripsinya
                        if desc == currentEntry:
                            print("\nNama kegiatan : {}".format(dataPerLine[0]))
                            print("Deskripsi     : {}".format(dataPerLine[4]))
                        # membaca kembali baris selanjutnya
                        data = openFile.readline().replace("\n", "")
