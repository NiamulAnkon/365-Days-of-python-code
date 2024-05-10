from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(18, 20, 28);")
        MainWindow.setWindowTitle("Rubik's Cube Timer")  # Fixed typo here
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Rubik's Cube Timer By Ankon")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 150, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 270, 75, 23))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Start")
        self.pushButton.clicked.connect(self.start_stop_timer)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 320, 801, 281))
        self.listWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer_running = False
        self.start_time = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Stop"))

    def start_stop_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = QtCore.QTime.currentTime()
            self.pushButton.setText("Stop")
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(self.update_timer)
            self.timer.start(100)  # Update timer display every 100 milliseconds
        else:
            self.timer_running = False
            self.pushButton.setText("Start")
            self.timer.stop()
            elapsed_time = self.start_time.msecsTo(QtCore.QTime.currentTime())
            self.label_2.setText("Time: " + QtCore.QTime().addMSecs(elapsed_time).toString("hh:mm:ss.zzz"))

    def update_timer(self):
        elapsed_time = self.start_time.msecsTo(QtCore.QTime.currentTime())
        self.label_2.setText("Time: " + QtCore.QTime().addMSecs(elapsed_time).toString("hh:mm:ss.zzz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
