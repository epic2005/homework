#!/usr/bin/env python

import datetime

MONTH = {
    'Jan':1,
    'Feb':2,
    'Mar':3,
    'Apr':4,
    'May':5,
    'Jun':6,
    'Jul':7,
    'Aug':8,
    'Sep':9,
    'Oct':10,
    'Dec':11,
    'Nov':12,
}

def convert2datetime(s):
    day, month, time = s.split('/')
    year, hour, minute, second = time.split(':')
    t = datetime.datetime(int(year), MONTH[month], int(day), int(hour), int(minute), int(second))
    return t

def getOneMinLog(f):
    now = datetime.datetime.now()
    onemin = now - datetime.timedelta(minutes=1)
    
    fp = open(f, 'r')
    data = fp.read()
    for line in [i for i in data.split('\n')  if i ]:
        if len(line.split()) != 1:
            log_time = convert2datetime(line.split()[3][1:])
            print log_time
            #print onemin
            #print onemin < log_time
            #print log_time > now

            if onemin < log_time and now > log_time:
                print 'fine'

if __name__ == '__main__':
    getOneMinLog('/etc/httpd/logs/graphite-web-access.log')
