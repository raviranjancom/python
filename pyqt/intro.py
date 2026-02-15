from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon,QFont
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("COOl GUI")
        self.setGeometry(0,0,500,500)   # x, y, width, height 
        self.setWindowIcon(QIcon("C:/Users/Ravi/Documents/codes/python/graphics/favicon.png"))
        
        label=QLabel("Name : ",self)
        label.setFont(QFont("monospace", 30))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:tomato;" \
                            "background-color:cyan;")

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
