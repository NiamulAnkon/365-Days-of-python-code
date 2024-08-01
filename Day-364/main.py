from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 718)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 901, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.0113636 rgba(255, 0, 54, 255), stop:1 rgba(38, 255, 25, 255));")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.syr_lab = QtWidgets.QLabel(self.centralwidget)
        self.syr_lab.setGeometry(QtCore.QRect(340, 110, 171, 51))
        self.syr_lab.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                   "color: rgb(255, 255, 255);")
        self.syr_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.syr_lab.setObjectName("syr_lab")

        self.rank = QtWidgets.QComboBox(self.centralwidget)
        self.rank.setGeometry(QtCore.QRect(10, 180, 881, 41))
        self.rank.setObjectName("rank")
        self.rank.addItem("")
        self.rank.addItem("")

        self.train_info = QtWidgets.QLabel(self.centralwidget)
        self.train_info.setGeometry(QtCore.QRect(10, 320, 881, 391))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.train_info.setFont(font)
        self.train_info.setText("")
        self.train_info.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.train_info.setObjectName("train_info")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 240, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(40, 167, 69);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 240, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(40, 167, 69);")
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.pushButton.clicked.connect(self.show_info)
        self.pushButton_2.clicked.connect(self.show_info)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Valo Trainer"))
        self.syr_lab.setText(_translate("MainWindow", "Select Your Rank"))
        self.rank.setItemText(0, _translate("MainWindow", "Lower (iron, bronze, silver, gold)"))
        self.rank.setItemText(1, _translate("MainWindow", "Higher (plat, diamond, ascendant, immortal, radiant)"))
        self.pushButton.setText(_translate("MainWindow", "Show info for aim routine"))
        self.pushButton_2.setText(_translate("MainWindow", "Show info for aim labs"))

    def show_info(self):
        # Determine which rank is selected and which button is pressed
        rank_index = self.rank.currentIndex()
        sender = self.sender()

        if rank_index == 0:  # Lower rank selected
            if sender == self.pushButton:
                self.show_info_lower()
            elif sender == self.pushButton_2:
                self.show_aim_labs_lower()
        elif rank_index == 1:  # Higher rank selected
            if sender == self.pushButton:
                self.show_info_high()
            elif sender == self.pushButton_2:
                self.show_aim_labs_high()

    def show_info_high(self):
        msg_high = '''Aim and Practice Routine for High-Rank Players (Platinum+)
Focus: Refinement, consistency, and adaptability.

Warm-up (15-20 minutes):
Static crosshair placement: Practice holding your crosshair on specific points on the screen for extended periods.
Tracking drills: Follow moving targets at various speeds and angles.
Flick shots: Train rapid target acquisition and precision.
Aim training (30-45 minutes):
Aim Labs or Kovaak's: Utilize custom scenarios to target specific weaknesses (e.g., flicking, tracking, micro-adjustments).
Deathmatch: Practice aim in a live environment, focusing on crosshair placement, recoil control, and shot accuracy.
Agent-specific practice (15-20 minutes):
Master ability usage: Experiment with different scenarios and combinations.
Line-up practice: Perfect ability placements for optimal impact.
Competitive matches (1-2 hours):
Apply skills in-game: Focus on decision-making, map awareness, and teamwork.
Analyze gameplay: Review demos to identify areas for improvement.
Additional Tips:
Consistency: Practice regularly, even if it's for short durations.
Variety: Incorporate different aim training exercises to prevent plateaus.
Mental game: Develop strategies to manage stress and maintain focus.
Teamwork: Communicate effectively and coordinate with your team.'''
        self.train_info.setText(msg_high)

    def show_aim_labs_high(self):
        aim_labs_trainings_high = '''High-Rank Players (Platinum+)
Focus: Precision, reaction time, and adaptability.

Warm-up:
Straight Shot: Improve consistency and click accuracy.
Target Switch: Enhance target acquisition and flicking.
Main Course:
Flick Shot: Develop rapid target acquisition and precision.
Tracking: Improve ability to follow moving targets at various speeds.
Reaction Time: Enhance response time to sudden targets.
Strafe Shot: Practice shooting while moving.
Cooldown:
Aim Hero: Identify strengths and weaknesses.
Gridshot: Improve crosshair placement and consistency.'''
        self.train_info.setText(aim_labs_trainings_high)

    def show_info_lower(self):
        msg_low = '''Aim and Practice Routine for Low-Rank Players (Iron-Gold)
Focus: Fundamentals, consistency, and muscle memory.

Warm-up (10-15 minutes):
Static crosshair placement: Build muscle memory for accurate aiming.
Basic tracking drills: Improve ability to follow targets.
Aim training (20-30 minutes):
Aim Labs or Kovaak's: Start with basic scenarios to establish foundations.
Deathmatch: Practice gunplay and movement mechanics.
Game sense (15-20 minutes):
Watch pro players or streamers: Learn map control, economy management, and team coordination.
Observe your gameplay: Identify common mistakes and areas for improvement.
Competitive matches (1-2 hours):
Apply what you've learned: Focus on basic mechanics and decision-making.
Communicate with your team: Build trust and improve coordination.
Additional Tips:
Patience: Improvement takes time. Avoid getting discouraged.
Fundamentals: Master basic mechanics before moving to advanced techniques.
Game sense: Understanding the game is as important as aim.
Positive attitude: A good mindset can significantly impact performance.'''
        self.train_info.setText(msg_low)

    def show_aim_labs_lower(self):
        aim_labs_trainings_low = '''Low-Rank Players (Iron-Gold)
Focus: Fundamentals, consistency, and muscle memory.

Warm-up:
Straight Shot: Build basic accuracy and consistency.
Tracking (slow): Start with slower targets to build muscle memory.
Main Course:
Click Test: Improve click speed and accuracy.
Target Switch (easy): Develop basic flicking ability.
Tracking (medium): Gradually increase target speed.
Strafe Shot (slow): Practice shooting while moving at a controlled pace.
Cooldown:
Aim Hero: Identify areas for improvement.
Gridshot: Develop basic crosshair placement.'''
        self.train_info.setText(aim_labs_trainings_low)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
