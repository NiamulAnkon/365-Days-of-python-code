from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FoodManagementApp(object):
    def setupUi(self, FoodManagementApp):
        FoodManagementApp.setObjectName("FoodManagementApp")
        FoodManagementApp.resize(800, 600)
        FoodManagementApp.setStyleSheet("background-color: rgb(80, 80, 80);")
        self.centralwidget = QtWidgets.QWidget(FoodManagementApp)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header.setFont(font)
        self.header.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.381, y1:0.539955, x2:0.551, y2:0.454545, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 194, 0, 255));\n"
"color: qlineargradient(spread:pad, x1:0.381, y1:0.539955, x2:0.551, y2:0.454545, stop:0 rgba(62, 0, 120, 255), stop:1 rgba(36, 255, 0, 255));")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.csnmlab = QtWidgets.QLabel(self.centralwidget)
        self.csnmlab.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.csnmlab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.csnmlab.setAlignment(QtCore.Qt.AlignCenter)
        self.csnmlab.setObjectName("csnmlab")

        self.orditmlab = QtWidgets.QLabel(self.centralwidget)
        self.orditmlab.setGeometry(QtCore.QRect(130, 50, 91, 21))
        self.orditmlab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.orditmlab.setAlignment(QtCore.Qt.AlignCenter)
        self.orditmlab.setObjectName("orditmlab")

        self.oiqlab = QtWidgets.QLabel(self.centralwidget)
        self.oiqlab.setGeometry(QtCore.QRect(240, 50, 111, 21))
        self.oiqlab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.oiqlab.setAlignment(QtCore.Qt.AlignCenter)
        self.oiqlab.setObjectName("oiqlab")

        self.odlab = QtWidgets.QLabel(self.centralwidget)
        self.odlab.setGeometry(QtCore.QRect(370, 50, 101, 21))
        self.odlab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.odlab.setAlignment(QtCore.Qt.AlignCenter)
        self.odlab.setObjectName("odlab")

        self.stslab = QtWidgets.QLabel(self.centralwidget)
        self.stslab.setGeometry(QtCore.QRect(480, 50, 101, 21))
        self.stslab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stslab.setAlignment(QtCore.Qt.AlignCenter)
        self.stslab.setObjectName("stslab")

        self.crsnm = QtWidgets.QLineEdit(self.centralwidget)
        self.crsnm.setGeometry(QtCore.QRect(0, 80, 113, 20))
        self.crsnm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.crsnm.setObjectName("crsnm")

        self.oi = QtWidgets.QLineEdit(self.centralwidget)
        self.oi.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.oi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.oi.setObjectName("oi")

        self.oiq = QtWidgets.QLineEdit(self.centralwidget)
        self.oiq.setGeometry(QtCore.QRect(240, 80, 113, 20))
        self.oiq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.oiq.setObjectName("oiq")

        self.od = QtWidgets.QLineEdit(self.centralwidget)
        self.od.setGeometry(QtCore.QRect(360, 80, 113, 20))
        self.od.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.od.setObjectName("od")

        self.sts = QtWidgets.QComboBox(self.centralwidget)
        self.sts.setGeometry(QtCore.QRect(480, 80, 101, 21))
        self.sts.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sts.setObjectName("sts")
        self.sts.addItem("")
        self.sts.addItem("")
        self.sts.addItem("")
        self.sts.addItem("")

        self.foodorderlist = QtWidgets.QListWidget(self.centralwidget)
        self.foodorderlist.setGeometry(QtCore.QRect(0, 250, 801, 351))
        self.foodorderlist.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.foodorderlist.setObjectName("foodorderlist")

        self.addords = QtWidgets.QPushButton(self.centralwidget)
        self.addords.setGeometry(QtCore.QRect(330, 170, 101, 31))
        self.addords.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.addords.setObjectName("addords")
        self.addords.clicked.connect(self.add_ords)
        FoodManagementApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(FoodManagementApp)
        QtCore.QMetaObject.connectSlotsByName(FoodManagementApp)

    def retranslateUi(self, FoodManagementApp):
        _translate = QtCore.QCoreApplication.translate
        FoodManagementApp.setWindowTitle(_translate("FoodManagementApp", "MainWindow"))
        self.header.setText(_translate("FoodManagementApp", "Food Deliveries Management App"))
        self.csnmlab.setText(_translate("FoodManagementApp", "Customer\'s Name"))
        self.orditmlab.setText(_translate("FoodManagementApp", "Orderd item"))
        self.oiqlab.setText(_translate("FoodManagementApp", "Orderd item quantity"))
        self.odlab.setText(_translate("FoodManagementApp", "Order date"))
        self.stslab.setText(_translate("FoodManagementApp", "Status"))
        self.sts.setItemText(0, _translate("FoodManagementApp", "Pending"))
        self.sts.setItemText(1, _translate("FoodManagementApp", "Cancle"))
        self.sts.setItemText(2, _translate("FoodManagementApp", "Complete"))
        self.sts.setItemText(3, _translate("FoodManagementApp", "On hold"))
        self.addords.setText(_translate("FoodManagementApp", "Add Orders"))
    
    def add_ords(self):
        customer_Name = self.crsnm.text()
        customer_ordered_item = self.oi.text()
        ordered_quantitiy = self.oiq.text()
        ordered_date = self.od.text()
        status = self.sts.currentText()
        infos = f"Customer Name: {customer_Name}, Ordered Item: {customer_ordered_item}, Ordered Item Quantity: {ordered_quantitiy}, Order Date: {ordered_date}, Status: {status}"
        self.foodorderlist.addItem(infos)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FoodManagementApp = QtWidgets.QMainWindow()
    ui = Ui_FoodManagementApp()
    ui.setupUi(FoodManagementApp)
    FoodManagementApp.show()
    sys.exit(app.exec_())
