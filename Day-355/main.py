import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')

        self.vbox = QVBoxLayout()

        self.display = QLineEdit(self)
        self.vbox.addWidget(self.display)

        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', 'C', '=', '+']
        ]

        for row in self.buttons:
            hbox = QHBoxLayout()
            for button in row:
                btn = QPushButton(button, self)
                btn.clicked.connect(self.on_click)
                hbox.addWidget(btn)
            self.vbox.addLayout(hbox)

        self.setLayout(self.vbox)

    def on_click(self):
        sender = self.sender().text()
        if sender == '=':
            try:
                expression = self.display.text()
                result = self.calculate(expression)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        elif sender == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + sender)

    def calculate(self, expression):
        try:
            # Basic parsing to determine the operation
            if '+' in expression:
                num1, num2 = map(float, expression.split('+'))
                operation = 'add'
            elif '-' in expression:
                num1, num2 = map(float, expression.split('-'))
                operation = 'subtract'
            elif '*' in expression:
                num1, num2 = map(float, expression.split('*'))
                operation = 'multiply'
            elif '/' in expression:
                num1, num2 = map(float, expression.split('/'))
                operation = 'divide'
            else:
                raise ValueError("Invalid expression")

            response = requests.post('http://127.0.0.1:5000/calculate', json={'operation': operation, 'num1': num1, 'num2': num2})
            response_data = response.json()

            if response.status_code != 200:
                raise ValueError(response_data['error'])

            return response_data['result']
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return 'Error'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
