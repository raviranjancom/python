import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel,QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon
import requests

class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Open weather")
        self.setGeometry(600,300,500,500)
        self.setWindowIcon(QIcon("pyqt/logo.png"))
        self.initUI()

    def initUI(self):
        main_widget=QWidget()
        self.setCentralWidget(main_widget)
        mylayout=QVBoxLayout()
        self.textbox=QLineEdit()
        self.textbox.setPlaceholderText("Enter your City....")
        city_name=self.textbox.text()
        self.button=QPushButton("Get Weather", self)
        self.button.clicked.connect(self.fun)
        
        self.tempeture_label=QLabel("",self)
        self.tempeture_label.setAlignment(Qt.AlignCenter)
        self.image_label=QLabel("",self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("font-size: 100px;")
        self.details_label=QLabel("",self)
        self.details_label.setAlignment(Qt.AlignCenter)
        mylayout.addWidget(self.textbox)
        mylayout.addWidget(self.button)
        mylayout.addWidget(self.tempeture_label)
        mylayout.addWidget(self.image_label)
        mylayout.addWidget(self.details_label)
        self.setStyleSheet("*{font-family: gills-sans; font-size: 25px; background-color: black; color: white; font-weight: bold;} QLineEdit{background-color: #D33939; border: none; border-radius: 5%; padding: 5px; color: white;} QPushButton{background-color: #D33939;padding: 5px; color: white; font-weight: bold;} QLabel{background-color: #17C9A6;}")

        main_widget.setLayout(mylayout)

    def fun(self):
        city=self.textbox.text()
        self.getweather(city)
        self.textbox.setText("")


    def getweather(self,city):
        hashmap = {
            'Sunny': "☀️",
            'Cold': "🌨️",
            'Thunderstorm': "⛈️",
            'Clear': "☁️",
            'Rain': "🌧️",
            'Others': "⛅"
        }
        api="3d10621fccf5118c7c77aa35f7785b47"
        url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric"
        response=requests.get(url)

        if(response.status_code==200):
            self.tempeture_label.setText(f"{str(response.json()['main']['temp'])}°C")
            self.details_label.setText(str(response.json()['weather'][0]['main']))
            idx=response.json()['weather'][0]['main']
            self.image_label.setText(hashmap[idx])

        else:
            self.tempeture_label.setText("City not found")


def main():
    app=QApplication(sys.argv)
    window=mywindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

