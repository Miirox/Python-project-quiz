from MainWindow import *
from Toolbar import *
from Navigator import *
from Questions import *
from Answers import *
from Hints import *
from FinishButton import *
from Stopwatch import *
from EndWindow import *
from GiveUp import *
from datetime import datetime
import random

temp = 0
after_id = ''
indexes = []
ans_indexes = []
score = []
currentScore = 10


def navigateColors():
    navigate.navTo1['bg'] = "white"
    navigate.navTo2['bg'] = "white"
    navigate.navTo3['bg'] = "white"
    navigate.navTo4['bg'] = "white"
    navigate.navTo5['bg'] = "white"
    navigate.navTo6['bg'] = "white"
    navigate.navTo7['bg'] = "white"
    navigate.navTo8['bg'] = "white"
    navigate.navTo9['bg'] = "white"
    navigate.navTo10['bg'] = "white"


def newQuestion():
    global currentScore
    ans.ans_btn1['bg'] = '#ccc'
    ans.ans_btn2['bg'] = '#ccc'
    ans.ans_btn3['bg'] = '#ccc'
    ans.ans_btn4['bg'] = '#ccc'

    currentScore = 10


def falseAnswer1(self):
    global currentScore
    ans.ans_btn1['bg'] = 'red'
    ans.ans_btn1.config(state=DISABLED)
    currentScore -= 3


def falseAnswer2(self):
    global currentScore
    ans.ans_btn2['bg'] = 'red'
    ans.ans_btn2.config(state=DISABLED)
    currentScore -= 3


def falseAnswer3(self):
    global currentScore
    ans.ans_btn3['bg'] = 'red'
    ans.ans_btn3.config(state=DISABLED)
    currentScore -= 3


def falseAnswer4(self):
    global currentScore
    ans.ans_btn4['bg'] = 'red'
    ans.ans_btn4.config(state=DISABLED)
    currentScore -= 3


def randQuestions():
    global indexes
    while len(indexes) < 10:
        x = random.randint(0, 19)
        if x in indexes:
            continue
        else:
            indexes.append(x)


randQuestions()
print(indexes)
print()


def randAnswers():
    global ans_indexes
    while len(ans_indexes) < 4:
        x = random.randint(0, 3)
        if x in ans_indexes:
            continue
        else:
            ans_indexes.append(x)


def removeAnsIndexes():
    global ans_indexes
    ans_indexes = []


def startButtonClick(self):
    main_window.start_btn.destroy()
    main_window.welcome.destroy()
    main_window.rules_btn.destroy()
    main_window.exit_btn.destroy()
    rules_lbl.destroy()
    isStarted()


def rulesButtonClick(self):
    main_window.start_btn.place(x=300, y=175)
    main_window.rules_btn.place(x=450, y=175)
    main_window.exit_btn.place(x=600, y=175)
    rules_lbl.pack()
    rules_lbl.place(x=50, y=250, width=900, height=225)


def toMainButtonClick():
    endWind.delete()
    main_window.packed()


def isStarted():
    def tick():
        global temp, after_id
        after_id = root.after(1000, tick)
        f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
        stopTime.time_lbl.configure(text=str(f_temp))
        temp += 1
        if stopTime.time_lbl['text'] == "10:00":
            navigate.delete()
            quest.question.destroy()
            ans.delete()
            hint.delete()
            finish.delete()
            stopTime.delete()
            root.after_cancel(after_id)

            endWindow()

    navigate.packed()
    navigate.places()

    quest.places()
    Quest1()

    ans.packed()
    ans.places()

    hint.packed()
    hint.places()

    finish.packed()
    finish.places()

    stopTime.packed()
    stopTime.places()
    tick()


