import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel,QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon
import datetime

class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarm")
        self.setGeometry(700,300,500,200)
        self.setWindowIcon(QIcon("pyqt/favicon.png"))

        self.hour=0
        self.minutes=0
        self.seconds=0

        self.stop_timer=True
        self.reset_timer=False

        self.timer=QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) 
        self.update_time()

    def update_time(self):
        self.initUI()

    def get_time(self):
        if(self.stop_timer==True):
            return f"{str(self.hour).zfill(2)} : {str(self.minutes).zfill(2)} : {str(self.seconds).zfill(2)}"
        
        elif(self.reset_timer==True):
            self.hour=0
            self.minutes=0
            self.seconds=0
            self.reset_timer=False
            return f"{str(self.hour).zfill(2)} : {str(self.minutes).zfill(2)} : {str(self.seconds).zfill(2)}"

        self.hour=self.hour + (self.minutes+1)//60
        self.minutes=(self.minutes + (self.seconds + 1)//60)%60
        self.seconds=(self.seconds + 1)%60
        current_time=f"{str(self.hour).zfill(2)} : {str(self.minutes).zfill(2)} : {str(self.seconds).zfill(2)}"
        return current_time

    def initUI(self):
        current_time=self.get_time()
        mywidget=QWidget()
        self.setCentralWidget(mywidget)

        # creating top and bottom layouts
        top_layout=QVBoxLayout()
        bottom_layout=QHBoxLayout()

        # creating the label for top layout and also styleing it
        top_label=QLabel(current_time,self)
        top_label.setAlignment(Qt.AlignCenter)
        top_label.setStyleSheet("background-color: black; color: green; font-size: 80px; font-family: monospace;")

        # adding that label to top layout
        top_layout.addWidget(top_label)
        
        # creating buttons for bottom layout and styling
        self.start_button=QPushButton("Start",self)
        self.start_button.setStyleSheet("background-color: green; color: White; border: none; padding: 10px; border-radius: 5%; font-size: 20px; font-family: gill-sans; font-weight: bold;")
        self.start_button.clicked.connect(self.click_start)
        self.stop_button=QPushButton("Stop",self)
        self.stop_button.setStyleSheet("background-color: red; color: White; border: none; padding: 10px; border-radius: 5%; font-size: 20px; font-family: gill-sans; font-weight: bold;")
        self.stop_button.clicked.connect(self.click_stop)
        self.reset_button=QPushButton("Reset",self)
        self.reset_button.setStyleSheet("background-color: blue; color: White; border: none; padding: 10px; border-radius: 5%; font-size: 20px; font-family: gill-sans; font-weight: bold;")
        self.reset_button.clicked.connect(self.click_reset)


        # adding those buttons to the bottom layout
        bottom_layout.addWidget(self.start_button)
        bottom_layout.addWidget(self.stop_button)
        bottom_layout.addWidget(self.reset_button)

        # created main layout for adding top and bottom layout
        main_layout=QVBoxLayout()

        #adding layouts to main layout
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        # setting main layout as central widget 
        mywidget.setLayout(main_layout)

    def click_start(self):
        self.stop_timer=False

    def click_stop(self):
        self.stop_timer=True
        
    def click_reset(self):
            self.reset_timer=True

    
def main():
    app=QApplication(sys.argv)
    window=mywindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
