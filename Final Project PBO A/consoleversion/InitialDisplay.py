from TodoListHandle import TodoListHandle
from Registration import Registration
from datetime import date, datetime
from os import system, name, remove
import calendar


class InitialDisplay:

    __signUp = Registration()
    __toDo = TodoListHandle()
    
    def mainMenu(self):

        try:
            # remove file kegiatan.txt sebelumnya (jika ada)
            remove("kegiatan.txt")
        except FileNotFoundError:
            print("", end="")
        finally:
            # jika file tidak ada, maka tidak akan diremove dan hanya akan dibuatkan file baru
            file = open("kegiatan.txt", "w+")
            file.close()

        # melakukan registrasi terlebih dahulu
        self.__clearScreen()
        self.__signUp.registration()
        self.__clearScreen()

        # setelah registrasi berhasil, maka akan muncul tampilan menu awal
        while True:
            self.__initialMenu()
            choice = int(input("> "))

            if choice == 1:
                self.__clearScreen()
                print("+-------------- To-Do-List Today -------------+\n")
                self.__toDo.showList()

            elif choice == 2:
                self.__clearScreen()
                print("+---------------- Adding List ----------------+\n")
                self.__toDo.showList()
                self.__toDo.addList()

            elif choice == 3:
                self.__clearScreen()
                print("+---------------- Delete List ----------------+\n")
                self.__toDo.showList()
                self.__toDo.deleteList()
            elif choice == 4:
                self.__clearScreen()
                print("+----------------- Edit List -----------------+\n")
                self.__toDo.showList()
                self.__toDo.editList()

            elif choice == 5:
                self.__clearScreen()
                print("+------------ Description List ---------------+\n")
                self.__toDo.showList()
                self.__toDo.descriptionList()

            elif choice == 6:
                self.__clearScreen()
                print("+------------------ Biodata ------------------+")
                print(self.__signUp.getBiodata())
                print("+{}+".format("-" * 45))

            elif choice == 0:
                break

            else:
                self.__clearScreen()

    # method clearScreen untuk menghapus screen pada terminal agar tidak penuh
    def __clearScreen(self):
        # for windows
        if name == "nt":
            _ = system("cls")
        # for linux and macOS
        elif name == "posix":
            _ = system("clear")

    # method initialMenu untuk menampilkan tampilan awal pilihan user
    def __initialMenu(self):
        print("\n+---------------- To-Do-List -----------------+")
        print("\nSelamat Datang {} ^_^\n".format(self.__signUp.getCallName()))
        self.__setTime()
        print("1. Lihat To-do-list Harian")
        print("2. Tambahkan kegiatan")
        print("3. Hapus kegiatan")
        print("4. Edit kegiatan")
        print("5. Lihat Deskripsi kegiatan")
        print("6. Lihat Biodata anda")
        print("0. Exit")

    # method setTime berguna untuk menampilkan jam, tanggal, dan hari saat ini.
    def __setTime(self):
        todayDate = date.today().strftime("%d %B %Y")
        timeNow = datetime.now().time().strftime("%H:%M:%S")
        print(
            "Today is {}\nDate : {}\nIt's : {} o'clock\n".format(
                calendar.day_name[date.today().weekday()], todayDate, timeNow
            )
        )
