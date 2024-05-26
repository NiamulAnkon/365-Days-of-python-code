from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.tsknm = QtWidgets.QLineEdit(self.centralwidget)
        self.tsknm.setGeometry(QtCore.QRect(20, 90, 121, 21))
        self.tsknm.setObjectName("tsknm")

        self.tskdln = QtWidgets.QLineEdit(self.centralwidget)
        self.tskdln.setGeometry(QtCore.QRect(190, 90, 121, 21))
        self.tskdln.setObjectName("tskdln")

        self.tskdes = QtWidgets.QLineEdit(self.centralwidget)
        self.tskdes.setGeometry(QtCore.QRect(360, 90, 121, 21))
        self.tskdes.setObjectName("tskdes")

        self.tskctg = QtWidgets.QLineEdit(self.centralwidget)
        self.tskctg.setGeometry(QtCore.QRect(530, 90, 121, 21))
        self.tskctg.setObjectName("tskctg")

        self.tsknmlab = QtWidgets.QLabel(self.centralwidget)
        self.tsknmlab.setGeometry(QtCore.QRect(20, 60, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tsknmlab.setFont(font)
        self.tsknmlab.setAlignment(QtCore.Qt.AlignCenter)
        self.tsknmlab.setObjectName("tsknmlab")

        self.tskdlnlab = QtWidgets.QLabel(self.centralwidget)
        self.tskdlnlab.setGeometry(QtCore.QRect(190, 60, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tskdlnlab.setFont(font)
        self.tskdlnlab.setAlignment(QtCore.Qt.AlignCenter)
        self.tskdlnlab.setObjectName("tskdlnlab")

        self.tskdeslab = QtWidgets.QLabel(self.centralwidget)
        self.tskdeslab.setGeometry(QtCore.QRect(360, 60, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tskdeslab.setFont(font)
        self.tskdeslab.setAlignment(QtCore.Qt.AlignCenter)
        self.tskdeslab.setObjectName("tskdeslab")

        self.tskctglab = QtWidgets.QLabel(self.centralwidget)
        self.tskctglab.setGeometry(QtCore.QRect(540, 60, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tskctglab.setFont(font)
        self.tskctglab.setAlignment(QtCore.Qt.AlignCenter)
        self.tskctglab.setObjectName("tskctglab")

        self.addbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addbtn.setGeometry(QtCore.QRect(340, 180, 111, 31))
        self.addbtn.setObjectName("addbtn")
        self.addbtn.clicked.connect(self.add_tasks)

        self.tsklist = QtWidgets.QListWidget(self.centralwidget)
        self.tsklist.setGeometry(QtCore.QRect(0, 250, 801, 351))
        self.tsklist.setObjectName("tsklist")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Task Manager"))
        self.tsknmlab.setText(_translate("MainWindow", "Task name"))
        self.tskdlnlab.setText(_translate("MainWindow", "Task Deadline"))
        self.tskdeslab.setText(_translate("MainWindow", "Task description"))
        self.tskctglab.setText(_translate("MainWindow", "Task catageory"))
        self.addbtn.setText(_translate("MainWindow", "Add Tasks"))
    def add_tasks(self):
        task_name = self.tsknm.text()
        task_deadline = self.tskdln.text()
        task_description = self.tskdes.text()
        task_catageory = self.tskctg.text()
        info = f"Task Name: {task_name} Task Deadline: {task_deadline} Task Description: {task_description} Task Catageory: {task_catageory}"
        self.tsklist.addItem(info)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
