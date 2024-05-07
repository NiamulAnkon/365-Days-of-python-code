from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 631)
        MainWindow.setStyleSheet("background-color: rgb(56, 143, 151);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.urlinp = QtWidgets.QLineEdit(self.centralwidget)
        self.urlinp.setGeometry(QtCore.QRect(0, 60, 801, 31))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.urlinp.setFont(font)
        self.urlinp.setStyleSheet("background-color: rgb(251, 173, 23);\n"
"color: rgb(255, 255, 255);")
        self.urlinp.setObjectName("urlinp")

        self.ScrapedData = QtWidgets.QTextBrowser(self.centralwidget)
        self.ScrapedData.setGeometry(QtCore.QRect(0, 90, 801, 521))
        self.ScrapedData.setStyleSheet("background-color: rgb(44, 74, 97);\n"
"color: rgb(255, 255, 255);")
        self.ScrapedData.setObjectName("ScrapedData")

        self.scrapebtn = QtWidgets.QPushButton(self.centralwidget)
        self.scrapebtn.setGeometry(QtCore.QRect(0, 610, 801, 23))
        self.scrapebtn.setStyleSheet("background-color: rgb(252, 249, 200);")
        self.scrapebtn.setObjectName("scrapebtn")
        self.scrapebtn.clicked.connect(self.scrapWeb)

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(210, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.urlinp.setPlaceholderText(_translate("MainWindow", "Enter Website Url"))
        self.ScrapedData.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.scrapebtn.setText(_translate("MainWindow", "Scrap"))
        self.header.setText(_translate("MainWindow", "Python WebScrapper Using Pyqt5"))

    def scrapWeb(self):
        lineedit = self.urlinp.text()
        html = urlopen(lineedit)
        bsobj = BeautifulSoup(html, 'lxml')
        self.ScrapedData.append(str(bsobj))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
