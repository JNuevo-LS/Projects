import geocoder
import requests
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QToolTip, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QFont
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
window.setGeometry(100, 100, 400, 600)

first_day = ''

#Function to update the weather data

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
update_button.move(230, 550)



today = dt.datetime.fromtimestamp(week_data.timestamps[0])
today_date = QLabel(text = '', parent = window )
# today_date.setFont(QFont('SansSerif', 7))
today_date.move(50, 50)

Day1_Data = QLabel(text='The temperature today will be ' + str(week_data.day_temps[0]) + ' degrees Fahrenheit', parent = window, wordWrap = True)
Day1_Data.setFont(QFont('SansSerif', 7))
Day1_Data.resize(100,200)
Day1_Data.move(10, 40)


window.show()
sys.exit(app.exec())

