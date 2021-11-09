from playsound import playsound
from datetime import datetime
import time




def load_alarm_music(alarm_voice):  
    playsound(alarm_voice)  
def alarm( alarm_message, alarm_music):
    print(alarm_message)
    return load_alarm_music(alarm_music)

    
def calculate_wait_time(alarm_time):    
    alarm_times=alarm_time.split(":")
    alarm_hour=int(alarm_times[0])
    alarm_minutes=int(alarm_times[1])
    now_hour=int(datetime.now().hour)
    now_minutes=int(datetime.now().minute)
    dif_hour=abs(alarm_hour-now_hour)
    dif_minutes=abs(alarm_minutes-now_minutes)
    if alarm_hour< now_hour:
       due_hour=24-dif_hour
    else:
        due_hour=dif_hour   
    if alarm_minutes< now_minutes:
        due_minutes=60-dif_minutes
    else:
        due_minutes=dif_minutes    
        
    return (due_hour*60*60)+(due_minutes*60)   


def set_alarm(alarm_time, alarm_voice, alarm_message):
    delay_sum=calculate_wait_time(alarm_time)
    time.sleep(delay_sum)
    alarm(alarm_message,alarm_voice)
    
    
    

set_alarm("20:50","path_to_file/AURORA - Cure For Me.mp3","Kak le")        

