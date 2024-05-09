from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EsportsTourManagementSystem(object):
    def setupUi(self, EsportsTourManagementSystem):
        EsportsTourManagementSystem.setObjectName("EsportsTourManagementSystem")
        EsportsTourManagementSystem.resize(800, 600)
        EsportsTourManagementSystem.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.977273 rgba(250, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        
        self.centralwidget = QtWidgets.QWidget(EsportsTourManagementSystem)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(-4, 0, 811, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Header.setFont(font)
        self.Header.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.977273 rgba(250, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setObjectName("Header")
        
        self.teamname = QtWidgets.QLineEdit(self.centralwidget)
        self.teamname.setGeometry(QtCore.QRect(20, 70, 101, 20))
        self.teamname.setStyleSheet("color: rgb(255, 255, 255);")
        self.teamname.setObjectName("teamname")
        
        self.teamregion = QtWidgets.QLineEdit(self.centralwidget)
        self.teamregion.setGeometry(QtCore.QRect(150, 70, 101, 20))
        self.teamregion.setStyleSheet("color: rgb(255, 255, 255);")
        self.teamregion.setObjectName("teamregion")
        
        self.position = QtWidgets.QComboBox(self.centralwidget)
        self.position.setGeometry(QtCore.QRect(290, 70, 81, 21))
        self.position.setStyleSheet("color: rgb(255, 255, 255);")
        self.position.setObjectName("position")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        
        self.points = QtWidgets.QLineEdit(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(410, 70, 101, 21))
        self.points.setStyleSheet("color: rgb(255, 255, 255);")
        self.points.setObjectName("points")
        
        self.tmnamelabel = QtWidgets.QLabel(self.centralwidget)
        self.tmnamelabel.setGeometry(QtCore.QRect(20, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tmnamelabel.setFont(font)
        self.tmnamelabel.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.tmnamelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tmnamelabel.setObjectName("tmnamelabel")
        
        self.teamregionlabel = QtWidgets.QLabel(self.centralwidget)
        self.teamregionlabel.setGeometry(QtCore.QRect(150, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.teamregionlabel.setFont(font)
        self.teamregionlabel.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.teamregionlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.teamregionlabel.setObjectName("teamregionlabel")
        
        self.poslabel = QtWidgets.QLabel(self.centralwidget)
        self.poslabel.setGeometry(QtCore.QRect(280, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.poslabel.setFont(font)
        self.poslabel.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.poslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.poslabel.setObjectName("poslabel")
        self.pntlabel = QtWidgets.QLabel(self.centralwidget)
        self.pntlabel.setGeometry(QtCore.QRect(410, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.pntlabel.setFont(font)
        self.pntlabel.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pntlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pntlabel.setObjectName("pntlabel")
        
        self.TeamsInfo = QtWidgets.QListWidget(self.centralwidget)
        self.TeamsInfo.setGeometry(QtCore.QRect(0, 220, 801, 381))
        self.TeamsInfo.setStyleSheet("color: rgb(255, 255, 255);")
        self.TeamsInfo.setObjectName("TeamsInfo")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 150, 75, 23))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.977273 rgba(250, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_info)
        EsportsTourManagementSystem.setCentralWidget(self.centralwidget)

        self.retranslateUi(EsportsTourManagementSystem)
        QtCore.QMetaObject.connectSlotsByName(EsportsTourManagementSystem)

    def retranslateUi(self, EsportsTourManagementSystem):
        _translate = QtCore.QCoreApplication.translate
        EsportsTourManagementSystem.setWindowTitle(_translate("EsportsTourManagementSystem", "MainWindow"))
        self.Header.setText(_translate("EsportsTourManagementSystem", "Esports Tournament Management System"))
        self.position.setItemText(0, _translate("EsportsTourManagementSystem", "1"))
        self.position.setItemText(1, _translate("EsportsTourManagementSystem", "2"))
        self.position.setItemText(2, _translate("EsportsTourManagementSystem", "3"))
        self.position.setItemText(3, _translate("EsportsTourManagementSystem", "4"))
        self.position.setItemText(4, _translate("EsportsTourManagementSystem", "5"))
        self.position.setItemText(5, _translate("EsportsTourManagementSystem", "7"))
        self.position.setItemText(6, _translate("EsportsTourManagementSystem", "8"))
        self.position.setItemText(7, _translate("EsportsTourManagementSystem", "9"))
        self.position.setItemText(8, _translate("EsportsTourManagementSystem", "10"))
        self.position.setItemText(9, _translate("EsportsTourManagementSystem", "Desqualify"))
        self.tmnamelabel.setText(_translate("EsportsTourManagementSystem", "Team name"))
        self.teamregionlabel.setText(_translate("EsportsTourManagementSystem", "Team Region"))
        self.poslabel.setText(_translate("EsportsTourManagementSystem", "Position"))
        self.pntlabel.setText(_translate("EsportsTourManagementSystem", "Points"))
        self.pushButton.setText(_translate("EsportsTourManagementSystem", "ADD"))
    
    def add_info(self):
        tm_name = self.teamname.text()
        tm_regn = self.teamregion.text()
        pos = self.position.currentText()
        pnt = self.points.text()
        all_info = f"Team Name: {tm_name}, Team Region: {tm_regn}, Team Position: {pos}, Team Points: {pnt}"
        self.TeamsInfo.addItem(all_info)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EsportsTourManagementSystem = QtWidgets.QMainWindow()
    ui = Ui_EsportsTourManagementSystem()
    ui.setupUi(EsportsTourManagementSystem)
    EsportsTourManagementSystem.show()
    sys.exit(app.exec_())
