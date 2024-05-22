from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(96, 113, 111);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.header.setFont(font)
        self.header.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.307227, y1:0.557, x2:0.591, y2:0.551136, stop:0 rgba(0, 255, 7, 255), stop:1 rgba(0, 104, 255, 255));")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.cnlabel = QtWidgets.QLabel(self.centralwidget)
        self.cnlabel.setGeometry(QtCore.QRect(10, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cnlabel.setFont(font)
        self.cnlabel.setObjectName("cnlabel")

        self.crsname = QtWidgets.QLineEdit(self.centralwidget)
        self.crsname.setGeometry(QtCore.QRect(10, 70, 113, 21))
        self.crsname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.crsname.setObjectName("crsname")

        self.cilab = QtWidgets.QLabel(self.centralwidget)
        self.cilab.setGeometry(QtCore.QRect(130, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cilab.setFont(font)
        self.cilab.setObjectName("cilab")

        self.cin = QtWidgets.QLineEdit(self.centralwidget)
        self.cin.setGeometry(QtCore.QRect(130, 70, 113, 21))
        self.cin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cin.setObjectName("cin")

        self.ctlab = QtWidgets.QLabel(self.centralwidget)
        self.ctlab.setGeometry(QtCore.QRect(270, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ctlab.setFont(font)
        self.ctlab.setObjectName("ctlab")

        self.cflab = QtWidgets.QLabel(self.centralwidget)
        self.cflab.setGeometry(QtCore.QRect(380, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cflab.setFont(font)
        self.cflab.setObjectName("cflab")
        self.cf = QtWidgets.QLineEdit(self.centralwidget)
        self.cf.setGeometry(QtCore.QRect(380, 70, 113, 21))
        self.cf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cf.setObjectName("cf")

        self.cdlab = QtWidgets.QLabel(self.centralwidget)
        self.cdlab.setGeometry(QtCore.QRect(500, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cdlab.setFont(font)
        self.cdlab.setObjectName("cdlab")
        self.cd = QtWidgets.QTextEdit(self.centralwidget)
        self.cd.setGeometry(QtCore.QRect(500, 70, 141, 131))
        self.cd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cd.setObjectName("cd")

        self.cplab = QtWidgets.QLabel(self.centralwidget)
        self.cplab.setGeometry(QtCore.QRect(650, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cplab.setFont(font)
        self.cplab.setObjectName("cplab")

        self.crslist = QtWidgets.QListWidget(self.centralwidget)
        self.crslist.setGeometry(QtCore.QRect(0, 290, 801, 311))
        self.crslist.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.crslist.setObjectName("crslist")

        self.cp = QtWidgets.QLineEdit(self.centralwidget)
        self.cp.setGeometry(QtCore.QRect(650, 70, 113, 21))
        self.cp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cp.setObjectName("cp")

        self.ct = QtWidgets.QLineEdit(self.centralwidget)
        self.ct.setGeometry(QtCore.QRect(260, 70, 113, 21))
        self.ct.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ct.setObjectName("ct")

        self.addbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addbtn.setGeometry(QtCore.QRect(320, 230, 75, 23))
        self.addbtn.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "background-color: rgb(255, 255, 255);")
        self.addbtn.setObjectName("addbtn")
        self.addbtn.clicked.connect(self.add_crs)

        self.addtcsv = QtWidgets.QPushButton(self.centralwidget)
        self.addtcsv.setGeometry(QtCore.QRect(430, 230, 75, 23))
        self.addtcsv.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.addtcsv.setObjectName("addtcsv")
        self.addtcsv.clicked.connect(self.save_all_to_csv)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "|CEBD| Course Manager"))
        self.cnlabel.setText(_translate("MainWindow", "Course name"))
        self.cilab.setText(_translate("MainWindow", "Course Instructructor"))
        self.ctlab.setText(_translate("MainWindow", "Course Type"))
        self.cflab.setText(_translate("MainWindow", "Course fee"))
        self.cdlab.setText(_translate("MainWindow", "Course Description"))
        self.cplab.setText(_translate("MainWindow", "Course Playlist"))
        self.addbtn.setText(_translate("MainWindow", "Add Course"))
        self.addtcsv.setText(_translate("MainWindow", "Add To Csv"))

    def add_crs(self):
        course_name = self.crsname.text()
        inst_name = self.cin.text()
        course_type = self.ct.text()
        course_des = self.cd.toPlainText()
        course_fee = self.cf.text()
        course_playlist = self.cp.text()
        info = f"Course Name: {course_name}, Instructor Name: {inst_name}, Course Type: {course_type}, Course Fee: {course_fee}, Course Playlist: {course_playlist}, Course Description: {course_des}"

        self.crslist.addItem(info)

    def save_all_to_csv(self):
        items = []
        for index in range(self.crslist.count()):
            item = self.crslist.item(index).text()
            course_details = dict(substring.split(": ", 1) for substring in item.split(", "))
            items.append(course_details)

        if items:
            file_exists = os.path.isfile('courses.csv')
            df = pd.DataFrame(items)
            if file_exists:
                df.to_csv('courses.csv', mode='a', header=False, index=False)
            else:
                df.to_csv('courses.csv', mode='w', header=True, index=False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
