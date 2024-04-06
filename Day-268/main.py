from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 30, 801, 181))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setLineWidth(3)
        self.textBrowser.setMidLineWidth(-17)
        self.textBrowser.setObjectName("textBrowser")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(260, 510, 181, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn.setFont(font)
        self.btn.setStyleSheet("background-color: rgb(10, 255, 100);")
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.show_time)

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 240, 801, 181))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_2.setLineWidth(12)
        self.textBrowser_2.setMidLineWidth(-17)
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "Show"))

    def show_time(self):
        while True:
            QApplication.processEvents()
            dt = datetime.datetime.now()
            self.textBrowser.setText('Date: %s:%s:%s'%(dt.day, dt.month, dt.year))
            self.textBrowser_2.setText('Date: %s:%s:%s'%(dt.hour, dt.minute, dt.second))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
