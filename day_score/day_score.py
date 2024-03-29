#this is day score program

#imports
import typing
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QVBoxLayout, QPushButton, QLineEdit, QGroupBox, QComboBox, QWidgetAction
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pandas as pd
import sys
from datetime import date, datetime, timedelta

#global variables (redo)
defaultSelectionStartDate = (date.today() + timedelta(-9)).strftime("%d.%m.%Y")
defaultSelectionEndDate = date.today().strftime("%d.%m.%Y")

#example dataframe
#exampleData = {"date": [date(2023, 8, 21), date(2023, 8, 22)], "good score": [2, 1],"bad score": [1, 1], "final score": [1, 0]}
dateparse = lambda x: date.strptime(x, '%d.%m.%Y')
habitsHistory = pd.read_csv("day_score/habitsHistory.csv", sep=";", header=0, parse_dates=True, index_col=["date"])

#habits class
class HabitsContainer():
    goodHabits = []
    goodHabitsScores = []
    goodHabitsScoresSum = 0

    badHabits = []
    badHabitsScores = []
    badHabitsScoresSum = 0

    habitsSum = 0

    def addGoodHabit(self, name, score):
        self.goodHabits.append(name)
        self.goodHabitsScores.append(score)

    def addBadHabit(self, name, score):
        self.badHabits.append(name)
        self.badHabitsScores.append(score)

    def saveDay(self):
        if len(self.goodHabitsScores) != 0:
            self.goodHabitsScoresSum = sum(self.goodHabitsScores)
        if len(self.badHabitsScores) != 0:
            self.badHabitsScoresSum = sum(self.badHabitsScores)
        self.habitsSum = self.goodHabitsScoresSum + self.badHabitsScoresSum
        dayData = {"date": datetime.today(), "good score": [self.goodHabitsScoresSum], "bad score": [self.badHabitsScoresSum], "final score": [self.habitsSum]}
        #this global is bad
        global habitsHistory
        habitsHistory= pd.concat([habitsHistory, pd.DataFrame(dayData).set_index(["date"])])
        print(habitsHistory)

    def deleteCurrentHabit(self):
        target = QApplication.instance().sender()
        targetText = target.text().replace("(x)", "").split("|")
        name = targetText[0]
        score = int(targetText[1])
        if score > 0:
            Habits.addGoodHabit(f"-{name}", -score)
        else:
            Habits.addBadHabit(f"-{name}", -score)
        target.deleteLater()

    def deleteHabits(self):
        for button in win.addedHabitsGroupBox.findChildren(QPushButton):
            button.deleteLater()


#create simple container
Habits = HabitsContainer()

def addHabitFunc():
    habitName = win.habitNameInputLine.text()
    habitScore = int(win.habitScoreLine.text())

    if int(win.habitScoreLine.text()) > 0:
        Habits.addGoodHabit(habitName, habitScore)
        newHabitButton = QPushButton(parent=win.addedHabitsGroupBox, text=f"(x){habitName}|{habitScore}")
        newHabitButton.setStyleSheet('QPushButton {background-color: #7FFF00; color: black;}')
        newHabitButton.clicked.connect(Habits.deleteCurrentHabit)
        win.addedHabitsGroupBoxLayout.addWidget(newHabitButton)

    elif int(win.habitScoreLine.text()) < 0:
        Habits.addBadHabit(habitName, habitScore)
        newHabitButton = QPushButton(parent=win.addedHabitsGroupBox, text=f"(x){habitName}|{habitScore}")
        newHabitButton.setStyleSheet('QPushButton {background-color: #FFA07A; color: black;}')
        newHabitButton.clicked.connect(Habits.deleteCurrentHabit)
        win.addedHabitsGroupBoxLayout.addWidget(newHabitButton)


