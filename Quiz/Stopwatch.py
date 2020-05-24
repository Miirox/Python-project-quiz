from tkinter import *


class Stopwatch:
    def __init__(self, stopwatch):
        self.time_lbl = Label(stopwatch, text="00:00", font=("Times New Roman", 28, 'bold'))

    def packed(self):
        self.time_lbl.pack()

    def places(self):
        self.time_lbl.place(x=850, y=420)

    def delete(self):
        self.time_lbl.destroy()