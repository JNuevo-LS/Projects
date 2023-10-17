import geocoder
import requests
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QFont, QPalette
import sys
import datetime as dt
import math

#Class set up to make extracting data from the OpenWeatherMap API's data easier.
class weather_date:
    def __init__(self, weather_data):

        self.list_of_attributes = ['weather_description', 'summaries', 'day_temp', 'min_temp', 'max_temp', 'humidity', 
                              'day_temperature_feels_like', 'night_temperature_feels_like', 'wind_speed', 'uv_index']
        self.day_temp = []
        self.min_temp = []
        self.max_temp = []
        self.summaries = []
        self.humidity = []
        self.day_temperature_feels_like = []
        self.night_temperature_feels_like = []
        self.weather = []
        self.weather_description = []
        self.wind_speed = []
        self.rain_volume = []
        self.uv_index = []
        self.timestamps = []
        for n in range(7):
            weather_list = weather_data['daily'][n]
            self.timestamps.append(weather_list['dt'])
            self.summaries.append(weather_list['summary'])
            self.day_temp.append(weather_list['temp']['day'])
            self.min_temp.append(weather_list['temp']['min'])
            self.max_temp.append(weather_list['temp']['max'])
            self.day_temperature_feels_like.append(weather_list['feels_like']['day'])
            self.night_temperature_feels_like.append(weather_list['feels_like']['night'])
            self.humidity.append(weather_list['humidity'])
            self.weather.append(weather_list['weather'][0]['main'])
            self.weather_description.append(weather_list['weather'][0]['description'])
            self.wind_speed.append(weather_list['wind_speed'])
            self.uv_index.append(weather_list['uvi'])

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

def Set_Weather_F():
    g = geocoder.ip('me')
    response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={g.lat}&lon={g.lng}&units=imperial&exclude=current,hourly,minutely&appid=PRIVATE")
    raw_data = response.json()
    return raw_data

def Set_Weather_C():
    g = geocoder.ip('me')
    response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={g.lat}&lon={g.lng}&units=metric&exclude=current,hourly,minutely&appid=PRIVATE")
    raw_data = response.json()
    return raw_data

raw_data = Set_Weather_F() # Done to automatically give weather data

week_data = weather_date(raw_data)

QToolTip.setFont(QFont('SansSerif', 10))

def create_label(day_of_week): #Using given readable date, creates a title for each forecast.
    date_label = QLabel(text = f'Forecast for {day_of_week[1]} {day_of_week[0][2]}, {day_of_week[0][0]}', parent = window)
    date_label.setFont(QFont('SansSerif', 8))
    return date_label

def perfectly_sized(label_name): #Function to resize labels to a standard, usually fine size.
    return label_name.resize(120,40), label_name.setFont(QFont('SansSerif', 7)), label_name.setStyleSheet('border: 1px solid lightblue;')

week_date_list = []
for n in range(7):
    week_date_list.append(week_data.timestamps[n])

readable_date_list = []
for n in range(7):
    readable_date_list.append(readable_date(week_date_list[n]))

for index, date in enumerate(readable_date_list): #Employs previous function to create weeks forecast with minimal code
    date = create_label(readable_date_list[index])
    date.move(15+(index*160), 50)

label_list = []

def of_or_not(index):
    if 5 < index < 8:
        of = ''
    else:
        of = 'of'
    return of

for attribute in week_data.list_of_attributes: #The heart of this app
    attribute_index = week_data.list_of_attributes.index(attribute)
    list_of_the_attribute = getattr(week_data, attribute)
    for n, attr_val in enumerate(list_of_the_attribute):
        if attribute_index <= 1:
            attribute_label = QLabel(f'{attr_val.capitalize()}', parent = window, wordWrap = True) #For the two descriptive label
            perfectly_sized(attribute_label)
            if attribute_index == 1:
                attribute_label.resize(120, 50) #Resizes description as it is often a long string.
        else:   
            of = of_or_not(attribute_index)
            stripped_attr = str(attribute).replace('_', ' ') #Remove unneeded underscores
            attribute_label = QLabel(f"{stripped_attr.capitalize()} {of} {attr_val}", parent = window, wordWrap = True)
            perfectly_sized(attribute_label)
        attribute_label.move(20+(n*160), 70+(attribute_index*45)) #Made to perfectly place all labels neatly and evenly spaced
        label_list.append(attribute_label)

def Label_Updates_Automated(update): #Updates every single already made label to the newest up to date information.
    week_data_updated = weather_date(update)
    count = 1
    rows = [0,1,2,3,4,5,6,7,8,9]
    for n in range(0, 70):
        iteration = math.ceil(count / 7)
        if iteration == 0:
            iteration = 1
        column = n % 7
        row = rows.index(iteration-1)
        specific_attribute = week_data_updated.list_of_attributes[row]
        list_of_the_attribute = getattr(week_data_updated, specific_attribute)
        if iteration <= 2:
            text = str(list_of_the_attribute[column]).capitalize()
        else:
            of = of_or_not(iteration-1)
            stripped_specific_attribute = str(specific_attribute).replace('_', ' ')
            text = f'{stripped_specific_attribute.capitalize()} {of} {list_of_the_attribute[column]}'
        label_list[n].setText(text)
        count += 1

def Update_Weather_C():
    weather_updated_C = Set_Weather_C()
    return  Label_Updates_Automated(weather_updated_C)

def Update_Weather_F():
    weather_updated_F = Set_Weather_F()
    return Label_Updates_Automated(weather_updated_F)


update_button_F = QPushButton(text='Update Meteorological Data in Imperial System', parent= window)
update_button_F.clicked.connect(lambda:Update_Weather_F()) #Need to create function
update_button_F.setToolTip('Please keep in mind that the data is only refreshed every 30 minutes.')
update_button_F.move(650, 550)

update_button_C = QPushButton(text='Update Meteorological Data in Metric System', parent= window)
update_button_C.clicked.connect(lambda:Update_Weather_C()) #Need to create function
update_button_C.setToolTip('Please keep in mind that the data is only refreshed every 30 minutes.')
update_button_C.move(325, 550)


app.setStyle('Fusion')

window.show()
sys.exit(app.exec())

