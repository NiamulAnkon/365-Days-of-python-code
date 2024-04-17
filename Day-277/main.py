from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.task_lable = QtWidgets.QLabel(self.centralwidget)
        self.task_lable.setGeometry(QtCore.QRect(300, 30, 161, 61))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.task_lable.setFont(font)

        self.task_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.task_lable.setObjectName("task_lable")

        self.tsk_name = QtWidgets.QLineEdit(self.centralwidget)
        self.tsk_name.setGeometry(QtCore.QRect(280, 110, 211, 31))
        self.tsk_name.setText("")
        self.tsk_name.setObjectName("tsk_name")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 190, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addTask)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 260, 801, 341))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tasks = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.task_lable.setText(_translate("MainWindow", "Tasks Name:"))
        self.pushButton.setText(_translate("MainWindow", "Add task"))


    def addTask(self):
        task_name = self.tsk_name.text()
        if task_name:
            self.tasks.append(task_name)
            self.updateTaskList()
            self.tsk_name.clear()

    def updateTaskList(self):
        self.listWidget.clear()
        for task in self.tasks:
            self.listWidget.addItem(task)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())