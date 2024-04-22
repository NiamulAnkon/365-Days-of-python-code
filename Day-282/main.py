from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(60, 255, 48, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(320, 0, 221, 81))

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        self.header.setFont(font)
        self.header.setObjectName("header")

        self.songlist = QtWidgets.QListWidget(self.centralwidget)
        self.songlist.setGeometry(QtCore.QRect(40, 120, 811, 341))
        self.songlist.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.songlist.setObjectName("songlist")

        self.songinp = QtWidgets.QLineEdit(self.centralwidget)
        self.songinp.setGeometry(QtCore.QRect(160, 480, 191, 31))
        self.songinp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.songinp.setObjectName("songinp")

        self.addsngbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addsngbtn.setGeometry(QtCore.QRect(410, 490, 75, 23))
        self.addsngbtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.addsngbtn.setObjectName("addsngbtn")
        self.addsngbtn.clicked.connect(self.addSongToList)

        self.footer = QtWidgets.QLabel(self.centralwidget)
        self.footer.setGeometry(QtCore.QRect(0, 573, 901, 31))
        self.footer.setText("")
        self.footer.setObjectName("footer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Song List Manager"))
        self.addsngbtn.setText(_translate("MainWindow", "Add Song"))

    def addSongToList(self):
        song_name = self.songinp.text().strip()
        if song_name:
            self.songlist.addItem(song_name)
            self.footer.setText(f'{song_name} added to your favorite songs!')
            self.songinp.clear()
        else:
            self.footer.setText('Please enter a song name to add!')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
