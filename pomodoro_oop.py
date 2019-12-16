from datetime import datetime, date, time
from datetime import timedelta
from time import sleep

class Pomodoro:

    # Class attribute to be shared among all methods as it does not change.
    one_second = timedelta(seconds=1)

    # def __init__(self):
    #     pass

    # Standard method that represent timer.
    def timer(self, num_minutes):
        print(f"Starting Timer {num_minutes} Minutes:")
        self.num_minutes = timedelta(minutes=num_minutes)
        count_min = num_minutes * 60
        for i in range(count_min):
            count_min -= 1
            sleep(1)
            new_time = self.num_minutes - self.one_second
            print(new_time)
            self.num_minutes = new_time

    # Calling standard method to start 25 min timer.
    def study_timer(self):
        return Pomodoro.timer(self, 25)

    # Calling standard method to start 5 min timer.
    def break_timer(self):
        return Pomodoro.timer(self, 5)

# Call Pomodoro methods.  
if __name__ == "__main__":
    Pomodoro().study_timer()
    Pomodoro().break_timer()