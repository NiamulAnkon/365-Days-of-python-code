from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import QtWidgets
import sys

def on_clicked():
    print("haha U Got Hacked +_+")

def main():
    app = QApplication(sys.argv)
    window =  QMainWindow()
    window.setGeometry(100,200, 300, 300)
    window.setWindowTitle("my toadays code")

    text = QLabel(window)
    text.setText("I am learning Code")
    text.move(30,20)

    btn = QtWidgets.QPushButton(window)
    btn.setText('Press :)')
    btn.move(50,60)
    btn.clicked.connect(on_clicked)


    window.show()

    sys.exit(app.exec())

main()


