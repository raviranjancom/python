from PyQt5.QtWidgets import QApplication,QBoxLayout,QMainWindow,QVBoxLayout,QHBoxLayout,QGridLayout,QLabel,QWidget,QPushButton,QCheckBox
from PyQt5.QtGui import QFont,QPixmap,QIcon

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Mr. Robot")
        self.initUI()

    def initUI(self):
        self.count=0
        self.button=QPushButton("Click",self)
        self.button.setGeometry(100,100,100,100)
        self.button.setStyleSheet("background-color:tomato;font-size:20;")
        self.label=QLabel("Hallo",self)
        self.label.setGeometry(0,0,100,100)
        self.label.setStyleSheet("background-color:cyan;font-size:20;")
        self.button.clicked.connect(self.onclick)

    def onclick(self):
        self.count+=1
        self.label.setText(str(self.count))

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.setWindowIcon(QIcon("python/graphics/favicon.png"))

    
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

