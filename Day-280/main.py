from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BudgetTrackerApp(object):
    def setupUi(self, BudgetTrackerApp):
        BudgetTrackerApp.setObjectName("BudgetTrackerApp")
        BudgetTrackerApp.resize(911, 639)
        BudgetTrackerApp.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.364, x2:0, y2:0.017, stop:0 rgba(1, 255, 245, 255), stop:0.98 rgba(255, 23, 180, 255), stop:1 rgba(0, 0, 0, 0));")
        
        self.centralwidget = QtWidgets.QWidget(BudgetTrackerApp)
        self.centralwidget.setObjectName("centralwidget")

        self.thistory = QtWidgets.QListWidget(self.centralwidget)
        self.thistory.setGeometry(QtCore.QRect(90, 110, 671, 331))
        self.thistory.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.thistory.setObjectName("thistory")

        self.bodytext = QtWidgets.QLabel(self.centralwidget)
        self.bodytext.setGeometry(QtCore.QRect(90, 80, 111, 31))
        self.bodytext.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        
        self.bodytext.setAlignment(QtCore.Qt.AlignCenter)
        self.bodytext.setObjectName("bodytext")

        self.addtrnsbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addtrnsbtn.setGeometry(QtCore.QRect(360, 460, 161, 41))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.addtrnsbtn.setFont(font)
        self.addtrnsbtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.addtrnsbtn.setObjectName("addtrnsbtn")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(180, 0, 441, 71))

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)

        self.header.setFont(font)
        self.header.setStyleSheet("")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        BudgetTrackerApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(BudgetTrackerApp)
        QtCore.QMetaObject.connectSlotsByName(BudgetTrackerApp)

        self.addtrnsbtn.clicked.connect(self.add_transaction)

    def retranslateUi(self, BudgetTrackerApp):
        _translate = QtCore.QCoreApplication.translate
        BudgetTrackerApp.setWindowTitle(_translate("BudgetTrackerApp", "MainWindow"))
        self.bodytext.setText(_translate("BudgetTrackerApp", "Transaction History"))
        self.addtrnsbtn.setText(_translate("BudgetTrackerApp", "Add Transaction"))
        self.header.setText(_translate("BudgetTrackerApp", "Transaction Manager App"))

    def add_transaction(self):
        transaction, ok = QtWidgets.QInputDialog.getText(BudgetTrackerApp, "Add Transaction", "Enter transaction:")
        if ok and transaction:
            self.thistory.addItem(transaction)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BudgetTrackerApp = QtWidgets.QMainWindow()
    ui = Ui_BudgetTrackerApp()
    ui.setupUi(BudgetTrackerApp)
    BudgetTrackerApp.show()
    sys.exit(app.exec_())
