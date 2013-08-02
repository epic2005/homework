#!/usr/bin/env python
from subprocess import Popen, PIPE
import platform
import re

def getProcTxt(cmd):
    p = Popen(cmd,stdout=PIPE,shell=True)
    stdout,stderr = p.communicate()
    return stdout

def getProcTopLine(cmd):
	p = Popen(cmd,stdout=PIPE,shell=True)
	out = p.stdout.readline()
	return out

def parseDMI(dmi):
    pd = {}
    for line in dmi.split('\n'):
        if line.startswith('\t'):
            k,v = [i.strip() for i in line.split(':')]
            pd[k] = v
    return pd

def getPlatForm(n):	
	pf = platform.uname()	
	ret = pf[n]
	
	if n == 1:
		pass
	elif n == 4:
		if ret == 'i686':
			ret = '32bit'
		elif ret == 'x86_64':
			ret = '64bit'
		else :
			ret = 'can\'t find server bit.'
	else:
		ret = "error."
	return ret
	
def parserIfconfig(out):
    groups = [i for i in out.split('\n\n') if i and not i.startswith('lo')]
    ipaddr = re.compile(r'.*inet addr:([\d.]{7,15})?')

    ret = []
    n = 0
    ipstr = ""

    for group in groups:
        for line in group.split('\n'):
            m_ipaddr = ipaddr.match(line)
            if m_ipaddr:
                ret.append(m_ipaddr.groups()[0].strip())

    #for ip in ret:
    #    n += 1
    #    if n != len(ret):
    #        ip = "%s;" % ip
    #    ipstr.append(ip)
    #ipstr = "".join(ipstr)

    #ipstr = ";".join([str(ip) for ip in ret])
    ipstr = ret[0]

    return ipstr

def parserCPU(proc):

    cpu_name = ""
    cpu_phys = []

    s = [i for i in proc.split("\n\n") if i]

    for item in s:
        for line in item.split('\n'):
            k, v = line.split(':')
            if k.strip() == 'physical id' :
                cpu_phys.append(v)
            if k.strip() == 'model name':
                cpu_name = v.strip()

    return (len(s),len(list(set(cpu_phys))),cpu_name)
