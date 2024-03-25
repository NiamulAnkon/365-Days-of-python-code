from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("Software")

    # lab = QLabel(window)
    # lab.setText("Hello World")
    # lab.setFont(QFont("Arial", 16))
    # lab.move(50, 100)
    lt = QVBoxLayout()

    lab = QLabel("Press The button to know everything")
    txt_box = QTextEdit()
    button = QPushButton("Press Me!")

    lt.addWidget(lab)
    lt.addWidget(txt_box)
    lt.addWidget(button)

    button.clicked.connect(lambda: on_clicked(txt_box.toPlainText()))

    window.setLayout(lt)

    window.show()
    app.exec_()

def on_clicked(msg):
    # msg = QMessageBox()
    # msg.setText("Hello World")
    # msg.exec_()
    msgs = QMessageBox()
    msgs.setText(msg)
    msgs.exec_()

if __name__ == "__main__":
    main()
