import threading
import time

def walk():
    time.sleep(8)
    print("walking dog")

def get_mail():
    time.sleep(4)
    print("You got the mail")

def take_out_trash():
    time.sleep(2)
    print("trash out")


task1=threading.Thread(target=walk)
task1.start()
task2=threading.Thread(target=get_mail)
task2.start()
task3=threading.Thread(target=take_out_trash)
task3.start()
