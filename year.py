import datetime as dt
import time as tm

tm.time()
def fromtimestamp():
    dtnow = dt.datetime.fromtimestamp(tm.time())
    create = dtnow.year, dtnow.month,dtnow.day,dtnow.hour,dtnow.minute,dtnow.second
    print(create)
fromtimestamp()

# now = dt.datetime.now()
# print("Current date and time: ")
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
# print(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))
