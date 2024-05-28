from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.381, y1:0.539955, x2:0.551, y2:0.454545, stop:0 rgba(255, 0, 151, 255), stop:1 rgba(91, 38, 38, 255));\n"
"color: rgb(255, 255, 255);")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.culab = QtWidgets.QLabel(self.centralwidget)
        self.culab.setGeometry(QtCore.QRect(10, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.culab.setFont(font)
        self.culab.setAlignment(QtCore.Qt.AlignCenter)
        self.culab.setObjectName("culab")

        self.wiwglab = QtWidgets.QLabel(self.centralwidget)
        self.wiwglab.setGeometry(QtCore.QRect(130, 60, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wiwglab.setFont(font)
        self.wiwglab.setAlignment(QtCore.Qt.AlignCenter)
        self.wiwglab.setObjectName("wiwglab")

        self.cmbtlab = QtWidgets.QLabel(self.centralwidget)
        self.cmbtlab.setGeometry(QtCore.QRect(290, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbtlab.setFont(font)
        self.cmbtlab.setAlignment(QtCore.Qt.AlignCenter)
        self.cmbtlab.setObjectName("cmbtlab")

        self.crdtp = QtWidgets.QComboBox(self.centralwidget)
        self.crdtp.setGeometry(QtCore.QRect(490, 110, 101, 22))
        self.crdtp.setObjectName("crdtp")
        self.crdtp.addItem("")
        self.crdtp.addItem("")

        self.ctlab = QtWidgets.QLabel(self.centralwidget)
        self.ctlab.setGeometry(QtCore.QRect(470, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ctlab.setFont(font)
        self.ctlab.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlab.setObjectName("ctlab")

        self.iwlgv = QtWidgets.QLineEdit(self.centralwidget)
        self.iwlgv.setGeometry(QtCore.QRect(170, 110, 113, 20))
        self.iwlgv.setObjectName("iwlgv")

        self.crdmnbdytxt = QtWidgets.QLineEdit(self.centralwidget)
        self.crdmnbdytxt.setGeometry(QtCore.QRect(310, 110, 113, 20))
        self.crdmnbdytxt.setObjectName("crdmnbdytxt")

        self.crdinfo = QtWidgets.QLineEdit(self.centralwidget)
        self.crdinfo.setGeometry(QtCore.QRect(10, 110, 141, 91))
        self.crdinfo.setObjectName("crdinfo")

        self.addbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addbtn.setGeometry(QtCore.QRect(320, 210, 101, 41))
        self.addbtn.setObjectName("addbtn")
        self.addbtn.clicked.connect(self.add_cards_list)

        self.crdlist = QtWidgets.QListWidget(self.centralwidget)
        self.crdlist.setGeometry(QtCore.QRect(0, 280, 801, 321))
        self.crdlist.setObjectName("crdlist")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Card Distribution System"))
        self.culab.setText(_translate("MainWindow", "Card info"))
        self.wiwglab.setText(_translate("MainWindow", "who i will give"))
        self.cmbtlab.setText(_translate("MainWindow", "Card Main body texts"))
        self.crdtp.setItemText(0, _translate("MainWindow", "Wedding"))
        self.crdtp.setItemText(1, _translate("MainWindow", "invitation"))
        self.ctlab.setText(_translate("MainWindow", "Card Type"))
        self.addbtn.setText(_translate("MainWindow", "Add Card to list"))
    
    def add_cards_list(self):
        card_main_body_text = self.crdmnbdytxt.text()
        card_info = self.crdinfo.text()
        card_iwillgive = self.iwlgv.text()
        card_type = self.crdtp.currentText()
        info = f"Card Main Body Text: {card_main_body_text} Card Info: {card_info} Who i WIll give: {card_iwillgive} Card TYpe: {card_type}"
        self.crdlist.addItem(info)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
