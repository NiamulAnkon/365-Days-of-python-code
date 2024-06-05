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
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(10, 80, 761, 31))
        self.url.setText("")
        self.url.setObjectName("url")

        self.catg = QtWidgets.QComboBox(self.centralwidget)
        self.catg.setGeometry(QtCore.QRect(630, 160, 121, 22))
        self.catg.setObjectName("catg")
        self.catg.addItem("")
        self.catg.addItem("")
        self.catg.addItem("")

        self.catlab = QtWidgets.QLabel(self.centralwidget)
        self.catlab.setGeometry(QtCore.QRect(640, 120, 81, 31))
        self.catlab.setAlignment(QtCore.Qt.AlignCenter)
        self.catlab.setObjectName("catlab")

        self.addbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addbtn.setGeometry(QtCore.QRect(330, 140, 101, 41))
        self.addbtn.setObjectName("addbtn")
        self.addbtn.clicked.connect(self.add_websites)

        self.addurllab = QtWidgets.QLabel(self.centralwidget)
        self.addurllab.setGeometry(QtCore.QRect(340, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addurllab.setFont(font)
        self.addurllab.setAlignment(QtCore.Qt.AlignCenter)
        self.addurllab.setObjectName("addurllab")

        self.websitelist = QtWidgets.QListWidget(self.centralwidget)
        self.websitelist.setGeometry(QtCore.QRect(10, 290, 781, 301))
        self.websitelist.setObjectName("websitelist")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Save Website"))
        self.catg.setItemText(0, _translate("MainWindow", "Work"))
        self.catg.setItemText(1, _translate("MainWindow", "Fun"))
        self.catg.setItemText(2, _translate("MainWindow", "Scerect"))
        self.catlab.setText(_translate("MainWindow", "Catageory"))
        self.addbtn.setText(_translate("MainWindow", "Add Website"))
        self.addurllab.setText(_translate("MainWindow", "add url"))
    
    def add_websites(self):
        url = self.url.text()
        catageory = self.catg.currentText()
        info  = f"The Website Url: {url}, The Catageory of the site is: {catageory}"
        self.websitelist.addItem(info)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
