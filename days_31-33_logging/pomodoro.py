from datetime import datetime, date, time
from datetime import timedelta
from time import sleep
import sys 
import logbook
import pytz


def timer_25():
    min_25 = timedelta(minutes=25)
    app_log.info(f"Pomodoro 25 started")
    second_1 = timedelta(hours=0, minutes=0, seconds=1)
    count_25_min = 1500
    for i in range(1500):
        count_25_min -= 1
        sleep(1)
        new_time = min_25 - second_1
        print(new_time)
        min_25 = new_time
    app_log.infor('Pomodoro 25 finished.')
    
def timer_5():
    min_5 = timedelta(minutes=5)
    app_log.info(f"Pomodoro 5 started")
    second_1 = timedelta(hours=0, minutes=0, seconds=1)
    count_5_min = 300
    for i in range(300):
        count_5_min -= 1
        sleep(1)
        new_time = min_5 - second_1
        print(new_time)
        min_5 = new_time
    app_log.infor('Pomodoro 25 finished.')

def pomodoro():
    usr = input("Choose timer 25 or 5: ")
    answer = int(usr)
    try: 
        if answer == 25:
            print(timedelta(minutes=25))
            return timer_25()
        elif answer == 5:
            print(timedelta(minutes=5))
            return timer_5()
        else:
            return ValueError5
    except KeyboardInterrupt:
        print("\nDone!")
        app_log.info("Session interupted by user")
    else:
        app_log.info(f"Pomodoro session finished")
    

def cst_tz():
    return datetime.now(tz=pytz.UTC)

if __name__ == "__main__":
    level = logbook.TRACE
    app_log = logbook.Logger("App")
    logbook.TimedRotatingFileHandler("/Users/Vule/Documents/Python/100_Days_of_Python/days_31-33_logging/pomodoro.log", level=level, ).push_application()

    pomodoro()