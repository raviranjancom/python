import datetime

target=datetime.time(2025,8,30 1,10,30)
now=datetime.datetime.now()
now=now.strftime("%H:%M:%S")

while(True):
    if(now==target):
        print("Alarm")
        break;
    else:
        print(f"{now}....")
        now=datetime.datetime.now()


