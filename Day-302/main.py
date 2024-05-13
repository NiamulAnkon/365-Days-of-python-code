from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 599)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.909, x2:0.619, y2:0.460227, stop:0 rgba(0, 255, 50, 255), stop:1 rgba(245, 227, 0, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setStyleSheet("background-color: rgb(0, 255, 72);")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        
        self.plntname_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.plntname_2.setGeometry(QtCore.QRect(10, 110, 113, 20))
        self.plntname_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plntname_2.setObjectName("plntname_2")
        
        self.plntname = QtWidgets.QLabel(self.centralwidget)
        self.plntname.setGeometry(QtCore.QRect(10, 80, 111, 20))
        self.plntname.setObjectName("plntname")

        self.dissesname = QtWidgets.QLineEdit(self.centralwidget)
        self.dissesname.setGeometry(QtCore.QRect(150, 110, 113, 20))
        self.dissesname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dissesname.setObjectName("dissesname")

        self.disslabel = QtWidgets.QLabel(self.centralwidget)
        self.disslabel.setGeometry(QtCore.QRect(150, 80, 111, 20))
        self.disslabel.setObjectName("disslabel")

        self.waterlabel = QtWidgets.QLabel(self.centralwidget)
        self.waterlabel.setGeometry(QtCore.QRect(290, 80, 141, 20))
        self.waterlabel.setObjectName("waterlabel")

        self.waterinntimes = QtWidgets.QLineEdit(self.centralwidget)
        self.waterinntimes.setGeometry(QtCore.QRect(290, 110, 131, 20))
        self.waterinntimes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.waterinntimes.setObjectName("waterinntimes")

        self.idornumber = QtWidgets.QComboBox(self.centralwidget)
        self.idornumber.setGeometry(QtCore.QRect(460, 110, 121, 22))
        self.idornumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idornumber.setObjectName("idornumber")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")
        self.idornumber.addItem("")

        self.idornumberlabel = QtWidgets.QLabel(self.centralwidget)
        self.idornumberlabel.setGeometry(QtCore.QRect(450, 80, 141, 20))
        self.idornumberlabel.setObjectName("idornumberlabel")

        self.listofplants = QtWidgets.QListWidget(self.centralwidget)
        self.listofplants.setGeometry(QtCore.QRect(0, 230, 801, 371))
        self.listofplants.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listofplants.setObjectName("listofplants")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Garden Management System"))
        self.plntname.setText(_translate("MainWindow", "Plant name or type"))
        self.disslabel.setText(_translate("MainWindow", "Any disses"))
        self.waterlabel.setText(_translate("MainWindow", "Watering time for everyday"))
        self.idornumber.setItemText(0, _translate("MainWindow", "1"))
        self.idornumber.setItemText(1, _translate("MainWindow", "2"))
        self.idornumber.setItemText(2, _translate("MainWindow", "3"))
        self.idornumber.setItemText(3, _translate("MainWindow", "4"))
        self.idornumber.setItemText(4, _translate("MainWindow", "5"))
        self.idornumber.setItemText(5, _translate("MainWindow", "6"))
        self.idornumber.setItemText(6, _translate("MainWindow", "7"))
        self.idornumber.setItemText(7, _translate("MainWindow", "8"))
        self.idornumber.setItemText(8, _translate("MainWindow", "9"))
        self.idornumber.setItemText(9, _translate("MainWindow", "10"))
        self.idornumber.setItemText(10, _translate("MainWindow", "11"))
        self.idornumber.setItemText(11, _translate("MainWindow", "12"))
        self.idornumber.setItemText(12, _translate("MainWindow", "13"))
        self.idornumber.setItemText(13, _translate("MainWindow", "14"))
        self.idornumber.setItemText(14, _translate("MainWindow", "15"))
        self.idornumber.setItemText(15, _translate("MainWindow", "16"))
        self.idornumber.setItemText(16, _translate("MainWindow", "17"))
        self.idornumber.setItemText(17, _translate("MainWindow", "18"))
        self.idornumber.setItemText(18, _translate("MainWindow", "19"))
        self.idornumber.setItemText(19, _translate("MainWindow", "20"))
        self.idornumberlabel.setText(_translate("MainWindow", "Flower id or number"))
    
    def add_plants(self):
        plant_name = self.plntname.text()
        watering_time = self.waterinntimes.text()
        disses_name = self.dissesname.text()
        id_num = self.idornumber.currentText()
        plant_info = f"Plant Name: {plant_name}, Watering Times: {watering_time}, Disses Name: {disses_name}, Id or Num: {id_num}"
        self.listofplants.addItem(plant_info)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
