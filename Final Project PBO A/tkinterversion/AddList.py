from TodoList import TodoList
from tkinter.ttk import *
from tkinter import *
import tkinter as tk


class AddList(tk.Tk, TodoList):
    # method untuk membuat window
    def __init__(self):
        tk.Tk.__init__(self)
        # setting frame untuk node
        self.frame_1 = tk.Frame(self, bg="#e6a817")
        self.frame_1.pack(pady=0)
        # setting label(title)
        self.label_1 = Label(
            self.frame_1,
            text="Adding List",
            font=("Trebuchet MS", 28, "bold"),
            background="#e6a817",
        ).grid(row=0, pady=20)

        self.label_2 = Label(
            self.frame_1,
            text="Tekan 'esc' untuk keluar",
            font=("Verdana 12 italic"),
            background="#e6a817",
            foreground="red",
        ).grid(row=1, pady=0)

        # buat Entry dan Label untuk megisi kegiatan
        self.frame_2 = tk.Frame(self, bg="#e6a817", width=325, height=275)
        self.frame_2.pack(pady=15)

        self.name = Label(
            self.frame_2,
            text="Nama kegiatan       :",
            font=("calibri 12 bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=0, pady=3, sticky=W)

        self.entry_name = Entry(
            self.frame_2,
            width=25,
            font=("Trebuchet MS", 10, "bold"),
            background="#134f5c",
            foreground="white",
            relief=SUNKEN,
            borderwidth=3,
        )
        self.entry_name.grid(row=0, column=1, padx=10, pady=3)

        self.schedule = Label(
            self.frame_2,
            text="Jadwal kegiatan      :",
            font=("calibri 12 bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=1, pady=3, sticky=W)

        self.entry_schedule = Entry(
            self.frame_2,
            width=25,
            font=("Trebuchet MS", 10, "bold"),
            background="#134f5c",
            foreground="white",
            relief=SUNKEN,
            borderwidth=3,
        )
        self.entry_schedule.grid(row=1, column=1, padx=10, pady=3)

        self.priority = Label(
            self.frame_2,
            text="Prioritas kegiatan   :",
            font=("calibri 12 bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=2, pady=3, sticky=W)

        self.entry_priority = Entry(
            self.frame_2,
            width=25,
            font=("Trebuchet MS", 10, "bold"),
            background="#134f5c",
            foreground="white",
            relief=SUNKEN,
            borderwidth=3,
        )
        self.entry_priority.grid(row=2, column=1, padx=10, pady=3)

        self.status = Label(
            self.frame_2,
            text="Status kegiatan       :",
            font=("calibri 12 bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=3, pady=3, sticky=W)

        self.entry_status = Entry(
            self.frame_2,
            width=25,
            font=("Trebuchet MS", 10, "bold"),
            background="#134f5c",
            foreground="white",
            relief=SUNKEN,
            borderwidth=3,
        )
        self.entry_status.grid(row=3, column=1, padx=10, pady=3)

        self.description = Label(
            self.frame_2,
            text="Deskripsi kegiatan  :",
            font=("calibri 12 bold"),
            background="#e6a817",
            foreground="#2b2b2b",
        ).grid(row=4, pady=3, sticky=W)

        self.entry_description = Entry(
            self.frame_2,
            width=25,
            font=("Trebuchet MS", 10, "bold"),
            background="#134f5c",
            foreground="white",
            relief=SUNKEN,
            borderwidth=3,
        )
        self.entry_description.grid(row=4, column=1, padx=10, pady=3)
        # buat button submit
        self.submit_button = Button(
            self.frame_2,
            text="Daftarkan kegiatan",
            font=("calibri", 14, "bold"),
            width=18,
            background="#134f5c",
            foreground="white",
            borderwidth=0,
            relief=RAISED,
            command=lambda: self.addList(
                self.entry_name.get(),
                self.entry_schedule.get(),
                self.entry_priority.get(),
                self.entry_status.get(),
                self.entry_description.get(),
                self,
            ),
        ).grid(columnspan=2, pady=50)
        # mengatur judul, background, editable, dan menambahkan shortcut esc untuk exit program
        self.__centerWindow(400, 450)
        self.title("Add List")
        self.configure(background="#e6a817")
        self.resizable(0, 0)
        self.bind("<Escape>", lambda event: self.destroy())
        self.mainloop()

    # buat window GUI tepat ditengah layar laptop
    def __centerWindow(self, width, height):
        widthScreen = self.winfo_screenwidth()
        heightScreen = self.winfo_screenheight()
        x = (widthScreen / 2) - (width / 2)
        y = (heightScreen / 2) - ((height / 2) + 20)
        return self.geometry("%dx%d+%d+%d" % (width, height, x, y))
