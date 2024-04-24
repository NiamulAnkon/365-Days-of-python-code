from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets, QtMultimedia

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(60, 255, 48, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.video_widget = QtMultimediaWidgets.QVideoWidget(self.centralwidget)
        self.video_widget.setGeometry(QtCore.QRect(50, 50, 700, 400))
        self.video_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.video_widget.setObjectName("video_widget")
        
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(200, 480, 75, 23))
        self.play_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.play_button.setObjectName("play_button")
        self.play_button.clicked.connect(self.play_video)
        
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(400, 480, 75, 23))
        self.stop_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stop_button.setObjectName("stop_button")
        self.stop_button.clicked.connect(self.stop_video)
        
        self.add_video_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_video_button.setGeometry(QtCore.QRect(300, 530, 150, 23))
        self.add_video_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_video_button.setObjectName("add_video_button")
        self.add_video_button.clicked.connect(self.add_video)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.media_player = QtMultimedia.QMediaPlayer()  
        self.media_player.setVideoOutput(self.video_widget)  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Player"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.add_video_button.setText(_translate("MainWindow", "Add Video"))
    
    def play_video(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open Video File', '', 'Video Files (*.mp4 *.avi *.mkv)')  
        if file_path:
            self.media_player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_path)))  
            self.media_player.play()  

    def stop_video(self):
        self.media_player.stop()  

    def add_video(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open Video File', '', 'Video Files (*.mp4 *.avi *.mkv)')  
        if file_path:
            self.media_player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_path)))  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
