from Biodata import Biodata
from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import tkinter.messagebox


class Registration(tk.Tk):

    __biodata = ""
    __callName = ""
    __condition = 0

    def __init__(self):
        # method untuk membuat window
        tk.Tk.__init__(self)
        # buat node-node dan memasukkannya ke dalam frame
        self.frame_1 = tk.Frame(self, bg="#e6a817")
        self.frame_1.pack(pady=20)

        self.title_1 = Label(
            self.frame_1,
            text="To-do List Application",
            font="calibri 20 bold",
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=0, column=0, pady=0)

        self.title_2 = Label(
            self.frame_1,
            text="Registration",
            font=("Trebuchet MS", 28, "bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=1, column=0, pady=0)

        self.title_3 = Label(
            self.frame_1,
            text="Anda harus registrasi terlebih dahulu\nsebelum dapat melihat To-Do List",
            font=("comic sans MS", 13),
            background="#e6a817",
            foreground="#2b2b2b",
        )
        self.title_3.configure(justify=CENTER)
        self.title_3.grid(row=2, column=0, pady=0)

        self.title_4 = Label(
            self.frame_1,
            text="Note: Hasanuddin university college only\nTekan 'esc' untuk keluar",
            font=("Verdana 10 italic"),
            background="#e6a817",
            foreground="red",
        )
        self.title_4.configure(justify=CENTER)
        self.title_4.grid(row=3, column=0, pady=0)

        # buat Entry dan Label untuk megisi data user
        self.frame_2 = tk.Frame(self, bg="#e6a817", width=325, height=275)
        self.frame_2.pack()

        self.name = Label(
            self.frame_2,
            text="Nama                   :",
            font=("calibri 12 bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=0, pady=3, sticky=W)

        self.entry_name = Entry(
            self.frame_2,
            width=25,
            font=("Trebuchet MS", 10, "bold"),
            background="#ebebeb",
            foreground="#2b2b2b",
            relief=FLAT,
        )
        self.entry_name.grid(row=0, column=1, padx=10, pady=3)

        self.callName = Label(
            self.frame_2,
            text="Nama panggilan :",
            font=("calibri 12 bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=1, pady=3, sticky=W)

        self.entry_callName = Entry(
            self.frame_2,
            width=25,
            font=("Trebuchet MS", 10, "bold"),
            background="#ebebeb",
            foreground="#2b2b2b",
            relief=FLAT,
        )
        self.entry_callName.grid(row=1, column=1, padx=10, pady=3)

        self.born = Label(
            self.frame_2,
            text="Tangga lahir        :",
            font=("calibri 12 bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=2, pady=3, sticky=W)

        self.entry_born = Entry(
            self.frame_2,
            width=25,
            font=("Trebuchet MS", 10, "bold"),
            background="#ebebeb",
            foreground="#2b2b2b",
            relief=FLAT,
        )
        self.entry_born.grid(row=2, column=1, padx=10, pady=3)

        self.nim = Label(
            self.frame_2,
            text="NIM                      :",
            font=("calibri 12 bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=3, pady=3, sticky=W)

        self.entry_nim = Entry(
            self.frame_2,
            width=25,
            font=("Trebuchet MS", 10, "bold"),
            background="#ebebeb",
            foreground="#2b2b2b",
            relief=FLAT,
        )
        self.entry_nim.grid(row=3, column=1, padx=10, pady=3)

        self.submit_button = Button(
            self.frame_2,
            text="Daftar",
            font=("calibri", 14, "bold"),
            width=15,
            background="#134f5c",
            foreground="white",
            borderwidth=0,
            command=self.registrationProccess,
        ).grid(columnspan=2, pady=30)
        # mengatur judul, background, editable, dan menambahkan shortcut esc untuk exit program
        self.centerWindow(400, 475)
        self.title("Registration")
        self.configure(background="#e6a817")
        self.overrideredirect(True)
        self.resizable(0, 0)
        self.bind("<Escape>", lambda event: self.destroy())
        self.mainloop()

    # button untuk mengambil inputan user
    def onButton(self):
        return "{};{};{};{}".format(
            self.entry_name.get(),
            self.entry_callName.get(),
            self.entry_born.get(),
            self.entry_nim.get(),
        )

    # buat window GUI tepat ditengah layar
    def centerWindow(self, width, height):
        widthScreen = self.winfo_screenwidth()
        heightScreen = self.winfo_screenheight()
        x = (widthScreen / 2) - (width / 2)
        y = (heightScreen / 2) - ((height / 2) + 55)
        return self.geometry("%dx%d+%d+%d" % (width, height, x, y))

    def getBiodata(self):
        return self.__biodata

    def getCallName(self):
        return self.__callName

    def getCondition(self):
        return self.__condition

    # proses registrasi
    def registrationProccess(self):
        # meletakkan daftar kode setiap fakultas
        facultyDict = {
            "A": "Kedokteran",
            "B": "Farmasi",
            "C": "Teknik",
            "D": "Kehutanan",
            "E": "Pertanian",
            "F": "Keperawatan",
            "G": "Kesehatan Masyarakat",
            "H": "MIPA",
        }

        userInput = self.onButton().split(";")
        # menginstansiasi object biodata
        bio = Biodata(userInput[0], userInput[1], userInput[2], userInput[3])
        # mengecek apakah inputan tanggal lahir sudah sesuai
        try:
            bio.setAge(userInput[2])
        except Exception:
            tkinter.messagebox.showerror(
                "Registration failed",
                "Format tanggal lahir salah (gunakan format dd/mm/yyyy)!",
            )
        finally:
            # mengecek apakah inputan NIM sudah sesuai
            try:
                bio.setRegisterYear(userInput[3])
            except ValueError:
                tkinter.messagebox.showerror(
                    "registration failed", "Format NIM salah!",
                )

        bio.setFaculty(facultyDict)
        bio.setEmail(userInput[0])

        # jika NIM yang diinput tidak ada dalam daftar dictionary di atas, maka:
        if bio.getFaculty() is None:
            tkinter.messagebox.showerror(
                "Registration failed", "NIM anda tidak ada dalam daftar!"
            )
        elif bio.getFaculty is not None and not bio.getAge().__eq__(""):
            self.__condition += 1
            self.__biodata = bio.info()
            self.__callName = bio.callName
            tkinter.messagebox.showinfo(
                "Registration successfull", "Proses registrasi berhasil!",
            )
            self.destroy()
