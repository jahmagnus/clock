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


def runInterface():

    window = Tk()
    img = PhotoImage(file='number1.png')
    imgLbl = Label(window, image=img)
    imgLbl.grid()
    window.mainloop()

flag = True
while flag:
    renderImage()
    time.sleep(5)


# interface opens and stays open for the duration, the interface needs to read the output from render image
# and update with the relevent information. ie, when the minutes change so should the number in the
# interface should change too