from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 600)
        font = QtGui.QFont()
        font.setFamily("Roman")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(24, 24, 24);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.ablab = QtWidgets.QLabel(self.centralwidget)
        self.ablab.setGeometry(QtCore.QRect(30, 100, 191, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.ablab.setFont(font)
        self.ablab.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.ablab.setAlignment(QtCore.Qt.AlignCenter)
        self.ablab.setObjectName("ablab")

        self.nrlab = QtWidgets.QLabel(self.centralwidget)
        self.nrlab.setGeometry(QtCore.QRect(360, 100, 191, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.nrlab.setFont(font)
        self.nrlab.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.nrlab.setAlignment(QtCore.Qt.AlignCenter)
        self.nrlab.setObjectName("nrlab")

        self.lhlab = QtWidgets.QLabel(self.centralwidget)
        self.lhlab.setGeometry(QtCore.QRect(660, 100, 191, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lhlab.setFont(font)
        self.lhlab.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.lhlab.setAlignment(QtCore.Qt.AlignCenter)
        self.lhlab.setObjectName("lhlab")

        self.aba = QtWidgets.QPushButton(self.centralwidget)
        self.aba.setGeometry(QtCore.QRect(40, 170, 151, 23))
        self.aba.setStyleSheet("background-color: rgb(255, 102, 64);")
        self.aba.setObjectName("aba")
        self.aba.clicked.connect(self.add_status)

        self.nra = QtWidgets.QPushButton(self.centralwidget)
        self.nra.setGeometry(QtCore.QRect(370, 170, 151, 23))
        self.nra.setStyleSheet("background-color: rgb(255, 102, 64);")
        self.nra.setObjectName("nra")
        self.nra.clicked.connect(self.add_status)

        self.lha = QtWidgets.QPushButton(self.centralwidget)
        self.lha.setGeometry(QtCore.QRect(680, 170, 151, 23))
        self.lha.setStyleSheet("background-color: rgb(255, 102, 64);")
        self.lha.setObjectName("lha")
        self.lha.clicked.connect(self.add_status)

        self.wha = QtWidgets.QPushButton(self.centralwidget)
        self.wha.setGeometry(QtCore.QRect(40, 370, 151, 23))
        self.wha.setStyleSheet("background-color: rgb(255, 102, 64);")
        self.wha.setObjectName("wha")
        self.wha.clicked.connect(self.add_status)

        self.whlab = QtWidgets.QLabel(self.centralwidget)
        self.whlab.setGeometry(QtCore.QRect(30, 300, 191, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.whlab.setFont(font)
        self.whlab.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.whlab.setAlignment(QtCore.Qt.AlignCenter)
        self.whlab.setObjectName("whlab")

        self.bblab = QtWidgets.QLabel(self.centralwidget)
        self.bblab.setGeometry(QtCore.QRect(350, 300, 191, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.bblab.setFont(font)
        self.bblab.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.bblab.setAlignment(QtCore.Qt.AlignCenter)
        self.bblab.setObjectName("bblab")

        self.bba = QtWidgets.QPushButton(self.centralwidget)
        self.bba.setGeometry(QtCore.QRect(360, 380, 151, 23))
        self.bba.setStyleSheet("background-color: rgb(255, 102, 64);")
        self.bba.setObjectName("bba")
        self.bba.clicked.connect(self.add_status)

        self.fa = QtWidgets.QPushButton(self.centralwidget)
        self.fa.setGeometry(QtCore.QRect(690, 380, 151, 23))
        self.fa.setStyleSheet("background-color: rgb(255, 102, 64);")
        self.fa.setObjectName("fa")
        self.fa.clicked.connect(self.add_status)

        self.flab = QtWidgets.QLabel(self.centralwidget)
        self.flab.setGeometry(QtCore.QRect(680, 300, 191, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

        self.flab.setFont(font)
        self.flab.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.flab.setAlignment(QtCore.Qt.AlignCenter)
        self.flab.setObjectName("flab")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setStyleSheet("color: rgb(255, 0, 0);")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Hacks for shoting game"))
        self.ablab.setText(_translate("MainWindow", "Aim Bot"))
        self.nrlab.setText(_translate("MainWindow", "No Recoil"))
        self.lhlab.setText(_translate("MainWindow", "Lock Head"))
        self.aba.setText(_translate("MainWindow", "Activate"))
        self.nra.setText(_translate("MainWindow", "Activate"))
        self.lha.setText(_translate("MainWindow", "Activate"))
        self.wha.setText(_translate("MainWindow", "Activate"))
        self.whlab.setText(_translate("MainWindow", "Wall Hack"))
        self.bblab.setText(_translate("MainWindow", "Breaking Bullets"))
        self.bba.setText(_translate("MainWindow", "Activate"))
        self.fa.setText(_translate("MainWindow", "Activate"))
        self.flab.setText(_translate("MainWindow", "Fly"))

    def add_status(self):
        self.statusbar.setWindowTitle('Activated :)')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())