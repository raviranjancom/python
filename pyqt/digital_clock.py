from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt,QTimer
import sys
import datetime
import time

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() 
        self.label=QLabel(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(500,400,1000,200)
        self.setWindowIcon(QIcon("graphics/favicon.png"))
        self.setWindowTitle("Digital Clock")

        self.label=QLabel(self)
        self.label.setGeometry(0,0,1000,200)
        self.label.setStyleSheet("background-color: black; color:green; font-size:150px")
        self.label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        QTimer.singleShot(0, self.run_clock)

    def run_clock(self):
        while True:
            self.initClock()
            QApplication.processEvents()
            time.sleep(1)

    def initClock(self):
        time=datetime.datetime.now()
        time=time.strftime("%H : %M : %S")
        self.label.setText(str(time))

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()

