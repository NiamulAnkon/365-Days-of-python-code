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
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.vivaamount = QtWidgets.QLineEdit(self.centralwidget)
        self.vivaamount.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.vivaamount.setObjectName("vivaamount")
        self.valab = QtWidgets.QLabel(self.centralwidget)
        self.valab.setGeometry(QtCore.QRect(10, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.valab.setFont(font)
        self.valab.setAlignment(QtCore.Qt.AlignCenter)
        self.valab.setObjectName("valab")
        self.viadlab = QtWidgets.QLabel(self.centralwidget)
        self.viadlab.setGeometry(QtCore.QRect(230, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.viadlab.setFont(font)
        self.viadlab.setAlignment(QtCore.Qt.AlignCenter)
        self.viadlab.setObjectName("viadlab")

        self.vivadate = QtWidgets.QDateEdit(self.centralwidget)
        self.vivadate.setGeometry(QtCore.QRect(230, 80, 110, 22))
        self.vivadate.setObjectName("vivadate")

        self.givingpositions = QtWidgets.QLineEdit(self.centralwidget)
        self.givingpositions.setGeometry(QtCore.QRect(360, 80, 401, 20))
        self.givingpositions.setObjectName("givingpositions")

        self.gvplab = QtWidgets.QLabel(self.centralwidget)
        self.gvplab.setGeometry(QtCore.QRect(430, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gvplab.setFont(font)
        self.gvplab.setAlignment(QtCore.Qt.AlignCenter)
        self.gvplab.setObjectName("gvplab")
        
        self.listofvivas = QtWidgets.QTableWidget(self.centralwidget)
        self.listofvivas.setGeometry(QtCore.QRect(10, 280, 781, 311))
        self.listofvivas.setObjectName("listofvivas")
        self.listofvivas.setColumnCount(0)
        self.listofvivas.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Viva Managment Software for Campus Edify"))
        self.valab.setText(_translate("MainWindow", "viva amount"))
        self.viadlab.setText(_translate("MainWindow", "viva Date"))
        self.gvplab.setText(_translate("MainWindow", "giving positions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
