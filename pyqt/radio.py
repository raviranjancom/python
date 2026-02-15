from PyQt5.QtWidgets import QApplication,QBoxLayout,QMainWindow,QVBoxLayout,QHBoxLayout,QGridLayout,QLabel,QWidget,QPushButton,QCheckBox,QRadioButton,QButtonGroup
from PyQt5.QtGui import QFont,QPixmap,QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,500)
        self.radio1=QRadioButton("Visa",self)
        
        self.radio2=QRadioButton("Mastercard",self)
        
        self.radio3=QRadioButton("UPI",self)
        self.button_group=QButtonGroup()
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,500,100)
        self.radio2.setGeometry(0,100,500,100)
        self.radio3.setGeometry(0,200,500,100)
        self.button_group.addButton(self.radio1)
        self.button_group.addButton(self.radio2)
        self.radio1.toggled.connect(self.fun)

    def fun(self):
        radio_button=self.sender()
        if (radio_button.isChecked()):
            print(f"{radio_button} is clicked")


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
