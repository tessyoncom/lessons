# This is the solution to the assignment from simeon
from datetime import date

# this is func1 - function to return date
def func1():
    today_date = date.today()
    return today_date
print("Today's date is: ", func1())

# this is func2 - function to return time
import time
def func2():
    time_now = time.localtime(time.time())
    time_now = time.strftime("%I:%M",time_now)
    return time_now
print("The time now is: ", func2())

# this is func3 - function to return version of python
import sys
def func3():
    python_version = sys.version_info[0]
    return python_version
print ("The python version you are using is: ", func3())


