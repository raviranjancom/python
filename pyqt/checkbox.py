from PyQt5.QtWidgets import QApplication,QBoxLayout,QMainWindow,QVBoxLayout,QHBoxLayout,QGridLayout,QLabel,QWidget,QPushButton,QCheckBox
from PyQt5.QtGui import QFont,QPixmap,QIcon

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Mr. Robot")
        self.checkbox=QCheckBox("Male",self)
        self.initUI()

    def initUI(self):
        self.checkbox.setStyleSheet("font-size:20px;")
        self.checkbox.stateChanged.connect(self.onclick)

    def onclick(self,state):
        if state==2:
            print("checked")
        else:
            print("unchecked")

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.setWindowIcon(QIcon("python/graphics/favicon.png"))

    
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