#Main widget
class DayScoreApp(QWidget):
    #interface initialization
    def __init__(self):
        super().__init__()
        self.initUI()

    #initialization
    def initUI(self):
        #view selection init
        self.viewSelectionComboBox = QComboBox()
        habitsTypes = ["good habits", "bad habits", "full selection"]
        self.viewSelectionComboBox.addItems(habitsTypes)
        self.viewSeletionPeriodLabel = QLabel("Set period:")
        self.viewSeletionStartDateLine = QLineEdit(defaultSelectionStartDate)
        self.viewSeletionEndDateLine = QLineEdit(defaultSelectionEndDate)
        self.viewButton = QPushButton("Show")
        self.viewButton.clicked.connect(self.plotHabits)
        #view canvas init
        self.figure = plt.figure(figsize = [2, 2], edgecolor = 'black')
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.figure.set_layout_engine(layout='tight')
        ax = self.figure.add_subplot(111)
        ax.set_title("Habits")
        ax.set_xlabel('Score')
        ax.set_ylabel('Date')
        #input init
        self.habitNameInputLabel = QLabel("Habit:")
        self.habitNameInputLine = QLineEdit()
        self.habitScoreLabel = QLabel("Score")
        self.habitScoreLine = QLineEdit()
        self.habitInputButton = QPushButton("Input habit")
        self.habitInputButton.clicked.connect(self.addHabit)
        #day options init
        self.dayLabel = QLabel("Day options:")
        self.daySaveButton = QPushButton("Save day")
        self.daySaveButton.clicked.connect(self.saveDay)
        self.dayResetDayButton = QPushButton("Reset day")
        self.dayResetDayButton.clicked.connect(self.resetDay)
        #habits groupbox
        self.addedHabitsGroupBox = QGroupBox("Added habits:")

        #grid layout
        self.vbox = QVBoxLayout()
        #view selection add
        self.vbox.addWidget(self.viewSelectionComboBox)
        self.vbox.addWidget(self.viewSeletionPeriodLabel)
        self.vbox.addWidget(self.viewSeletionStartDateLine)
        self.vbox.addWidget(self.viewSeletionEndDateLine)
        self.vbox.addWidget(self.viewButton)
        #canvas add
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.canvas)
        #input add
        self.vbox.addWidget(self.habitNameInputLabel)
        self.vbox.addWidget(self.habitNameInputLine)
        self.vbox.addWidget(self.habitScoreLabel)
        self.vbox.addWidget(self.habitScoreLine)
        self.vbox.addWidget(self.habitInputButton)
        #day options add
        self.vbox.addWidget(self.dayLabel)
        self.vbox.addWidget(self.daySaveButton)
        self.vbox.addWidget(self.dayResetDayButton)
        #added habits add
        self.vbox.addWidget(self.addedHabitsGroupBox)
        self.addedHabitsGroupBoxLayout = QVBoxLayout()
        self.addedHabitsGroupBox.setLayout(self.addedHabitsGroupBoxLayout)
        
        #layout setting
        self.setLayout(self.vbox)

        #show widget
        self.setWindowTitle('Day score')
        self.show()

    def addHabit(self):
        self.vbox.addWidget(addHabitFunc())

    def saveDay(self):
        Habits.saveDay()

    def plotHabits(self):
        if self.viewSelectionComboBox.currentText() == "good habits":
            self.figure.clear()
            self.figure.set_layout_engine(layout='tight')
            ax = self.figure.add_subplot(111)
            ax.set_title('Good Score')
            ax.set_xlabel('Date')
            ax.set_ylabel('Score')
            dateIndexStart = datetime.strptime(win.viewSeletionStartDateLine.text(), '%d.%m.%Y')
            dateIndexEnd = datetime.strptime(win.viewSeletionEndDateLine.text(), '%d.%m.%Y')
            dataSelected = habitsHistory[dateIndexStart: dateIndexEnd]
            print(dataSelected)
            x = dataSelected.index
            y = dataSelected["good score"]
            ax.plot(x, y)
            self.canvas.draw()
        elif self.viewSelectionComboBox.currentText() == "bad habits":
            self.figure.clear()
            self.figure.set_layout_engine(layout='tight')
            ax = self.figure.add_subplot(111)
            ax.set_title('Bad Score')
            ax.set_xlabel('Date')
            ax.set_ylabel('Score')
            dateIndexStart = datetime.strptime(win.viewSeletionStartDateLine.text(), '%d.%m.%Y')
            dateIndexEnd = datetime.strptime(win.viewSeletionEndDateLine.text(), '%d.%m.%Y')
            dataSelected = habitsHistory[dateIndexStart: dateIndexEnd]
            print(dataSelected)
            x = dataSelected.index
            y = dataSelected["bad score"]
            ax.plot(x, y)
            self.canvas.draw()
        else:
            self.figure.clear()
            self.figure.set_layout_engine(layout='tight')
            ax = self.figure.add_subplot(111)
            ax.set_title('Final Score')
            ax.set_xlabel('Date')
            ax.set_ylabel('Score')
            dateIndexStart = datetime.strptime(win.viewSeletionStartDateLine.text(), '%d.%m.%Y')
            dateIndexEnd = datetime.strptime(win.viewSeletionEndDateLine.text(), '%d.%m.%Y')
            dataSelected = habitsHistory[dateIndexStart: dateIndexEnd]
            print(dataSelected)
            x = dataSelected.index
            y = dataSelected["final score"]
            ax.plot(x, y)
            self.canvas.draw()

    def resetDay(self):
       global Habits
       global habitsHistory
       Habits.deleteHabits()
       Habits = HabitsContainer()
       habitsHistory.drop(date.today(), inplace=True)


#Start
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DayScoreApp()
    app.exec()
    habitsHistory.to_csv("day_score/habitsHistory.csv", sep=";")