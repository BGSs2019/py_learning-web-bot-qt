#this is day score program

#imports
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QProgressBar, QComboBox, QCheckBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pandas as pd
import sys
from datetime import date, timedelta

#global variables (redo)
defaultSelectionStartDate = date.today().strftime("%d.%m.%Y")
defaultSelectionEndDate = (date.today() + timedelta(-30)).strftime("%d.%m.%Y")

#example dataframe
exampleData = {"date": [date(2023, 8, 21), date(2023, 8, 22)], "good score": [2, 1],"bad score": [1, 1], "final score": [1, 0]}
habitsHistory = pd.DataFrame(exampleData)

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
        print(type(score))
        

    def addBadHabit(self, name, score):
        self.badHabits.append(name)
        self.badHabitsScores.append(score)

    def saveDay(self):
        self.goodHabitsScoresSum = sum(self.goodHabitsScores)
        self.badHabitsScoresSum = sum(self.badHabitsScores)
        self.habitsSum = self.goodHabitsScoresSum + self.badHabitsScoresSum
        dayData = {"date": date.today(), "good score": [self.goodHabitsScoresSum], "bad score": [self.badHabitsScoresSum]}
        #this global is bad
        global habitsHistory
        habitsHistory= pd.concat([habitsHistory, pd.DataFrame(dayData)], ignore_index=True)


#create simple container
Habits = HabitsContainer()

def addHabitFunc():
    habitName = win.habitNameInputLine.text()
    habitScore = int(win.habitScoreLine.text())

    if int(win.habitScoreLine.text()) > 0:
        Habits.addGoodHabit(habitName, habitScore)
        newHabitButton = QPushButton(f"(x){habitName}|{habitScore}")
        newHabitButton.setStyleSheet('QPushButton {background-color: #7FFF00; color: black;}')
        win.vbox.addWidget(newHabitButton)

    elif int(win.habitScoreLine.text()) < 0:
        Habits.addBadHabit(habitName, habitScore)
        newHabitButton = QPushButton(f"(x){habitName}|{habitScore}")
        newHabitButton.setStyleSheet('QPushButton {background-color: #FFA07A; color: black;}')
        win.vbox.addWidget(newHabitButton)


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
        #added habits init
        self.addedHabitsLabel = QLabel("Added habits:")

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
        self.vbox.addWidget(self.addedHabitsLabel)
        
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
            x = habitsHistory['date']
            y = habitsHistory['good score']
            ax.plot(x, y)
            self.canvas.draw()
            print(habitsHistory)
        elif self.viewSelectionComboBox.currentText() == "bad habits":
            self.figure.clear()
            self.figure.set_layout_engine(layout='tight')
            ax = self.figure.add_subplot(111)
            ax.set_title('Bad Score')
            ax.set_xlabel('Date')
            ax.set_ylabel('Score')
            x = habitsHistory['date']
            y = habitsHistory['bad score']
            ax.plot(x, y)
            self.canvas.draw()
        else:
            self.figure.clear()
            self.figure.set_layout_engine(layout='tight')
            ax = self.figure.add_subplot(111)
            ax.set_title('Final Score')
            ax.set_xlabel('Date')
            ax.set_ylabel('Score')
            x = habitsHistory['date']
            y = habitsHistory['final score']
            ax.plot(x, y)
            self.canvas.draw()


#Start
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DayScoreApp()
    app.exec()