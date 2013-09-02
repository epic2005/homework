#!/usr/bin/env python

import datetime

now = datetime.datetime.now()
#year,month,timed = str(now).split("-")
#day,cat = timed.split(" ")
#dt, tmp = str(now).split()

ymd = datetime.datetime.strftime(now, '%Y-%m-%d')
timed = datetime.datetime.strptime(ymd, '%Y-%m-%d')
onemin = datetime.timedelta(minutes=1)

for i in range(1440):
    timed = timed + onemin
    print timed
    timec = timed - onemin 
    print timec
