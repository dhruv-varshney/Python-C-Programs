import datetime as dt
import time as tm
tm.time()
c = dt.datetime.now()
print(c)
dtnow = dt.datetime.fromtimestamp(tm.time())
d = dtnow.year,dtnow.month,dtnow.day,dtnow.hour,dtnow.minute,dtnow.second,dtnow.microsecond
print(d)
