import tkinter.messagebox


class TodoList:
    def showList(self):
        data_txt = ""
        # membuka file.txt dan otomatis akan close file.txt jika perintah selesai
        with open("kegiatan.txt", "r") as openFile:
            # data perbaris akan ditampung disini
            data = openFile.readline().replace("\n", "")
            number = 1
            # membuat tata letak tabel
            data_txt += "+{}+\n".format("-" * 150)
            data_txt += "| No. | Nama kegiatan\t\t\t\t  | Jadwal\t\t | Prioritas\t  | Status\t\t          |\n"
            data_txt += "+{}+\n".format("-" * 150)
            # jika data pada file.txt kosong, maka akan muncul tampilan seperti ini
            if data.__eq__(""):
                data_txt += "|\t\t\t\t\t       Daftar kegiatan masih kosong!\t\t\t\t\t         |\n"
            # jika data pada file.txt ada, maka dibuat perulangan untuk membaca seluruh baris
            while not data.__eq__(""):
                dataPerline = data.split(";")
                data_txt += "|  %d   " % number
                data_txt += "| %-72s" % dataPerline[0]
                data_txt += "| %-39s" % dataPerline[1]
                data_txt += "| %-26s" % dataPerline[2]
                data_txt += "| %-22s|\n" % dataPerline[3]
                data = openFile.readline().replace("\n", "")
                number += 1
            data_txt += "+{}+\n".format("-" * 150)
            return data_txt

    def addList(
        self, activityName, schedule, getPriority, getStatus, description, master
    ):
        # membuka file.txt dan otomatis akan close file.txt jika perintah selesai
        with open("kegiatan.txt", "a") as openFile:
            openFile.write(
                "{};{};{};{};{}\n".format(
                    activityName, schedule, getPriority, getStatus, description
                )
            )
            tkinter.messagebox.showinfo(
                "Proccess successfull", "Berhasil menambahkan kegiatan!",
            )
            master.destroy()

    def deleteList(self, delete, master):
        # mengecek terlebih dahulu banyak baris pada file.txt
        totalLines = self.__checkTotalLineAtFile()
        # jika banyak baris adalah 0, artinya file.txt masih kosong
        if totalLines == 0:
            tkinter.messagebox.showerror("Empty file", "Daftar kegiatan masih kosong!")
            master.destroy()
        else:
            # user menentukan kegiatan yang akan dihapus
            if delete == 0 or delete > totalLines or 1 > delete:
                tkinter.messagebox.showerror(
                    "Activity not found", "Kegiatan yang dipilih tidak ada"
                )
            else:
                with open("kegiatan.txt", "r") as readFile:
                    # membaca semua baris dan memasukkannya kedalam list
                    lines = readFile.readlines()
                    # menampilkan kegiatan yang akan dihapus
                    with open("kegiatan.txt", "w") as writeFile:
                        for line in lines:
                            # jika baris pada file.txt tidak sama dengan baris yang akan dihapus, maka akan ditulis ulang
                            # secara otomatis baris yang sama tidak akan ditulis
                            if line.strip("\n") != lines[delete - 1].strip("\n"):
                                writeFile.write(line)
                        tkinter.messagebox.showinfo(
                            "Proccess Successfull", "Berhasil menghapus kegiatan"
                        )
                        master.destroy()

    def descriptionList(self, desc, master):
        # mengecek terlebih dahulu banyak baris pada file
        totalLines = self.__checkTotalLineAtFile()
        # jika baris pada file.txt kosong, maka akan muncul tampilan berikut
        if totalLines == 0:
            tkinter.messagebox.showerror("Empty file", "Daftar kegiatan masih kosong!")
            master.destroy()
        else:
            # cek apakah nomor yang dipilih ada pada baris yang ada di database
            if desc > totalLines or 1 > desc or desc == 0:
                tkinter.messagebox.showerror(
                    "Activity not found", "Kegiatan yang dipilih tidak ada"
                )
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
                            tkinter.messagebox.showinfo(
                                "Activity description",
                                "Nama kegiatan : {}\nDeskripsi        : {}".format(
                                    dataPerLine[0], dataPerLine[4]
                                ),
                            )
                        # membaca kembali baris selanjutnya
                        data = openFile.readline().replace("\n", "")

    # method yang digunakan untuk mengecek baris pada file.txt (baris dgn string "" tidak dihitung)
    @classmethod
    def __checkTotalLineAtFile(cls):
        totalLines = 0
        with open("kegiatan.txt", "r") as openFile:
            for line in openFile:
                if not line.__eq__(""):
                    totalLines += 1
        return totalLines
