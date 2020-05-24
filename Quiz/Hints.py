from tkinter import *


class Hints:
    def __init__(self, hints):
        self.hints_lbl = Label(
            hints,
            text="0",
            bg="#ccc",
            font=("Times New Roman", 16, 'bold'),
        )

    def packed(self):
        self.hints_lbl.pack()

    def places(self):
        self.hints_lbl.place(
            x=30,
            y=420,
            width=90,
            height=50,
        )

    def delete(self):
        self.hints_lbl.destroy()