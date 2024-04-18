from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.verticalLayout.addWidget(self.pushButton_edit)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout.addWidget(self.pushButton_delete)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recipe Manager"))
        self.label.setText(_translate("MainWindow", "Recipes"))
        self.pushButton_add.setText(_translate("MainWindow", "Add Recipe"))
        self.pushButton_edit.setText(_translate("MainWindow", "Edit Recipe"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete Recipe"))


class RecipeManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_recipe)
        self.ui.pushButton_edit.clicked.connect(self.edit_recipe)
        self.ui.pushButton_delete.clicked.connect(self.delete_recipe)

    def add_recipe(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Add Recipe', 'Enter recipe name:')
        if ok and text:
            self.ui.listWidget.addItem(text)

    def edit_recipe(self):
        current_item = self.ui.listWidget.currentItem()
        if current_item:
            text, ok = QtWidgets.QInputDialog.getText(self, 'Edit Recipe', 'Enter new recipe name:', text=current_item.text())
            if ok and text:
                current_item.setText(text)

    def delete_recipe(self):
        current_item = self.ui.listWidget.currentItem()
        if current_item:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(current_item))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = RecipeManager()
    MainWindow.show()
    sys.exit(app.exec_())
