from tkinter import *


class Answers:
    def __init__(self, answers):
        self.ansList = [
            ["a set of different manifestations of man in a certain motor activity", "a set of abilities of a person engaged in physical culture and sports, which are expressed in concrete results", "!individual features that determine the level of motor abilities of a person", "a set of skills and abilities that allow you to quickly and easily learn motor movements of varying complexity"],
            ["motor skills", "motor skills", "psycho-physical abilities", "!physical qualities"],
            ["!tests (control standards)", "individual reaction of the organism to the load", "the reaction of the respiratory and cardiovascular systems of the body to the load", "bit standards of a single sports classification"],
            ["strategy development process", "!the process of educating physical qualities and mastering vital movements", "knowledge system", "tactics of the game"],
            ["!a person's ability to overcome external resistance or resist it through their muscular efforts", "the ability of a person to show muscular effort of various sizes in the shortest possible time", "ability to show great muscular effort", "a person's ability to exert muscular effort for a long time"],
            ["human ability to overcome external resistance", "manifestation of maximum muscle tension in the static mode of muscle work", "the force shown by a person in terms of 1 kg of body weight", "!the maximum strength of a person that he is able to show regardless of his body weight"],
            ["the strength of a person compared to the strength of another person", "!the force shown by a person in terms of 1 kg of body weight", "force per 1 cm 2 of physiological diameter of a person", "the maximum strength of a person that he is able to show, regardless of his body weight"],
            ["circular method", "interval method", "!method of dynamic, maximum, repeated efforts", "there is no correct answer"],
            ["!from 13-14 to 17-18 years", "11-12 years", "from 17-18 to 19-20 years", "12-13 years"],
            ["from 17-18 to 19-20 years", "!from 11-12 to 15-16 years", "from 13-14 to 17-18 years", "from 15-16 to 17-18 years"],
            ["speed and power abilities", "frequency of movements", "!speed abilities", "motor reaction"],
            ["from 14 to 16 years", "from 16 to 18 years", "after 20 years", "!from 11-12 to 14-15 years"],
            ["!endurance", "by force", "functional stability", "fitness"],
            ["physical fatigue", "!overall endurance", "physical fitness", "physical efficiency"],
            ["!the time during which muscle activity of a certain nature and intensity is performed", "endurance factor", "maximum oxygen consumption", "heart rate"],
            ["from 20 to 25 years", "after 25 years", "from 10 to 14 years", "!from 14 to 20 years"],
            ["elasticity", "!flexibility", "stretching", "there is no correct answer"],
            ["mobility in the joints", "dynamic flexibility", "!active flexibility", "passive flexibility"],
            ["!ability to perform movements under the influence of external forces", "flexibility manifested in dynamic exercises", "flexibility manifested in static poses", "flexibility, which is manifested under the influence of fatigue"],
            ["static force method", "!repeated method", "maximum effort method", "method of alternating continuous exercise"]
        ]

        self.correctAnswers = [
            "!individual features that determine the level of motor abilities of a person",
            "!physical qualities",
            "!tests (control standards)",
            "!the process of educating physical qualities and mastering vital movements",
            "!a person's ability to overcome external resistance or resist it through their muscular efforts",
            "!the maximum strength of a person that he is able to show regardless of his body weight",
            "!the force shown by a person in terms of 1 kg of body weight",
            "!method of dynamic, maximum, repeated efforts",
            "!from 13-14 to 17-18 years",
            "!from 11-12 to 15-16 years",
            "!speed abilities",
            "!from 11-12 to 14-15 years",
            "!endurance",
            "!overall endurance",
            "!the time during which muscle activity of a certain nature and intensity is performed",
            "!from 14 to 20 years",
            "!flexibility",
            "!active flexibility",
            "!ability to perform movements under the influence of external forces",
            "!repeated method"
        ]

        self.ans_btn1 = Button(answers, background="#ccc")
        self.ans_btn2 = Button(answers, background="#ccc")
        self.ans_btn3 = Button(answers, background="#ccc")
        self.ans_btn4 = Button(answers, background="#ccc")

        self.ans_lbl1 = Label(answers, font=("Times New Roman", 16))
        self.ans_lbl2 = Label(answers, font=("Times New Roman", 16))
        self.ans_lbl3 = Label(answers, font=("Times New Roman", 16))
        self.ans_lbl4 = Label(answers, font=("Times New Roman", 16))

    def places(self):
        self.ans_btn1.place(x=30, y=170, width=30, height=30)
        self.ans_btn2.place(x=30, y=220, width=30, height=30)
        self.ans_btn3.place(x=30, y=270, width=30, height=30)
        self.ans_btn4.place(x=30, y=320, width=30, height=30)

        self.ans_lbl1.place(x=80, y=170)
        self.ans_lbl2.place(x=80, y=220)
        self.ans_lbl3.place(x=80, y=270)
        self.ans_lbl4.place(x=80, y=320)

    def packed(self):
        self.ans_btn1.pack()
        self.ans_btn2.pack()
        self.ans_btn3.pack()
        self.ans_btn4.pack()

        self.ans_lbl1.pack()
        self.ans_lbl2.pack()
        self.ans_lbl3.pack()
        self.ans_lbl4.pack()

    def delete(self):
        self.ans_btn1.destroy()
        self.ans_btn2.destroy()
        self.ans_btn3.destroy()
        self.ans_btn4.destroy()

        self.ans_lbl1.destroy()
        self.ans_lbl2.destroy()
        self.ans_lbl3.destroy()
        self.ans_lbl4.destroy()