#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.getsysteminfo import *

class IDCServer(object):
	
	def __init__(self, vendor='*',product='*',sn='-',hostname="*",osbit="*",ips="1.1.1.1",cpus="*",mem="",osver="",uuid=""):
		self.vendor = vendor
		self.product = product
		self.sn = sn
		self.hostname = hostname
		self.osbit = osbit
		self.ips = ips
		self.cpus = cpus
		self.mem = mem
		self.osver = osver
		self.uuid = uuid

	def getDMI(self):
		dmi = parseDMI(getProcTxt("dmidecode -t 1"))
		return dmi
	
	def getIps(self):
		ips = parserIfconfig(getProcTxt("ifconfig"))
		return ips
	
	def getCPU(self):
		cpu = parserCPU(getProcTxt("cat /proc/cpuinfo"))
		return cpu
	
	def getMemory(self):
		out = getProcTopLine("cat /proc/meminfo")
		mem = out.split(":")
		return mem[1].strip()
	
	def getOsver(self):
		out = getProcTopLine("cat /etc/issue")
		return out.strip()

	def idc_vendor(self):
		dmi = self.getDMI()
		self.vendor = dmi['Manufacturer']
		return self.vendor
	
	def idc_product(self):
		dmi = self.getDMI()
		self.product = dmi['Product Name']
		return self.product
	
	def idc_sn(self):
		dmi = self.getDMI()
		self.sn = dmi['Serial Number']
		return self.sn
	
        def idc_uuid(self):
		dmi = self.getDMI()
		self.uuid = dmi['UUID']
		return self.uuid
		
	def idc_hostname(self):
		self.hostname = getPlatForm(1)
		return self.hostname

	def idc_osbit(self):
		self.osbit = getPlatForm(4)
		return self.osbit

	def idc_ips(self):
		self.ips = self.getIps()
		return self.ips
	
	def idc_cpu(self):
		self.cpus = self.getCPU()
		return self.cpus
		
	def idc_memory(self):
		self.mem = self.getMemory()
		return self.mem
	
	def idc_osver(self):
		self.osver = self.getOsver()
		return self.osver
