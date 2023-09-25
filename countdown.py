import time as t
import datetime as dt

def countdown_timer(time):
    time = int(time)
    target = dt.datetime.now() + dt.timedelta(minutes=time)

    while dt.datetime.now() < target:
        remaining = target - dt.datetime.now()
        print(f'{remaining} remaining.')
        t.sleep(1.0)
    
    print('Countdown completed, taking off.')

measurements = ['days', 'day', 'hours', 'hour', 'minutes', 'minute', 'seconds', 'second']


converted_countdown = 0
time_class = input('Days, Minutes, Hours, or Seconds?: ').lower
countdown = input('How long, in the previous measurement?: ')
if time_class == 'days':
    converted_countdown = int(countdown) * 1440
    # countdown_timer(converted_countdown)
elif time_class == 'hours':
    converted_countdown = int(countdown) * 60
    # countdown_timer(converted_countdown)
elif time_class == 'minutes':
    converted_countdown = int(countdown)
    print(countdown_timer(converted_countdown))
else:
    converted_countdown = int(countdown) / 60
    # countdown_timer(converted_countdown)




