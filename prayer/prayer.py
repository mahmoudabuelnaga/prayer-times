from datetime import datetime
import requests
import os

now = datetime.now()
month = now.strftime("%m")
year = now.strftime("%Y")

def get_prayer_times(city, country):
    url = f'http://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method=2&month={month}&year={year}'
    r = requests.get(url).json()
    return r    