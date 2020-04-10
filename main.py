from datetime import datetime
import time
from tkinter import *


def getTime():
    currentDate = datetime.now()

    return currentDate


def formatHour():
    currentDate = getTime()
    currentHour = str(currentDate.hour).zfill(2)

    return currentHour


def formatMinute():
    currentDate = getTime()
    currentMinute = str(currentDate.minute).zfill(2)

    return currentMinute


def renderImage():
    currentHour = formatHour()
    currentMinute = formatMinute()

    hourFirstColumn = int(currentHour[0])
    hourSecondColumn = int(currentHour[1])
    minuteFirstColumn = int(currentMinute[0])
    minuteSecondColumn = int(currentMinute[1])

    print(hourFirstColumn, hourSecondColumn, minuteFirstColumn, minuteSecondColumn)


def getHourColumns():
    currentHour = formatHour()


def getMinuteColumns():
    currentMinute = formatMinute()


flag = True
window = Tk()
img = PhotoImage(file='simpsons.jpg')

imgLbl = Label(window, image=img)
while flag:
    renderImage()
    time.sleep(5)
