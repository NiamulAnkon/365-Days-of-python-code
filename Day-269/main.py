import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QMessageBox, QVBoxLayout, QWidget, QPushButton, QFileDialog

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Text Editor')
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Create a menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')

        # Add actions to the file menu
        open_action = QAction('&Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if filename:
            try:
                with open(filename, 'r') as file:
                    self.text_edit.setText(file.read())
            except Exception as e:
                QMessageBox.warning(self, 'Error', str(e))

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if filename:
            try:
                with open(filename, 'w') as file:
                    file.write(self.text_edit.toPlainText())
            except Exception as e:
                QMessageBox.warning(self, 'Error', str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
