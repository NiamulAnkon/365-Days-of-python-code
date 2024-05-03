from PyQt5 import QtCore, QtGui, QtWidgets


class AddOrderWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddOrderWindow, self).__init__(parent)
        self.setWindowTitle("Add Order")
        self.setGeometry(100, 100, 400, 300)

        self.order_name_label = QtWidgets.QLabel("Order Name:")
        self.order_name_input = QtWidgets.QLineEdit()

        self.quantity_label = QtWidgets.QLabel("Quantity:")
        self.quantity_input = QtWidgets.QSpinBox()

        self.customer_name_label = QtWidgets.QLabel("Customer Name:")
        self.customer_name_input = QtWidgets.QLineEdit()

        self.address_label = QtWidgets.QLabel("Address:")
        self.address_input = QtWidgets.QLineEdit()

        self.price_label = QtWidgets.QLabel("Price:")
        self.price_input = QtWidgets.QLineEdit()

        self.status_label = QtWidgets.QLabel("Status:")
        self.status_input = QtWidgets.QComboBox()
        self.status_input.addItems(["Pending", "Canceled", "Complete"])

        self.date_label = QtWidgets.QLabel("Date:")
        self.date_input = QtWidgets.QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QtCore.QDate.currentDate())

        self.save_button = QtWidgets.QPushButton("Save")
        self.save_button.clicked.connect(self.save_order)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.order_name_label)
        layout.addWidget(self.order_name_input)
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.customer_name_label)
        layout.addWidget(self.customer_name_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)
        layout.addWidget(self.status_label)
        layout.addWidget(self.status_input)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_order(self):
        order_name = self.order_name_input.text()
        quantity = self.quantity_input.value()
        customer_name = self.customer_name_input.text()
        address = self.address_input.text()
        price = self.price_input.text()
        status = self.status_input.currentText()
        date = self.date_input.date().toString(QtCore.Qt.ISODate)

        order_details = f"{order_name} - Quantity: {quantity} - Customer: {customer_name} - Address: {address} - Price: {price} - Status: {status} - Date: {date}"

        self.parent().add_order_to_list(order_details)
        self.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 631)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.482636, y1:0.489, x2:0, y2:0, stop:0 rgba(140, 41, 0, 255), stop:0.977273 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 0));")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(210, 0, 381, 41))

        font = QtGui.QFont()
        font.setPointSize(22)

        self.Header.setFont(font)
        self.Header.setStyleSheet("color: rgb(255, 255, 255);")
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setObjectName("Header")

        self.addorderbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addorderbtn.setGeometry(QtCore.QRect(310, 70, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.addorderbtn.setFont(font)
        self.addorderbtn.setStyleSheet("background-color: rgb(255, 241, 34);\n"
"color: rgb(255, 0, 0);")
        self.addorderbtn.setObjectName("addorderbtn")
        self.addorderbtn.clicked.connect(self.show_add_order_window)

        self.dltorderbtn = QtWidgets.QPushButton(self.centralwidget)
        self.dltorderbtn.setGeometry(QtCore.QRect(310, 140, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.dltorderbtn.setFont(font)
        self.dltorderbtn.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 4);")
        self.dltorderbtn.setObjectName("dltorderbtn")

        self.edtorderbtn = QtWidgets.QPushButton(self.centralwidget)
        self.edtorderbtn.setGeometry(QtCore.QRect(310, 220, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edtorderbtn.setFont(font)
        self.edtorderbtn.setStyleSheet("background-color: rgb(34, 255, 34);\n"
"color: rgb(255, 0, 0);")
        self.edtorderbtn.setObjectName("edtorderbtn")
        
        self.orderlist = QtWidgets.QListWidget(self.centralwidget)
        self.orderlist.setGeometry(QtCore.QRect(0, 290, 851, 341))
        self.orderlist.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.orderlist.setObjectName("orderlist")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Header.setText(_translate("MainWindow", "Bakery Management system"))
        self.addorderbtn.setText(_translate("MainWindow", "Add Order"))
        self.dltorderbtn.setText(_translate("MainWindow", "Delete Order"))
        self.edtorderbtn.setText(_translate("MainWindow", "Edit Order"))

    def show_add_order_window(self):
        self.add_order_window = AddOrderWindow(self)
        self.add_order_window.show()

    def add_order_to_list(self, order_details):
        self.orderlist.addItem(order_details)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
