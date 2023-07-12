import time
import datetime
import winsound

# 1. Timer
# 2. Alarm
# World Clock

print("Select a use for the clock app: ")
print("1. Timer")
print("2. Alarm")
print("3. World Clock")

operation = input()

if operation == "1":
    timer = int(input("How many seconds do you want the timer to be?: "))
    for x in range(timer,0,-1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("TIMES UP")


if operation == "2":
    alarmHour = int(input("Enter Hour: "))
    alarmMin = int(input("Enter Minutes: "))
    alarmAm = input("am . pm: ")

    if alarmAm == "pm":
        alarmHour += 12

    while True:
        if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
            print("TIMES UP!")
            winsound.MessageBeep(-1)
            break

if operation == "3":
    print("IN PROGRESS")


