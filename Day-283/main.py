from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(60, 255, 48, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 41))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.songlist = QtWidgets.QListWidget(self.centralwidget)
        self.songlist.setGeometry(QtCore.QRect(20, 90, 761, 441))
        self.songlist.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.songlist.setObjectName("songlist")

        self.addsngbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addsngbtn.setGeometry(QtCore.QRect(100, 540, 111, 31))
        self.addsngbtn.setStyleSheet("background-color: rgb(76, 255, 0);")
        self.addsngbtn.setObjectName("addsngbtn")
        self.addsngbtn.clicked.connect(self.addSong)

        self.playsngbtn = QtWidgets.QPushButton(self.centralwidget)
        self.playsngbtn.setGeometry(QtCore.QRect(330, 540, 111, 31))
        self.playsngbtn.setStyleSheet("background-color: rgb(76, 255, 0);")
        self.playsngbtn.setObjectName("playsngbtn")
        self.playsngbtn.clicked.connect(self.playSelectedSong)

        self.stopsngbtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopsngbtn.setGeometry(QtCore.QRect(550, 540, 101, 31))
        self.stopsngbtn.setStyleSheet("background-color: rgb(76, 255, 0);")
        self.stopsngbtn.setObjectName("stopsngbtn")
        self.stopsngbtn.clicked.connect(self.stopPlaying)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.player = QtMultimedia.QMediaPlayer()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Song Player"))
        self.addsngbtn.setText(_translate("MainWindow", "Add song"))
        self.playsngbtn.setText(_translate("MainWindow", "play song"))
        self.stopsngbtn.setText(_translate("MainWindow", "stop song"))
    
    def addSong(self):
        file_dialog = QtWidgets.QFileDialog(self.centralwidget)  
        file_dialog.setNameFilter("MP3 Files (*.mp3)")
        file_dialog.setViewMode(QtWidgets.QFileDialog.List)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            for file_path in file_paths:
                song_name = QtCore.QFileInfo(file_path).fileName()
                self.songlist.addItem(song_name)

    def playSelectedSong(self):
        current_item = self.songlist.currentItem()
        if current_item:
            song_name = current_item.text()
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, 'Open File', '', 'Audio Files (*.mp3)')
            if file_path:
                self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_path)))
                self.player.play()
                # self.#().showMessage(f'Now playing: {song_name}')

    def stopPlaying(self):
        self.player.stop()
        # self.#().showMessage('Playback stopped')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
