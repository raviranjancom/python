from PyQt5.QtWidgets import QApplication,QBoxLayout,QMainWindow,QVBoxLayout,QHBoxLayout,QGridLayout,QLabel,QWidget,QPushButton,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QFont,QPixmap,QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,500)
        self.text_box=QLineEdit(self)
        self.submit_button = QPushButton("Submit",self)
        
        self.initUI()

    def initUI(self):
        self.text_box.setGeometry(0,0,300,40)
        self.text_box.setPlaceholderText("Enter your name.... ")
        self.submit_button.setGeometry(310,10,80,30)
        self.submit_button.clicked.connect(self.fun)
    
    def fun(self):
        self.submit_button.setText("Yo!")
        self.submit_button.setDisabled(True)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
