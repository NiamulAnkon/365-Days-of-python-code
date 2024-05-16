from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(18, 20, 28);")
        MainWindow.setWindowTitle("Personal Health Dashboard")
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
        self.label.setText("Personal Health Dashboard")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 801, 541))
        self.tabWidget.setObjectName("tabWidget")

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.setupTab1Ui(self.tab1)
        self.tabWidget.addTab(self.tab1, "Weight Tracker")

        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.setupTab2Ui(self.tab2)
        self.tabWidget.addTab(self.tab2, "Exercise Log")

        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.setupTab3Ui(self.tab3)
        self.tabWidget.addTab(self.tab3, "Water Intake")

        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.setupTab4Ui(self.tab4)
        self.tabWidget.addTab(self.tab4, "Diet Tracker")

        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.setupTab5Ui(self.tab5)
        self.tabWidget.addTab(self.tab5, "Health Goals")

        MainWindow.setCentralWidget(self.centralwidget)

    def setupTab1Ui(self, tab):
        layout = QtWidgets.QVBoxLayout(tab)
        label = QtWidgets.QLabel("Track your weight here")
        label.setStyleSheet("color: rgb(255, 255, 255);")
        layout.addWidget(label)
        tab.setLayout(layout)

    def setupTab2Ui(self, tab):
        layout = QtWidgets.QVBoxLayout(tab)
        label = QtWidgets.QLabel("Log your exercises here")
        label.setStyleSheet("color: rgb(255, 255, 255);")
        layout.addWidget(label)
        tab.setLayout(layout)

    def setupTab3Ui(self, tab):
        layout = QtWidgets.QVBoxLayout(tab)
        label = QtWidgets.QLabel("Monitor your water intake here")
        label.setStyleSheet("color: rgb(255, 255, 255);")
        layout.addWidget(label)
        tab.setLayout(layout)

    def setupTab4Ui(self, tab):
        layout = QtWidgets.QVBoxLayout(tab)
        label = QtWidgets.QLabel("Track your diet here")
        label.setStyleSheet("color: rgb(255, 255, 255);")
        layout.addWidget(label)
        tab.setLayout(layout)

    def setupTab5Ui(self, tab):
        layout = QtWidgets.QVBoxLayout(tab)
        label = QtWidgets.QLabel("Set and monitor your health goals here")
        label.setStyleSheet("color: rgb(255, 255, 255);")
        layout.addWidget(label)
        tab.setLayout(layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
