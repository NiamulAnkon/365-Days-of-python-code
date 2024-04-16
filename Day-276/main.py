from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1162, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.amount = QtWidgets.QTextEdit(self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(30, 60, 361, 21))
        self.amount.setObjectName("amount")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.date = QtWidgets.QTextEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(30, 160, 361, 21))
        self.date.setObjectName("date")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.Note = QtWidgets.QTextEdit(self.centralwidget)
        self.Note.setGeometry(QtCore.QRect(20, 270, 381, 211))
        self.Note.setObjectName("Note")

        self.oneside = QtWidgets.QFrame(self.centralwidget)
        self.oneside.setGeometry(QtCore.QRect(9, 9, 401, 731))
        self.oneside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.oneside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.oneside.setObjectName("oneside")

        self.pushButton = QtWidgets.QPushButton(self.oneside)
        self.pushButton.setGeometry(QtCore.QRect(0, 530, 401, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.oneside)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 620, 401, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.secondframe = QtWidgets.QFrame(self.centralwidget)
        self.secondframe.setGeometry(QtCore.QRect(420, 10, 741, 731))
        self.secondframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.secondframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.secondframe.setObjectName("secondframe")

        self.el = QtWidgets.QLabel(self.secondframe)
        self.el.setGeometry(QtCore.QRect(10, 10, 161, 41))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.el.setFont(font)
        self.el.setObjectName("el")

        self.textEdit = QtWidgets.QTextEdit(self.secondframe)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 721, 641))
        self.textEdit.setObjectName("textEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.submit_expense)
        self.pushButton_2.clicked.connect(self.clear_fields)

        self.expenses = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Amount:"))
        self.label_2.setText(_translate("MainWindow", "Date:"))
        self.label_3.setText(_translate("MainWindow", "Notes:"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.el.setText(_translate("MainWindow", "Expense List:"))

    def submit_expense(self):
        amount = self.amount.toPlainText()
        date = self.date.toPlainText()
        notes = self.Note.toPlainText()

        expense_info = f"Amount: {amount}, Date: {date}, Notes: {notes}"
        self.expenses.append(expense_info)

        self.textEdit.setText("\n".join(self.expenses))

    def clear_fields(self):
        self.amount.clear()
        self.date.clear()
        self.Note.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
