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

#render image and gethourcolumn are functions to be worked on---i think i can move some of the work from render
#image into the hour colums. this will assist in mapping an hour or minute value to an image that represents
#that value ex. current hour = 12 current minute = 45

def getHourFirstColumn():
    currentHour = formatHour()
    hourFirstColumn = int(currentHour[0])
    return hourFirstColumn

def getHourSecondColumn():
    currentHour = formatHour()
    hourSecondColumn = int(currentHour[1])
    return hourSecondColumn

def getMinuteFirstColumn():
    currentMinute = formatMinute()
    minuteFirstColumn = int(currentMinute[0])
    return minuteFirstColumn

def getMinuteSecondColumn():
    currentMinute = formatMinute()
    minuteSecondColumn = int(currentMinute[1])
    return minuteSecondColumn

##function will take input from helper methods and return an image based on the current value of the hour
##and minute.
def renderImage(timeInput):
    if timeInput == 0:
        return Image.open('number1.png')
##THIS IS WERE I STOPPED 10.4.20. continue to write function that will return an image to be used in the interface
##based on the value of the timeinput. the returning of an image i think needs the module called 'pillow'
##which I have not yet added to my python library.


def runInterface():

    window = Tk()
    img = PhotoImage(file='number1.png')

    firstHourColumn = Label(window, image=img)
    firstHourColumn.grid(row=1, column=1)

    secondHourColumn = Label(window, image=img)
    secondHourColumn.grid(row=1, column=2)

    firstMinuteColumn = Label(window, image=img)
    firstMinuteColumn.grid(row=1, column=3)

    secondMinuteColumn = Label(window, image=img)
    secondMinuteColumn.grid(row=1, column=4)
    window.mainloop()



runInterface()


# interface opens and stays open for the duration, the interface needs to read the output from render image
# and update with the relevent information. ie, when the minutes change so should the number in the
# interface should change too