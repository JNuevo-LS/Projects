import geocoder
import requests
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QFont, QPalette
import sys
import datetime as dt
#Class set up to make extracting data from the OpenWeatherMap API's data easier.
class weather_date:
    def __init__(self, weather_data):
        self.day_temps = []
        self.min_temps = []
        self.max_temps = []
        self.summaries = []
        self.humidity = []
        self.feels_like_day = []
        self.feels_like_night = []
        self.weather = []
        self.weather_description = []
        self.wind_speed = []
        self.rain_volume = []
        self.uvindex = []
        self.timestamps = []
        for n in range(7):
            weather_list = weather_data['daily'][n]
            self.timestamps.append(weather_list['dt'])
            self.summaries.append(weather_list['summary'])
            self.day_temps.append(weather_list['temp']['day'])
            self.min_temps.append(weather_list['temp']['min'])
            self.max_temps.append(weather_list['temp']['max'])
            self.feels_like_day.append(weather_list['feels_like']['day'])
            self.feels_like_night.append(weather_list['feels_like']['night'])
            self.humidity.append(weather_list['humidity'])
            self.weather.append(weather_list['weather'][0]['main'])
            self.weather_description.append(weather_list['weather'][0]['description'])
            self.wind_speed.append(weather_list['wind_speed'])
            self.uvindex.append(weather_list['uvi'])

#Setup of PyQt6 GUI
app = QApplication(sys.argv)
window = QWidget()
#Overall window configuration
window.setWindowTitle("PyQt App")
window.setFixedSize(1140, 600)
window.setWindowTitle('Weather App')

first_day = ''

#Function to update the weather data

def pseudo_calendar(value):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    value = int(value)
    if value <= 12:
        value_as_month = months[value-1]
    else: print('Month value invalid')
    return value_as_month

def readable_date(date_given):
    date = dt.datetime.fromtimestamp(date_given)
    date = (str(date).split())[0].split('-')
    month = pseudo_calendar(date[1])
    return [date, month]

def Update_Weather():
    g = geocoder.ip('me')
    response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={g.lat}&lon={g.lng}&units=imperial&exclude=current,hourly,minutely&appid=cab21c27f9c1bbea893d4604a27a6fc3")
    raw_data = response.json()
    return raw_data


raw_data = Update_Weather() # Done to automatically give weather data

week_data = weather_date(raw_data)

QToolTip.setFont(QFont('SansSerif', 10))
update_button = QPushButton(text='Update Meteorological Data', parent= window)
update_button.clicked.connect(lambda:Update_Weather())
update_button.setToolTip('Please keep in mind that the data is refreshed every 30 minutes.')
update_button.move(390, 550)

week_date_list = []
for n in range(7): #Iterates through every day of the week, and gathers their timestamp.
    week_date_list.append(week_data.timestamps[n]) 

readable_date_list = []
for n in range(7): #Iterates through list of timestamps and turns them into a readable date.
    readable_date_list.append(readable_date(week_date_list[n]))


def create_label(day_of_week):
    date_label = QLabel(text = f'Forecast for {day_of_week[1]} {day_of_week[0][2]}, {day_of_week[0][0]}', parent = window)
    date_label.setFont(QFont('SansSerif', 8))
    return date_label


today_date = create_label(readable_date_list[0])
today_date.move(15, 50)

day2_date = create_label(readable_date_list[1])
day2_date.move(175,50)
day3_date = create_label(readable_date_list[2])
day3_date.move(335, 50)
day4_date = create_label(readable_date_list[3])
day4_date.move(495, 50)
day5_date = create_label(readable_date_list[4])
day5_date.move(655, 50)
day6_date = create_label(readable_date_list[5])
day6_date.move(815, 50)
day7_date = create_label(readable_date_list[6])
day7_date.move(975, 50)


today_Data = QLabel(text='The temperature today will be ' + str(week_data.day_temps[0]) + ' degrees Fahrenheit', parent = window, wordWrap = True)
today_Data.setFont(QFont('SansSerif', 7))
today_Data.resize(120,30)
today_Data.move(20, 70)

app.setStyle('Fusion')

window.show()
sys.exit(app.exec())

