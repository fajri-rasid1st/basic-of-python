from TodoList import TodoList
from tkinter.ttk import *
from tkinter import *
import tkinter as tk


class ShowList(tk.Tk, TodoList):
    # method untuk membuat window
    def __init__(self):
        tk.Tk.__init__(self)
        # mengatur node dari window dan memasukkannya kedalam container(frame)
        self.frame_1 = tk.Frame(self, bg="#e6a817")
        self.frame_1.pack(pady=0)

        self.label_1 = Label(
            self.frame_1,
            text="To-do List Today",
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
        # mengatur judul, background, editable, dan menambahkan shortcut esc untuk exit program
        self.__centerWindow(960, 540)
        self.title("To-Do-List")
        self.configure(background="#e6a817")
        self.resizable(0, 0)
        self.bind("<Escape>", lambda event: self.destroy())
        self.mainloop()

    # buat window GUI tepat ditengah layar
    def __centerWindow(self, width, height):
        widthScreen = self.winfo_screenwidth()
        heightScreen = self.winfo_screenheight()
        x = (widthScreen / 2) - (width / 2)
        y = (heightScreen / 2) - ((height / 2) + 20)
        return self.geometry("%dx%d+%d+%d" % (width, height, x, y))
