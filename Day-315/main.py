# ui_mainwindow.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.amountInput = QtWidgets.QLineEdit(self.centralwidget)
        self.amountInput.setGeometry(QtCore.QRect(10, 60, 200, 30))
        self.amountInput.setObjectName("amountInput")

        self.categoryInput = QtWidgets.QLineEdit(self.centralwidget)
        self.categoryInput.setGeometry(QtCore.QRect(220, 60, 200, 30))
        self.categoryInput.setObjectName("categoryInput")

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(430, 60, 100, 30))
        self.addButton.setObjectName("addButton")

        self.transactionList = QtWidgets.QListWidget(self.centralwidget)
        self.transactionList.setGeometry(QtCore.QRect(10, 100, 580, 200))
        self.transactionList.setObjectName("transactionList")

        self.balanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.balanceLabel.setGeometry(QtCore.QRect(10, 310, 580, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.balanceLabel.setFont(font)
        self.balanceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.balanceLabel.setObjectName("balanceLabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Budget Tracker"))
        self.header.setText(_translate("MainWindow", "Simple Budget Tracker"))
        self.amountInput.setPlaceholderText(_translate("MainWindow", "Amount"))
        self.categoryInput.setPlaceholderText(_translate("MainWindow", "Category"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.balanceLabel.setText(_translate("MainWindow", "Balance: $0.00"))
