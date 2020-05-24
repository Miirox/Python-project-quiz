from tkinter import *


class MainWindow:
    def __init__(self, window):
        self.welcome = Label(window,
                             text="Welcome to the QUIZ!",
                             font=("Times New Roman", 30),
                             bg="#D09CFF"
                             )
        self.start_btn = Button(window,
                                text="START",
                                font=("Times New Roman", 20),
                                background="#E31381",
                                )
        self.rules_btn = Button(window,
                                text="RULES",
                                font=("Times New Roman", 20),
                                background="#E31381",
                                )
        self.exit_btn = Button(window,
                               text="EXIT",
                               font=("Times New Roman", 20),
                               background="#E31381",
                               command=window.destroy,
                               )

    def packed(self):
        self.welcome.pack()
        self.start_btn.pack()
        self.rules_btn.pack()
        self.exit_btn.pack()

    def delete(self):
        self.welcome.destroy()
        self.start_btn.destroy()
        self.rules_btn.destroy()
        self.exit_btn.destroy()

    def places(self):
        self.welcome.place(x=312.5, y=100)
        self.start_btn.place(x=450, y=175, bordermode=OUTSIDE)
        self.rules_btn.place(x=450, y=250, bordermode=OUTSIDE)
        self.exit_btn.place(x=461, y=325, bordermode=OUTSIDE)
