from datetime import datetime
import os
import urllib.request
from datetime import timedelta

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    year, month, daytime = line.split()[1].split('-')
    day, time = (daytime.split("T"))
    hour, minute, second = time.split(":")
    return datetime(int(year), int(month), int(day), int(hour), int(minute), int(second)) 


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_lines = []
    for line in loglines:
        if "Shutdown initiated" in line:
            shutdown_lines.append(line)

    first = convert_to_datetime(shutdown_lines[0])
    last = convert_to_datetime(shutdown_lines[-1])

    return (last - first)
    


