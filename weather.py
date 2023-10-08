import geocoder
import requests
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QFont
import sys



#Setup of PyQt6 GUI
app = QApplication(sys.argv)
window = QWidget()
#Overall window configuration
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)

first_day = ''

helloMsg = QLabel(str(first_day), parent = window)
helloMsg.move(20,60)

#Function to update the weather data

def Update_Weather():
    g = geocoder.ip('me')
    response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={g.lat}&lon={g.lng}&units=imperial&exclude=current,hourly,minutely&appid=cab21c27f9c1bbea893d4604a27a6fc3")
    raw_data = response.json()
    first_day = raw_data['daily'][0]
    helloMsg.setText(str(first_day))

Update_Weather() # Done to automatically give weather data

QToolTip.setFont(QFont('SansSerif', 10))
update_button = QPushButton(text='Update Meteorological Data', parent= window)
update_button.clicked.connect(lambda:Update_Weather())
update_button.setToolTip('Please keep in mind that the data is refreshed every 30 minutes.')
update_button.move(25,25)

window.show()
sys.exit(app.exec())