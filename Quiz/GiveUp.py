from tkinter import *


class GiveUp:
    def __init__(self, giveup):
        self.message = Label(giveup, text='You\'ve given up', font=('Times New Roman', 30), fg='red')
        self.mark = Label(giveup, text='Your Mark is: 0', font=('Times New Roman', 30))
        self.exit_btn = Button(giveup,
                               text="EXIT",
                               font=("Times New Roman", 20),
                               background="#ccc",
                               command=giveup.destroy,
                               )

    def packed(self):
        self.message.pack()
        self.mark.pack()
        self.exit_btn.pack()

    def places(self):
        self.message.place(x=360, y=100)
        self.mark.place(x=360, y=160)
        self.exit_btn.place(x=455, y=220, width=90, bordermode=OUTSIDE)

    def delete(self):
        self.message.destroy()
        self.mark.destroy()
        self.exit_btn.destroy()