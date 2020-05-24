from tkinter import *


class Toolbar:
    def __init__(self, toolbar):
        self.main_menu = Menu(toolbar)
        self.file_menu = Menu(self.main_menu, tearoff=0)

    def add(self, toolbar):
        self.file_menu.add_command(label="Exit", command=toolbar.destroy)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)


