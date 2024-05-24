# ui_mainwindow.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 800, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 60, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")

        self.titleInput = QtWidgets.QLineEdit(self.centralwidget)
        self.titleInput.setGeometry(QtCore.QRect(120, 60, 200, 30))
        self.titleInput.setObjectName("titleInput")

        self.authorLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorLabel.setGeometry(QtCore.QRect(10, 100, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.authorLabel.setFont(font)
        self.authorLabel.setObjectName("authorLabel")

        self.authorInput = QtWidgets.QLineEdit(self.centralwidget)
        self.authorInput.setGeometry(QtCore.QRect(120, 100, 200, 30))
        self.authorInput.setObjectName("authorInput")

        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setGeometry(QtCore.QRect(10, 140, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yearLabel.setFont(font)
        self.yearLabel.setObjectName("yearLabel")

        self.yearInput = QtWidgets.QLineEdit(self.centralwidget)
        self.yearInput.setGeometry(QtCore.QRect(120, 140, 200, 30))
        self.yearInput.setObjectName("yearInput")

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(340, 60, 100, 30))
        self.addButton.setObjectName("addButton")

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(340, 100, 100, 30))
        self.deleteButton.setObjectName("deleteButton")

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(340, 140, 100, 30))
        self.saveButton.setObjectName("saveButton")

        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(450, 140, 100, 30))
        self.loadButton.setObjectName("loadButton")

        self.bookList = QtWidgets.QListWidget(self.centralwidget)
        self.bookList.setGeometry(QtCore.QRect(10, 200, 780, 350))
        self.bookList.setObjectName("bookList")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Book Collection Manager"))
        self.header.setText(_translate("MainWindow", "Book Collection Manager"))
        self.titleLabel.setText(_translate("MainWindow", "Title:"))
        self.authorLabel.setText(_translate("MainWindow", "Author:"))
        self.yearLabel.setText(_translate("MainWindow", "Year:"))
        self.addButton.setText(_translate("MainWindow", "Add Book"))
        self.deleteButton.setText(_translate("MainWindow", "Delete Book"))
        self.saveButton.setText(_translate("MainWindow", "Save to CSV"))
        self.loadButton.setText(_translate("MainWindow", "Load from CSV"))
