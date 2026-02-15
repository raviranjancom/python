from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QVBoxLayout,QHBoxLayout,QGridLayout
from PyQt5.QtGui import QPixmap,QIcon,QFont
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("Bro Code")
        self.setWindowIcon(QIcon("python/graphics/favicon.png"))
        label=QLabel("Mr. Robot",self)
        label.setStyleSheet("background-color:black;color:white;")
        label.setFont(QFont("monospace",30))
        label.setGeometry(0,0,500,50)
        label.setAlignment(Qt.AlignCenter)
        

        # image label
        pixmap=QPixmap("python/graphics/favicon.png")

        img_label=QLabel(self)
        img_label.setPixmap(pixmap)
        img_label.setGeometry(0,50,250,250)
        img_label.setStyleSheet("background-color:blue;")
        img_label.setFont(QFont("monospace",10))
        img_label.setScaledContents(True)
        img_label.setGeometry(int(img_label.width()/2),int(img_label.height()/2),img_label.width(),img_label.height())
        
        
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