def Quest1():
    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo1['bg'] = "#FF1493"
    root['bg'] = '#ffa845'

    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[0]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[0]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[0]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[0]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[0]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#ffa845'
    ans.ans_lbl1['bg'] = '#ffa845'
    ans.ans_lbl2['bg'] = '#ffa845'
    ans.ans_lbl3['bg'] = '#ffa845'
    ans.ans_lbl4['bg'] = '#ffa845'
    stopTime.time_lbl['bg'] = '#ffa845'
    finish.end_btn['bg'] = '#9400d3'
    hint.hints_lbl['bg'] = '#9400d3'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[0]]:
        ans.ans_btn1.bind("<Button-1>", Quest2)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[0]]:
        ans.ans_btn2.bind("<Button-1>", Quest2)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[0]]:
        ans.ans_btn3.bind("<Button-1>", Quest2)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[0]]:
        ans.ans_btn4.bind("<Button-1>", Quest2)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def Quest2(self):
    score.append(currentScore)
    print(score)
    print()

    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo2['bg'] = "#FF1493"
    root['bg'] = '#fff945'

    removeAnsIndexes()
    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[1]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[1]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[1]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[1]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[1]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#fff945'
    ans.ans_lbl1['bg'] = '#fff945'
    ans.ans_lbl2['bg'] = '#fff945'
    ans.ans_lbl3['bg'] = '#fff945'
    ans.ans_lbl4['bg'] = '#fff945'
    stopTime.time_lbl['bg'] = '#fff945'
    finish.end_btn['bg'] = '#adff2f'
    hint.hints_lbl['bg'] = '#adff2f'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[1]]:
        ans.ans_btn1.bind("<Button-1>", Quest3)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[1]]:
        ans.ans_btn2.bind("<Button-1>", Quest3)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[1]]:
        ans.ans_btn3.bind("<Button-1>", Quest3)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[1]]:
        ans.ans_btn4.bind("<Button-1>", Quest3)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def Quest3(self):
    score.append(currentScore)
    print(score)
    print()

    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo3['bg'] = "#FF1493"
    root['bg'] = '#aeff45'

    removeAnsIndexes()
    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[2]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[2]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[2]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[2]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[2]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#aeff45'
    ans.ans_lbl1['bg'] = '#aeff45'
    ans.ans_lbl2['bg'] = '#aeff45'
    ans.ans_lbl3['bg'] = '#aeff45'
    ans.ans_lbl4['bg'] = '#aeff45'
    stopTime.time_lbl['bg'] = '#aeff45'
    finish.end_btn['bg'] = '#ffff00'
    hint.hints_lbl['bg'] = '#ffff00'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[2]]:
        ans.ans_btn1.bind("<Button-1>", Quest4)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[2]]:
        ans.ans_btn2.bind("<Button-1>", Quest4)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[2]]:
        ans.ans_btn3.bind("<Button-1>", Quest4)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[2]]:
        ans.ans_btn4.bind("<Button-1>", Quest4)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def Quest4(self):
    score.append(currentScore)
    print(score)
    print()

    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo4['bg'] = "#FF1493"
    root['bg'] = '#45ffbb'

    removeAnsIndexes()
    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[3]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[3]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[3]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[3]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[3]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#45ffbb'
    ans.ans_lbl1['bg'] = '#45ffbb'
    ans.ans_lbl2['bg'] = '#45ffbb'
    ans.ans_lbl3['bg'] = '#45ffbb'
    ans.ans_lbl4['bg'] = '#45ffbb'
    stopTime.time_lbl['bg'] = '#45ffbb'
    finish.end_btn['bg'] = '#1e90ff'
    hint.hints_lbl['bg'] = '#1e90ff'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[3]]:
        ans.ans_btn1.bind("<Button-1>", Quest5)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[3]]:
        ans.ans_btn2.bind("<Button-1>", Quest5)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[3]]:
        ans.ans_btn3.bind("<Button-1>", Quest5)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[3]]:
        ans.ans_btn4.bind("<Button-1>", Quest5)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def Quest5(self):
    score.append(currentScore)
    print(score)
    print()

    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo5['bg'] = "#FF1493"
    root['bg'] = '#45f3ff'

    removeAnsIndexes()
    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[4]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[4]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[4]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[4]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[4]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#45f3ff'
    ans.ans_lbl1['bg'] = '#45f3ff'
    ans.ans_lbl2['bg'] = '#45f3ff'
    ans.ans_lbl3['bg'] = '#45f3ff'
    ans.ans_lbl4['bg'] = '#45f3ff'
    stopTime.time_lbl['bg'] = '#45f3ff'
    finish.end_btn['bg'] = '#ff69b4'
    hint.hints_lbl['bg'] = '#ff69b4'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[4]]:
        ans.ans_btn1.bind("<Button-1>", Quest6)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[4]]:
        ans.ans_btn2.bind("<Button-1>", Quest6)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[4]]:
        ans.ans_btn3.bind("<Button-1>", Quest6)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[4]]:
        ans.ans_btn4.bind("<Button-1>", Quest6)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def Quest6(self):
    score.append(currentScore)
    print(score)
    print()

    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo6['bg'] = "#FF1493"
    root['bg'] = '#e28bf7'

    removeAnsIndexes()
    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[5]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[5]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[5]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[5]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[5]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#e28bf7'
    ans.ans_lbl1['bg'] = '#e28bf7'
    ans.ans_lbl2['bg'] = '#e28bf7'
    ans.ans_lbl3['bg'] = '#e28bf7'
    ans.ans_lbl4['bg'] = '#e28bf7'
    stopTime.time_lbl['bg'] = '#e28bf7'
    finish.end_btn['bg'] = '#ff00ff'
    hint.hints_lbl['bg'] = '#ff00ff'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[5]]:
        ans.ans_btn1.bind("<Button-1>", Quest7)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[5]]:
        ans.ans_btn2.bind("<Button-1>", Quest7)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[5]]:
        ans.ans_btn3.bind("<Button-1>", Quest7)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[5]]:
        ans.ans_btn4.bind("<Button-1>", Quest7)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def Quest7(self):
    score.append(currentScore)
    print(score)
    print()

    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo7['bg'] = "#FF1493"
    root['bg'] = '#c576cc'

    removeAnsIndexes()
    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[6]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[6]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[6]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[6]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[6]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#c576cc'
    ans.ans_lbl1['bg'] = '#c576cc'
    ans.ans_lbl2['bg'] = '#c576cc'
    ans.ans_lbl3['bg'] = '#c576cc'
    ans.ans_lbl4['bg'] = '#c576cc'
    stopTime.time_lbl['bg'] = '#c576cc'
    finish.end_btn['bg'] = '#00ffff'
    hint.hints_lbl['bg'] = '#00ffff'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[6]]:
        ans.ans_btn1.bind("<Button-1>", Quest8)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[6]]:
        ans.ans_btn2.bind("<Button-1>", Quest8)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[6]]:
        ans.ans_btn3.bind("<Button-1>", Quest8)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[6]]:
        ans.ans_btn4.bind("<Button-1>", Quest8)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def Quest8(self):
    score.append(currentScore)
    print(score)
    print()

    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo8['bg'] = "#FF1493"
    root['bg'] = '#ffd952'

    removeAnsIndexes()
    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[7]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[7]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[7]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[7]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[7]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#ffd952'
    ans.ans_lbl1['bg'] = '#ffd952'
    ans.ans_lbl2['bg'] = '#ffd952'
    ans.ans_lbl3['bg'] = '#ffd952'
    ans.ans_lbl4['bg'] = '#ffd952'
    stopTime.time_lbl['bg'] = '#ffd952'
    finish.end_btn['bg'] = '#ff1493'
    hint.hints_lbl['bg'] = '#ff1493'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[7]]:
        ans.ans_btn1.bind("<Button-1>", Quest9)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[7]]:
        ans.ans_btn2.bind("<Button-1>", Quest9)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[7]]:
        ans.ans_btn3.bind("<Button-1>", Quest9)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[7]]:
        ans.ans_btn4.bind("<Button-1>", Quest9)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def Quest9(self):
    score.append(currentScore)
    print(score)
    print()

    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo9['bg'] = "#FF1493"
    root['bg'] = '#bdff52'

    removeAnsIndexes()
    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[8]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[8]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[8]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[8]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[8]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#bdff52'
    ans.ans_lbl1['bg'] = '#bdff52'
    ans.ans_lbl2['bg'] = '#bdff52'
    ans.ans_lbl3['bg'] = '#bdff52'
    ans.ans_lbl4['bg'] = '#bdff52'
    stopTime.time_lbl['bg'] = '#bdff52'
    finish.end_btn['bg'] = '#7fffd4'
    hint.hints_lbl['bg'] = '#7fffd4'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[8]]:
        ans.ans_btn1.bind("<Button-1>", Quest10)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[8]]:
        ans.ans_btn2.bind("<Button-1>", Quest10)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[8]]:
        ans.ans_btn3.bind("<Button-1>", Quest10)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[8]]:
        ans.ans_btn4.bind("<Button-1>", Quest10)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def Quest10(self):
    score.append(currentScore)
    print(score)
    print()

    mark = sum(score)

    newQuestion()
    navigateColors()
    navigate.navTo10['bg'] = "#FF1493"
    root['bg'] = '#8fcbb4'

    removeAnsIndexes()
    randAnswers()
    print(ans_indexes)

    quest.question['text'] = quest.questList[indexes[9]]
    ans.ans_lbl1['text'] = ans.ansList[indexes[9]][ans_indexes[0]]
    ans.ans_lbl2['text'] = ans.ansList[indexes[9]][ans_indexes[1]]
    ans.ans_lbl3['text'] = ans.ansList[indexes[9]][ans_indexes[2]]
    ans.ans_lbl4['text'] = ans.ansList[indexes[9]][ans_indexes[3]]
    hint.hints_lbl['text'] = str(mark)

    quest.question['bg'] = '#8fcbb4'
    ans.ans_lbl1['bg'] = '#8fcbb4'
    ans.ans_lbl2['bg'] = '#8fcbb4'
    ans.ans_lbl3['bg'] = '#8fcbb4'
    ans.ans_lbl4['bg'] = '#8fcbb4'
    stopTime.time_lbl['bg'] = '#8fcbb4'
    finish.end_btn['bg'] = '#00ff00'
    hint.hints_lbl['bg'] = '#00ff00'

    if ans.ans_lbl1['text'] == ans.correctAnswers[indexes[9]]:
        ans.ans_btn1.bind("<Button-1>", endQuiz)
    else:
        ans.ans_btn1.bind("<Button-1>", falseAnswer1)

    if ans.ans_lbl2['text'] == ans.correctAnswers[indexes[9]]:
        ans.ans_btn2.bind("<Button-1>", endQuiz)
    else:
        ans.ans_btn2.bind("<Button-1>", falseAnswer2)

    if ans.ans_lbl3['text'] == ans.correctAnswers[indexes[9]]:
        ans.ans_btn3.bind("<Button-1>", endQuiz)
    else:
        ans.ans_btn3.bind("<Button-1>", falseAnswer3)

    if ans.ans_lbl4['text'] == ans.correctAnswers[indexes[9]]:
        ans.ans_btn4.bind("<Button-1>", endQuiz)
    else:
        ans.ans_btn4.bind("<Button-1>", falseAnswer4)


