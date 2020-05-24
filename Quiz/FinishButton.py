from tkinter import *


class FinishButton:
    def __init__(self, finish):
        self.end_btn = Button(
            finish,
            text="GIVE UP",
            bg="#008080",
            font=("Times New Roman", 16, 'bold'),
        )

    def packed(self):
        self.end_btn.pack()

    def places(self):
        self.end_btn.place(
            x=395,
            y=420,
            width=210,
            height=50,
        )

    def delete(self):
        self.end_btn.destroy()