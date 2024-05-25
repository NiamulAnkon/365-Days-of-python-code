from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(0, 0, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Header.setFont(font)
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setObjectName("Header")

        self.fc = QtWidgets.QLineEdit(self.centralwidget)
        self.fc.setGeometry(QtCore.QRect(80, 130, 131, 21))
        self.fc.setObjectName("fc")

        self.tc = QtWidgets.QLineEdit(self.centralwidget)
        self.tc.setGeometry(QtCore.QRect(550, 130, 131, 21))
        self.tc.setObjectName("tc")

        self.cnvbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cnvbtn.setGeometry(QtCore.QRect(330, 190, 101, 41))
        self.cnvbtn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.cnvbtn.setObjectName("cnvbtn")
        self.cnvbtn.clicked.connect(self.convert)

        self.brrrrrrr = QtWidgets.QLabel(self.centralwidget)
        self.brrrrrrr.setGeometry(QtCore.QRect(250, 390, 271, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.brrrrrrr.setFont(font)
        self.brrrrrrr.setText("")
        self.brrrrrrr.setAlignment(QtCore.Qt.AlignCenter)
        self.brrrrrrr.setObjectName("brrrrrrr")

        self.fclab = QtWidgets.QLabel(self.centralwidget)
        self.fclab.setGeometry(QtCore.QRect(30, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fclab.setFont(font)
        self.fclab.setAlignment(QtCore.Qt.AlignCenter)
        self.fclab.setObjectName("fclab")

        self.tclab = QtWidgets.QLabel(self.centralwidget)
        self.tclab.setGeometry(QtCore.QRect(500, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tclab.setFont(font)
        self.tclab.setAlignment(QtCore.Qt.AlignCenter)
        self.tclab.setObjectName("tclab")

        self.fa = QtWidgets.QLineEdit(self.centralwidget)
        self.fa.setGeometry(QtCore.QRect(100, 270, 131, 21))
        self.fa.setObjectName("fa")

        self.falab = QtWidgets.QLabel(self.centralwidget)
        self.falab.setGeometry(QtCore.QRect(50, 210, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.falab.setFont(font)
        self.falab.setAlignment(QtCore.Qt.AlignCenter)
        self.falab.setObjectName("falab")

        self.talab = QtWidgets.QLabel(self.centralwidget)
        self.talab.setGeometry(QtCore.QRect(480, 210, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.talab.setFont(font)
        self.talab.setAlignment(QtCore.Qt.AlignCenter)
        self.talab.setObjectName("talab")

        self.ta = QtWidgets.QLineEdit(self.centralwidget)
        self.ta.setGeometry(QtCore.QRect(530, 270, 131, 21))
        self.ta.setObjectName("ta")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Header.setText(_translate("MainWindow", "Currency Converter"))
        self.cnvbtn.setText(_translate("MainWindow", "Convert"))
        self.fclab.setText(_translate("MainWindow", "From Currency"))
        self.tclab.setText(_translate("MainWindow", "To Currency Currency"))
        self.falab.setText(_translate("MainWindow", "From Amount"))
        self.talab.setText(_translate("MainWindow", "To Amount"))
    def convert(self):
        from_currency = self.fc.text()
        to_currency = self.tc.text()

        if from_currency == "BDT" and to_currency == "USD":
            bdt = self.fa.text()
            to_currency = bdt * 120
            self.brrrrrrr.text(to_currency)

        if from_currency == "USD" and to_currency == "EUR":
            usd = self.fa.text()
            to_currency = usd * 0.92
            self.brrrrrrr.text(to_currency)

        if from_currency == "EUR" and to_currency == "BDT":
            eur = self.fa.text()
            to_currency = eur * 0.0079
            self.brrrrrrr.text(to_currency)
        else:
            self.brrrrrrr.text("Sorry i Can't do that fools")

        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
