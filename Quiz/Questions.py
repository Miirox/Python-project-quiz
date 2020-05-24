from tkinter import *


class Questions:
    def __init__(self, quest):
        self.question = Label(quest, font=("Times New Roman", 18), justify='left')
        self.questList = [
            "Physical qualities are:",
            "The basis of human motor abilities are:",
            "The level of development of human motor abilities is determined by:",
            "Physical training is:",
            "Strength is:",
            "Absolute power is:",
            "Relative strength is:",
            "What methods are used to train strength:",
            "The most favorable (sensitive) period of development of strength in boys is age",
            "The most favorable (sensitive) period of strength development in girls is age",
            "The capabilities of a person, providing him with the performance of motor actions\nin the minimum period of time for these conditions, are called: ",
            "Age is considered to be the most favorable period for the development of speed abilities",
            "The ability to withstand physical fatigue during muscle activity is called:",
            "The ability to perform long-term work of moderate intensity in the global functioning\nof the muscular system is called:",
            "One of the main criteria of endurance is:",
            "The most intense increase in endurance is observed with age:",
            "The ability to perform movements with a large amplitude is called:",
            "The ability to perform movements with a large amplitude due to its own activity\nof the corresponding muscles is called:",
            "Passive flexibility means:",
            "The main method of developing flexibility is:",
        ]

    def places(self):
        self.question.place(x=50, y=100)
