from datetime import datetime, date, time
from datetime import timedelta
from time import sleep


def timer_25():
    min_25 = timedelta(minutes=25)
    second_1 = timedelta(hours=0, minutes=0, seconds=1)
    count_25_min = 1500
    for i in range(1500):
        count_25_min -= 1
        sleep(1)
        new_time = min_25 - second_1
        print(new_time)
        min_25 = new_time
    
def timer_5():
    min_5 = timedelta(minutes=5)
    second_1 = timedelta(hours=0, minutes=0, seconds=1)
    count_5_min = 300
    for i in range(300):
        count_5_min -= 1
        sleep(1)
        new_time = min_5 - second_1
        print(new_time)
        min_5 = new_time

def pomodoro():
    usr = input("Choose timer 25 or 5: ")
    answer = int(usr)
    if answer == 25:
        print(timedelta(minutes=25))
        return timer_25()
    elif answer == 5:
        print(timedelta(minutes=5))
        return timer_5()
    else:
        return ValueError5


if __name__ == "__main__":
    pomodoro()
