from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.tasks = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -20, 941, 641))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("13167.jpg"))
        self.background.setObjectName("background")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 290, 751, 281))
        self.listWidget.setObjectName("listWidget")

        self.addtask_2 = QtWidgets.QLabel(self.centralwidget)
        self.addtask_2.setGeometry(QtCore.QRect(380, 250, 101, 41))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.addtask_2.setFont(font)
        self.addtask_2.setStyleSheet("color: qlineargradient(spread:pad, x1:1, y1:0.364, x2:0, y2:0.017, stop:0 rgba(255, 238, 1, 255), stop:0.98 rgba(155, 90, 255, 255), stop:1 rgba(0, 0, 0, 0));")
        self.addtask_2.setAlignment(QtCore.Qt.AlignCenter)
        self.addtask_2.setObjectName("addtask_2")

        self.tdlst = QtWidgets.QLabel(self.centralwidget)
        self.tdlst.setGeometry(QtCore.QRect(340, 20, 251, 71))

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        self.tdlst.setFont(font)
        self.tdlst.setStyleSheet("color: qlineargradient(spread:pad, x1:1, y1:0.364, x2:0, y2:0.017, stop:0 rgba(255, 238, 1, 255), stop:0.98 rgba(155, 90, 255, 255), stop:1 rgba(0, 0, 0, 0));")
        self.tdlst.setAlignment(QtCore.Qt.AlignCenter)
        self.tdlst.setObjectName("tdlst")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 180, 191, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.addtask = QtWidgets.QLabel(self.centralwidget)
        self.addtask.setGeometry(QtCore.QRect(380, 130, 101, 41))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.addtask.setFont(font)
        self.addtask.setStyleSheet("color: qlineargradient(spread:pad, x1:1, y1:0.364, x2:0, y2:0.017, stop:0 rgba(255, 238, 1, 255), stop:0.98 rgba(155, 90, 255, 255), stop:1 rgba(0, 0, 0, 0));")
        self.addtask.setAlignment(QtCore.Qt.AlignCenter)
        self.addtask.setObjectName("addtask")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_task)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 580, 201, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.delete_task)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addtask_2.setText(_translate("MainWindow", "Tasks:"))
        self.tdlst.setText(_translate("MainWindow", "Todo-List"))
        self.addtask.setText(_translate("MainWindow", "Add Task:"))
        self.pushButton.setText(_translate("MainWindow", "Add Task"))
        self.pushButton_2.setText(_translate("MainWindow", "Dellete Task"))
    
    def add_task(self):
        task = self.lineEdit.text()
        if task:
            self.tasks.append(task)
            self.listWidget.addItem(task)
            self.lineEdit.clear()

    def delete_task(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            self.tasks.remove(selected_item.text())
            self.listWidget.takeItem(self.listWidget.row(selected_item))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
