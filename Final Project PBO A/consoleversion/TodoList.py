from abc import ABC, abstractmethod

# membuat abstract class yg diinherit dari Abstract Base Class
# method pada class ini akan diimplementasikan pada subclass
class TodoList(ABC):
    @abstractmethod
    def showList(self):
        raise NotImplementedError

    @abstractmethod
    def addList(self):
        raise NotImplementedError

    @abstractmethod
    def deleteList(self):
        raise NotImplementedError

    @abstractmethod
    def editList(self):
        raise NotImplementedError

    @abstractmethod
    def descriptionList(self):
        raise NotImplementedError

    @classmethod
    # method ini diguanakan untuk menampilkan opsi yes atau no
    def __getYesOrNo(cls, message):
        print("\n{}".format(message))
        choice = input("> ")
        if choice.__eq__("y"):
            return True
        else:
            return False

    # method ini digunakan untuk mengambil nilai dari pilihan prioritas kegiatan
    @classmethod
    def __getPriority(cls, priority):
        if priority == 1:
            return "Sangat penting"
        elif priority == 2:
            return "Penting"
        elif priority == 3:
            return "Kurang penting"
        else:
            return "-"

    # method ini digunakan untuk mengambil nilai dari pilihan status kegiatan
    @classmethod
    def __getStatus(cls, status):
        if status == 1:
            return "Selesai"
        elif status == 2:
            return "Sedang dikerjakan"
        elif status == 3:
            return "Belum dikerjakan"
        else:
            return "-"

    # method ini digunakan untuk menampilkan pilihan prioritas kegiatan
    @classmethod
    def __priorityChoice(cls):
        print("1. sangat penting")
        print("2. penting")
        print("3. kurang penting")

    # method ini digunakan untuk menampilkan pilihan status kegiatan
    @classmethod
    def __statusChoice(cls):
        print("1. selesai")
        print("2. sedang dikerjakan")
        print("3. belum dikerjakan")

    # method yang digunakan untuk mengecek baris pada file.txt (baris dgn string "" tidak dihitung)
    @classmethod
    def __checkTotalLineAtFile(cls):
        totalLines = 0
        with open("kegiatan.txt", "r") as openFile:
            for line in openFile:
                if not line.__eq__(""):
                    totalLines += 1
        return totalLines
