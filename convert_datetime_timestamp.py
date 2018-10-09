import datetime
import time
from datetime import timedelta

"""
Plus 2 hours into specify time
"""

# method1
def cal_date(strs):
    date = datetime.datetime.strptime(strs, "%Y-%m-%d %H:%M:%S")
    unixtime = time.mktime(date.timetuple())
    # Plus 2 hours
    unixtime += 2*3600
    date = datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
    return date

# method2
def cal_date(strs):
    # ex. strs = "2018-10-01 00:00:00"
    date = datetime.datetime.strptime(strs, '%Y-%m-%d %H:%M:%S')
    return date+timedelta(hours=2)
    
