from tkinter import *


class EndWindow:
    def __init__(self, end):
        self.mark_lbl = Label(end,
                              font=('Times New Roman', 30),
                              )
        self.exit_btn = Button(end,
                               text="EXIT",
                               font=("Times New Roman", 20),
                               background="#ccc",
                               command=end.destroy,
                               )

    def placed(self):
        self.mark_lbl.place(x=347, y=150)
        self.exit_btn.place(x=455, y=210, width=90, bordermode=OUTSIDE)

    def packed(self):
        self.mark_lbl.pack()
        self.exit_btn.pack()

    def delete(self):
        self.mark_lbl.destroy()
        self.exit_btn.destroy()