def endQuiz(self):
    score.append(currentScore)
    print(score)

    navigate.delete()
    quest.question.destroy()
    ans.delete()
    hint.delete()
    finish.delete()
    stopTime.delete()
    root.after_cancel(after_id)

    endWindow()


def endWindow():
    global score
    mark = sum(score)
    print(mark)
    string = 'Your Mark is: ' + str(mark)

    endWind.packed()
    endWind.mark_lbl['text'] = string
    endWind.placed()
    root['bg'] = '#00ffff'
    endWind.mark_lbl['bg'] = '#00ffff'
    endWind.exit_btn['bg'] = '#00FF00'


def giveUp(self):
    navigate.delete()
    quest.question.destroy()
    ans.delete()
    hint.delete()
    finish.delete()
    stopTime.delete()
    root.after_cancel(after_id)

    giveUpEndWindow()


def giveUpEndWindow():
    give_up.packed()
    give_up.places()
    root['bg'] = '#00ffff'
    give_up.message['bg'] = '#00ffff'
    give_up.mark['bg'] = '#00ffff'
    give_up.exit_btn['bg'] = '#00FF00'


root = Tk()
root.title("QUIZ")
root.geometry("1000x500")
root['bg'] = '#D09CFF'
root.resizable(width=False, height=False)
root.bind('<Escape>', lambda e: root.destroy())

main_window = MainWindow(root)
main_window.packed()
main_window.places()

main_window.start_btn.bind("<Button-1>", startButtonClick)
main_window.rules_btn.bind("<Button-1>", rulesButtonClick)

rules_lbl = Label(root, text='1. To start the test, press the start button.\n'
                             '2. You have up to four attempts to correctly answer the question. During the passage,\n'
                             'all the questions go in order.\n'
                             '3. After 10 minutes have passed, the test ends and you can see how many points you could score.\n'
                             '4. From above you can see what question you are currently answering.\n'
                             '5. If you answer the first time, you will earn 10 points for the question, from the second - 7 points,\n'
                             'from the third - 4 points, and from the fourth you will earn 1 point.\n'
                             '6. When you press the give up button, you automatically get 0 points',
                  font=('Times New Roman', 16),
                  justify='left'
                  )

tools = Toolbar(root)
tools.add(root)
root.config(menu=tools.main_menu)

navigate = Navigator(root)
quest = Questions(root)
ans = Answers(root)
hint = Hints(root)
finish = FinishButton(root)
stopTime = Stopwatch(root)
endWind = EndWindow(root)
give_up = GiveUp(root)

finish.end_btn.bind("<Button-1>", giveUp)

root.mainloop()
