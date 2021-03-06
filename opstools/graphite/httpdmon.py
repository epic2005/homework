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

    ret = []
    for line in [i for i in data.split('\n')  if i ]:
        if len(line.split()) != 1:
            log_time = convert2datetime(line.split()[3][1:])

            if onemin < log_time and now > log_time:
                ret.append(log_time)

    return len(ret),log_time

if __name__ == '__main__':
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1',2003))

    #getOneMinLog('/etc/httpd/logs/graphite-web-access.log')
    n, h = getOneMinLog('/etc/httpd/logs/access_log')
    s = 'csvt.http_200 %d %s\n' % (n, h.strftime('%s'))
    sock.send(s)

