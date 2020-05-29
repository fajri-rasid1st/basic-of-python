from TodoList import TodoList
from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import tkinter.messagebox


class DescriptionList(tk.Tk, TodoList):
    # method untuk membuat window
    def __init__(self):
        tk.Tk.__init__(self)
        # membuat frame dan memasukkan label dan button kedalamnya
        self.frame_1 = tk.Frame(self, bg="#e6a817")
        self.frame_1.pack(pady=0)

        self.label_1 = Label(
            self.frame_1,
            text="Description List",
            font=("Trebuchet MS", 28, "bold"),
            background="#e6a817",
        ).grid(row=0, pady=25)

        self.label_2 = Label(
            self.frame_1,
            text="Tekan 'esc' untuk keluar",
            font=("Verdana 12 italic"),
            background="#e6a817",
            foreground="red",
        ).grid(row=1, pady=0)

        self.label_3 = Label(
            self.frame_1,
            text=self.showList(),
            font="calibri 11 bold",
            background="#e6a817",
            foreground="#2b2b2b",
        )
        self.label_3.configure(justify=LEFT)
        self.label_3.grid(row=2, pady=15)

        self.label_4 = Label(
            self.frame_1,
            text="Masukkan nomor kegiatan yang ingin dilihat deskripsinya :",
            font="calibri 14 bold",
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=3, pady=10)

        self.entry_desc = Entry(
            self.frame_1,
            width=2,
            font=("Trebuchet MS", 13, "bold"),
            background="#134f5c",
            foreground="white",
            relief=SUNKEN,
            borderwidth=5,
        )
        self.entry_desc.grid(row=4, pady=5)

        self.desc_button = Button(
            self.frame_1,
            text="Lihat",
            font=("calibri", 14, "bold"),
            width=6,
            background="#134f5c",
            foreground="white",
            borderwidth=0,
            relief=RIDGE,
            command=lambda: self.descriptionList(self.onClickAction(), self),
        ).grid(row=5, pady=10)
        # mengatur judul, background, editable, dan menambahkan shortcut esc untuk exit program
        self.__centerWindow(920, 500)
        self.title("Description List")
        self.configure(background="#e6a817")
        self.resizable(0, 0)
        self.bind("<Escape>", lambda event: self.destroy())
        self.mainloop()

    # # method yang mengembalikan isi dari entry dan mengcastingnya ke integer
    def onClickAction(self):
        try:
            return int(self.entry_desc.get())
        except ValueError:
            tkinter.messagebox.showerror(
                "Activity not found", "Masukkan nomor kegiatan dengan benar!"
            )

    # buat window GUI tepat ditengah layar
    def __centerWindow(self, width, height):
        widthScreen = self.winfo_screenwidth()
        heightScreen = self.winfo_screenheight()
        x = (widthScreen / 2) - (width / 2)
        y = (heightScreen / 2) - ((height / 2) + 20)
        return self.geometry("%dx%d+%d+%d" % (width, height, x, y))
