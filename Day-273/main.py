import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Enter an expression')

        
        buttons = [
            ('7', self.on_button_clicked), ('8', self.on_button_clicked), ('9', self.on_button_clicked), ('/', self.on_button_clicked),
            ('4', self.on_button_clicked), ('5', self.on_button_clicked), ('6', self.on_button_clicked), ('*', self.on_button_clicked),
            ('1', self.on_button_clicked), ('2', self.on_button_clicked), ('3', self.on_button_clicked), ('-', self.on_button_clicked),
            ('C', self.clear_input), ('0', self.on_button_clicked), ('=', self.calculate_result), ('+', self.on_button_clicked)
        ]

        
        for text, callback in buttons:
            button = QPushButton(text)
            button.clicked.connect(callback)
            layout.addWidget(button)

        layout.addWidget(self.input_field)
        self.setLayout(layout)

    def on_button_clicked(self):
        button = self.sender()
        text = button.text()
        current_text = self.input_field.text()
        self.input_field.setText(current_text + text)

    def clear_input(self):
        self.input_field.clear()

    def calculate_result(self):
        expression = self.input_field.text()
        try:
            result = eval(expression)
            self.input_field.setText(str(result))
        except Exception as e:
            self.input_field.setText('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
