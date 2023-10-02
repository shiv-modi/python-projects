from datetime import datetime
from playsound import playsound

alarm_time = input('Enter the time in HH:MM:SS: \n')
alarm_hours = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print('Alarm is set.....')

while True:

    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
    
    if(alarm_period == current_period):

        if(alarm_hours == current_hour):

            if(alarm_min == current_minute):

                if(alarm_sec == current_second):
                    
                    print("wake up")
                    playsound('alarm.mp3')
                    break;
                    