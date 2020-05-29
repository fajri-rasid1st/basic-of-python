from Registration import Registration
from ShowList import ShowList
from AddList import AddList
from DeleteList import DeleteList
from DescriptionList import DescriptionList
from tkinter.ttk import *
from tkinter import *
from datetime import date, datetime
from os import remove, system, name
import tkinter as tk
import calendar


class InitialDisplay:
    # registrasi terlebih dahulu
    __signUp = Registration()
    __toDo = Tk()

    # main menu
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
        # jika proses registrasi berhasil, maka method initial menu berjalan
        if self.__signUp.getCondition() == 1:
            self.__initialMenu(self.__toDo)

    # method initialMenu untuk menampilkan tampilan awal pilihan user
    def __initialMenu(self, master):
        photo_1 = PhotoImage(file="title_1.png")

        label_1 = Label(master, image=photo_1, background="#134f5c").pack(pady=0)

        label_2 = Label(
            master,
            text="Tekan 'esc' untuk keluar dari aplikasi",
            font=("calibri 14 bold"),
            background="#134f5c",
            foreground="red",
        ).pack(pady=0)

        label_3 = Label(
            master,
            text="Selamat datang {} ^_^\n{}".format(
                self.__signUp.getCallName(), self.__setTime()
            ),
            font=("Trebuchet MS", 13, "bold"),
            background="#134f5c",
            foreground="white",
        ).pack(pady=0)

        main_frame = tk.Frame(master, bg="#134f5c")
        main_frame.configure(width=100, height=100)
        main_frame.pack(pady=0)

        # button untuk melihat kegiatan
        button_choice_1 = Button(
            main_frame,
            text="Lihat To-Do List",
            font=("arial", 13, "bold"),
            width=15,
            background="#e6a817",
            foreground="#2b2b2b",
            borderwidth=3,
            relief=GROOVE,
            command=lambda: ShowList(),
        ).grid(row=0, pady=5)

        # button untuk menambahkan kegiatan
        button_choice_2 = Button(
            main_frame,
            text="Tambah kegiatan",
            font=("arial", 13, "bold"),
            width=15,
            background="#e6a817",
            foreground="#2b2b2b",
            borderwidth=3,
            relief=GROOVE,
            command=lambda: AddList(),
        ).grid(row=0, column=1, pady=10, padx=25)

        # button untuk menghapus kegiatan
        button_choice_3 = Button(
            main_frame,
            text="Hapus kegiatan",
            font=("arial", 13, "bold"),
            width=15,
            background="#e6a817",
            foreground="#2b2b2b",
            borderwidth=3,
            relief=GROOVE,
            command=lambda: DeleteList(),
        ).grid(row=1, pady=5)

        # button untuk melihat deskripsi
        button_choice_4 = Button(
            main_frame,
            text="Lihat deskripsi",
            font=("arial", 13, "bold"),
            width=15,
            background="#e6a817",
            foreground="#2b2b2b",
            borderwidth=3,
            relief=GROOVE,
            command=lambda: DescriptionList(),
        ).grid(row=1, column=1, pady=10, padx=25)

        label_bio = Label(
            main_frame,
            text="Biodata Anda",
            font=("arial", 13, "bold"),
            background="#134f5c",
            foreground="white",
        ).grid(row=2, pady=5, columnspan=2)

        # menampilkan biodata user
        biodataUser = self.biodata(main_frame)
        # mengatur judul, background, editable, dan menambahkan shortcut esc untuk exit program
        self.__centerWindow(master, 840, 680)
        master.title("To-Do-List Application")
        master.configure(background="#134f5c")
        master.overrideredirect(True)
        master.resizable(0, 0)
        master.bind("<Escape>", lambda event: master.destroy())
        master.mainloop()

    # buat window GUI tepat ditengah layar
    def __centerWindow(self, master, width, height):
        widthScreen = master.winfo_screenwidth()
        heightScreen = master.winfo_screenheight()
        x = (widthScreen / 2) - (width / 2)
        y = (heightScreen / 2) - ((height / 2) + 20)
        return master.geometry("%dx%d+%d+%d" % (width, height, x, y))

    # method setTime berguna untuk menampilkan jam, tanggal, dan hari saat ini.
    def __setTime(self):
        todayDate = date.today().strftime("%d %B %Y")
        timeNow = datetime.now().time().strftime("%H:%M:%S")
        return "Today is {}\nDate : {}\nIt's : {} o'clock\n".format(
            calendar.day_name[date.today().weekday()], todayDate, timeNow
        )

    # tampilan label biodata user
    def biodata(self, frame):
        biodata = Label(
            frame,
            text="{}\n{}\n{}".format(
                "+" + (len(self.__signUp.getBiodata().split("\n")[7]) + 10) * "-" + "+",
                self.__signUp.getBiodata(),
                "+" + (len(self.__signUp.getBiodata().split("\n")[7]) + 10) * "-" + "+",
            ),
            font=("calibri", 12, "bold"),
            background="#134f5c",
            foreground="white",
        )
        biodata.configure(justify=LEFT)
        biodata.grid(row=4, columnspan=2, pady=0)
        return biodata
