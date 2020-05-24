from tkinter import *


class Navigator:
    def __init__(self, navigator):
        self.navTo1 = Label(navigator,
                            text='1',
                            background="#faff8f",
                            foreground="black",
                            padx="20",
                            pady="8",
                            font=('Times New Roman', 16, 'bold'),
                            )
        self.navTo2 = Label(navigator,
                            text='2',
                            background="#faff8f",
                            foreground="black",
                            padx="20",
                            pady="8",
                            font=('Times New Roman', 16, 'bold'),
                            )
        self.navTo3 = Label(navigator,
                            text='3',
                            background="#faff8f",
                            foreground="black",
                            padx="20",
                            pady="8",
                            font=('Times New Roman', 16, 'bold'),
                            )
        self.navTo4 = Label(navigator,
                            text='4',
                            background="#faff8f",
                            foreground="black",
                            padx="20",
                            pady="8",
                            font=('Times New Roman', 16, 'bold'),
                            )
        self.navTo5 = Label(navigator,
                            text='5',
                            background="#faff8f",
                            foreground="black",
                            padx="20",
                            pady="8",
                            font=('Times New Roman', 16, 'bold'),
                            )
        self.navTo6 = Label(navigator,
                            text='6',
                            background="#faff8f",
                            foreground="black",
                            padx="20",
                            pady="8",
                            font=('Times New Roman', 16, 'bold'),
                            )
        self.navTo7 = Label(navigator,
                            text='7',
                            background="#faff8f",
                            foreground="black",
                            padx="20",
                            pady="8",
                            font=('Times New Roman', 16, 'bold'),
                            )
        self.navTo8 = Label(navigator,
                            text='8',
                            background="#faff8f",
                            foreground="black",
                            padx="20",
                            pady="8",
                            font=('Times New Roman', 16, 'bold'),
                            )
        self.navTo9 = Label(navigator,
                            text='9',
                            background="#faff8f",
                            foreground="black",
                            padx="20",
                            pady="8",
                            font=('Times New Roman', 16, 'bold'),
                            )
        self.navTo10 = Label(navigator,
                             text='10',
                             background="#faff8f",
                             foreground="black",
                             padx="20",
                             pady="8",
                             font=('Times New Roman', 16, 'bold'),
                             )

    def places(self):
        self.navTo1.place(x=137.5,
                          y=20,
                          height=50,
                          width=50,
                          )
        self.navTo2.place(x=212.5,
                          y=20,
                          height=50,
                          width=50,
                          )
        self.navTo3.place(x=287.5,
                          y=20,
                          height=50,
                          width=50,
                          )
        self.navTo4.place(x=362.5,
                          y=20,
                          height=50,
                          width=50,
                          )
        self.navTo5.place(x=437.5,
                          y=20,
                          height=50,
                          width=50,
                          )
        self.navTo6.place(x=512.5,
                          y=20,
                          height=50,
                          width=50,
                          )
        self.navTo7.place(x=587.5,
                          y=20,
                          height=50,
                          width=50,
                          )
        self.navTo8.place(x=662.5,
                          y=20,
                          height=50,
                          width=50,
                          )
        self.navTo9.place(x=737.5,
                          y=20,
                          height=50,
                          width=50,
                          )
        self.navTo10.place(x=812.5,
                           y=20,
                           height=50,
                           width=50,
                           )

    def packed(self):
        self.navTo1.pack()
        self.navTo2.pack()
        self.navTo3.pack()
        self.navTo4.pack()
        self.navTo5.pack()
        self.navTo6.pack()
        self.navTo7.pack()
        self.navTo8.pack()
        self.navTo9.pack()
        self.navTo10.pack()

    def delete(self):
        self.navTo1.destroy()
        self.navTo2.destroy()
        self.navTo3.destroy()
        self.navTo4.destroy()
        self.navTo5.destroy()
        self.navTo6.destroy()
        self.navTo7.destroy()
        self.navTo8.destroy()
        self.navTo9.destroy()
        self.navTo10.destroy()