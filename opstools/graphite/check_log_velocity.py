#!/usr/bin/env python

import datetime
import sys

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


def tailFile(f,lines):
    from subprocess import Popen, PIPE
    cmd = "tail -n %s %s" % (lines, f)
    p = Popen(cmd , stdout=PIPE, shell=True)
    stdout,stderr = p.communicate()
    return stdout

def convert2datetime(s):
    now  = datetime.datetime.now()
    month, day, time = s.split()
    hour, minute, second = time.split(':')
    t = datetime.datetime(now.year, MONTH[month], int(day), int(hour), int(minute), int(second))
    return t

def parseLog(data):
    now  = datetime.datetime.now()
    fiveminago = now - datetime.timedelta(minutes=5)

    ret = {}
    for line in [i for i in data.split('\n') if i ]:
        log_time = convert2datetime(' '.join(line.split()[0:3]))
        if fiveminago < log_time:
            if log_time in ret:
                ret[log_time] += 1
            else:
                ret[log_time] = 1
    return ret


def main():
    log_data = parseLog(tailFile('/var/log/messages',100))
    import operator

    sorted_data = sorted(log_data.iteritems(),key=operator.itemgetter(1),reverse=True)

    for t,n in sorted_data:
        if n > 1:
             #sys.exit()
            print t,n

if __name__ == '__main__':
    main()
