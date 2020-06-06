import subprocess
import datetime
import os

# Alarm Timer
alarmH = int(input('What Hour Do You Want The Alarm To Ring? :'))
alarmM = int(input('What Minute Do You Want The Alarm To Ring? :'))
ampm = input('Am Or Pm')
print('Wating For Alarm At', alarmH, alarmM, ampm)
if ampm == 'pm':
    alarmH = alarmH + 12
while 1 == 1:
    if (alarmH==datetime.datetime.now().hour and alarmM==datetime.datetime.now().minute):
        print('Beep Beep Beep....')
        subprocess.call(['afplay', os.path.expanduser('~/Desktop/Chatbot5/Over_the_horizon.mp3')])
