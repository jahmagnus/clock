import requests
import json
import webbrowser
import pprint
import time

run = True
while run:
    r = requests.get('http://worldtimeapi.org/api/timezone/Europe/London')

    dateTime = (r.json()['datetime'])
    time.sleep(5)

    print(dateTime)







