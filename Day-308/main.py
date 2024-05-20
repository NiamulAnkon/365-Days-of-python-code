from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.307227, y1:0.557, x2:0.591, y2:0.551136, stop:0 rgba(0, 255, 7, 255), stop:1 rgba(0, 104, 255, 255));")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.psgnmlab = QtWidgets.QLabel(self.centralwidget)
        self.psgnmlab.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.psgnmlab.setObjectName("psgnmlab")

        self.datlab = QtWidgets.QLabel(self.centralwidget)
        self.datlab.setGeometry(QtCore.QRect(160, 90, 47, 13))
        self.datlab.setObjectName("datlab")

        self.fromlab = QtWidgets.QLabel(self.centralwidget)
        self.fromlab.setGeometry(QtCore.QRect(290, 90, 47, 13))
        self.fromlab.setObjectName("fromlab")

        self.tolab = QtWidgets.QLabel(self.centralwidget)
        self.tolab.setGeometry(QtCore.QRect(410, 90, 47, 13))
        self.tolab.setObjectName("tolab")

        self.priclab = QtWidgets.QLabel(self.centralwidget)
        self.priclab.setGeometry(QtCore.QRect(540, 90, 47, 13))
        self.priclab.setObjectName("priclab")

        self.sitlab = QtWidgets.QLabel(self.centralwidget)
        self.sitlab.setGeometry(QtCore.QRect(620, 90, 47, 13))
        self.sitlab.setObjectName("sitlab")

        self.ticidlab = QtWidgets.QLabel(self.centralwidget)
        self.ticidlab.setGeometry(QtCore.QRect(720, 90, 61, 16))
        self.ticidlab.setObjectName("ticidlab")

        self.psgname = QtWidgets.QLineEdit(self.centralwidget)
        self.psgname.setGeometry(QtCore.QRect(10, 110, 113, 20))
        self.psgname.setObjectName("psgname")

        self.date = QtWidgets.QLineEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(140, 110, 113, 20))
        self.date.setObjectName("date")

        self.frm = QtWidgets.QLineEdit(self.centralwidget)
        self.frm.setGeometry(QtCore.QRect(270, 110, 113, 20))
        self.frm.setObjectName("frm")

        self.to = QtWidgets.QLineEdit(self.centralwidget)
        self.to.setGeometry(QtCore.QRect(400, 110, 113, 20))
        self.to.setObjectName("to")

        self.prc = QtWidgets.QLineEdit(self.centralwidget)
        self.prc.setGeometry(QtCore.QRect(520, 110, 81, 20))
        self.prc.setObjectName("prc")

        self.stno = QtWidgets.QComboBox(self.centralwidget)
        self.stno.setGeometry(QtCore.QRect(620, 110, 61, 22))
        self.stno.setObjectName("stno")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")
        self.stno.addItem("")

        self.ticid = QtWidgets.QLineEdit(self.centralwidget)
        self.ticid.setGeometry(QtCore.QRect(710, 110, 81, 20))
        self.ticid.setObjectName("ticid")

        self.addbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addbtn.setGeometry(QtCore.QRect(340, 170, 81, 31))
        self.addbtn.setObjectName("addbtn")
        self.addbtn.clicked.connect(self.add_info)

        self.ticketlist = QtWidgets.QListWidget(self.centralwidget)
        self.ticketlist.setGeometry(QtCore.QRect(0, 220, 801, 381))
        self.ticketlist.setObjectName("ticketlist")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Bus Ticket Management System"))
        self.psgnmlab.setText(_translate("MainWindow", "Pasanger name"))
        self.datlab.setText(_translate("MainWindow", "Date"))
        self.fromlab.setText(_translate("MainWindow", "from"))
        self.tolab.setText(_translate("MainWindow", "to"))
        self.priclab.setText(_translate("MainWindow", "Price"))
        self.sitlab.setText(_translate("MainWindow", "Seat no"))
        self.ticidlab.setText(_translate("MainWindow", "Ticket id"))
        self.stno.setItemText(0, _translate("MainWindow", "a1"))
        self.stno.setItemText(1, _translate("MainWindow", "a2"))
        self.stno.setItemText(2, _translate("MainWindow", "a3"))
        self.stno.setItemText(3, _translate("MainWindow", "a4"))
        self.stno.setItemText(4, _translate("MainWindow", "b1"))
        self.stno.setItemText(5, _translate("MainWindow", "b2"))
        self.stno.setItemText(6, _translate("MainWindow", "b3"))
        self.stno.setItemText(7, _translate("MainWindow", "b4"))
        self.stno.setItemText(8, _translate("MainWindow", "c1"))
        self.stno.setItemText(9, _translate("MainWindow", "c2"))
        self.stno.setItemText(10, _translate("MainWindow", "c3"))
        self.stno.setItemText(11, _translate("MainWindow", "c4"))
        self.addbtn.setText(_translate("MainWindow", "Add info"))
    
    def add_info(self):
        pessanger_name = self.psgname.text()
        date = self.date.text()
        fromplc = self.frm.text()
        to = self.to.text()
        price = self.prc.text()
        seatno = self.stno.currentText()
        ticket_id = self.ticid.text()
        info = f"Pessanger Name: {pessanger_name}, Date: {date}, From: {fromplc}, To: {to}, Price: {price}, Seat No: {seatno}, Ticket Id: {ticket_id}"
        self.ticketlist.addItem(info)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
