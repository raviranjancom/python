from PyQt5.QtWidgets import QApplication,QBoxLayout,QMainWindow,QVBoxLayout,QHBoxLayout,QGridLayout,QLabel,QWidget
from PyQt5.QtGui import QFont,QPixmap,QIcon

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Mr. Robot")
        self.initUI()

    def initUI(self):
        main_widget=QWidget()
        self.setCentralWidget(main_widget)

        label1=QLabel("#1",self)
        label2=QLabel("#2",self)
        label3=QLabel("#3",self)
        label4=QLabel("#4",self)

        label1.setStyleSheet("background-color:tomato;")
        label2.setStyleSheet("background-color:lightblue;")
        label3.setStyleSheet("background-color:yellow;")
        label4.setStyleSheet("background-color:green;")

        layout=QGridLayout()

        layout.addWidget(label1,0,0)
        layout.addWidget(label2,0,1)
        layout.addWidget(label3,1,0)
        layout.addWidget(label4,1,1)

        main_widget.setLayout(layout)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.setWindowIcon(QIcon("python/graphics/favicon.png"))

    
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

