from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.header.setFont(font)
        self.header.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.233, y1:0.778318, x2:0.823545, y2:0.25, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(55, 245, 0, 255));")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.cnsitlab = QtWidgets.QLabel(self.centralwidget)
        self.cnsitlab.setGeometry(QtCore.QRect(310, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cnsitlab.setFont(font)
        self.cnsitlab.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"color: rgb(255, 255, 255);")
        self.cnsitlab.setAlignment(QtCore.Qt.AlignCenter)
        self.cnsitlab.setObjectName("cnsitlab")

        self.cnsit = QtWidgets.QLabel(self.centralwidget)
        self.cnsit.setGeometry(QtCore.QRect(0, 150, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cnsit.setFont(font)
        self.cnsit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cnsit.setText("")
        self.cnsit.setAlignment(QtCore.Qt.AlignCenter)
        self.cnsit.setObjectName("cnsit")

        self.betlab = QtWidgets.QLabel(self.centralwidget)
        self.betlab.setGeometry(QtCore.QRect(300, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.betlab.setFont(font)
        self.betlab.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"color: rgb(255, 255, 255);")
        self.betlab.setAlignment(QtCore.Qt.AlignCenter)
        self.betlab.setObjectName("betlab")

        self.betamount = QtWidgets.QLineEdit(self.centralwidget)
        self.betamount.setGeometry(QtCore.QRect(310, 250, 113, 20))
        self.betamount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.betamount.setObjectName("betamount")

        self.pgup = QtWidgets.QPushButton(self.centralwidget)
        self.pgup.setGeometry(QtCore.QRect(250, 320, 75, 23))
        self.pgup.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pgup.setObjectName("pgup")
        self.pgup.clicked.connect(lambda: self.place_bet("up"))

        self.pgdown = QtWidgets.QPushButton(self.centralwidget)
        self.pgdown.setGeometry(QtCore.QRect(404, 320, 81, 23))
        self.pgdown.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pgdown.setObjectName("pgdown")
        self.pgdown.clicked.connect(lambda: self.place_bet("down"))

        self.listofe = QtWidgets.QListWidget(self.centralwidget)
        self.listofe.setGeometry(QtCore.QRect(0, 350, 801, 251))
        self.listofe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listofe.setObjectName("listofe")

        self.ballab = QtWidgets.QLabel(self.centralwidget)
        self.ballab.setGeometry(QtCore.QRect(700, 70, 41, 16))
        self.ballab.setObjectName("ballab")
        
        self.balance = QtWidgets.QLabel(self.centralwidget)
        self.balance.setGeometry(QtCore.QRect(750, 70, 31, 16))
        self.balance.setText("1000")
        self.balance.setObjectName("balance")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trading Game"))
        self.header.setText(_translate("MainWindow", "Trading Game"))
        self.cnsitlab.setText(_translate("MainWindow", "The Coin Situation"))
        self.betlab.setText(_translate("MainWindow", "Bet Amount"))
        self.pgup.setText(_translate("MainWindow", "Price Go Up"))
        self.pgdown.setText(_translate("MainWindow", "Price Go Down"))
        self.ballab.setText(_translate("MainWindow", "Balance:"))

    def update_coin_situation(self):
        # Generate a random coin price situation
        coin_price = random.uniform(1, 100)  # Example: Random price between 1 and 100
        self.cnsit.setText(f"Current Coin Price: ${coin_price:.2f}")
    
    def place_bet(self, direction):
        try:
            bet = int(self.betamount.text())
        except ValueError:
            self.listofe.addItem("Invalid bet amount.")
            return

        current_balance = int(self.balance.text())
        if bet > current_balance:
            self.listofe.addItem("Insufficient balance.")
            return

        outcome = random.choice(["up", "down"])
        if direction == outcome:
            current_balance += bet
            self.listofe.addItem(f"You won! Bet amount: {bet}. Outcome: {outcome}.")
        else:
            current_balance -= bet
            self.listofe.addItem(f"You lost! Bet amount: {bet}. Outcome: {outcome}.")

        self.balance.setText(str(current_balance))
        self.update_coin_situation()