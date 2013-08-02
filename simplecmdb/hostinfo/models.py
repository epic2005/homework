from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Host(models.Model):
    """store host information"""
    vendor = models.CharField(max_length=30)
    product = models.CharField(max_length=30)
    sn = models.CharField(max_length=30)
    hostname = models.CharField(max_length=30)
    osbit = models.CharField(max_length=15)
    osver = models.CharField(max_length=30)
    cpumodel = models.CharField(max_length=30)
    cpucores = models.IntegerField(max_length=2)
    cpunum = models.IntegerField(max_length=2)
    memory = models.CharField(max_length=30)
    ipaddr = models.IPAddressField(max_length=15)
    identity = models.CharField(max_length=32)

    def __unicode__(self):
        return "%s,%s" % (self.ipaddr,self.hostname)

#class IPaddr(models.Model):
#    ipaddr = models.IPAddressField()
#    host = models.ForeignKey('Host')


class HostGroup(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(Host)

    def __unicode__(self):
        return self.name

@receiver(pre_save,sender=Host)
def mod_handler(sender,**kwargs):
    ret = str(kwargs['instance'])
    ipaddr, hostname = ret.split(',')
    doconnect(ipaddr,'xxx','xxxxxx', hostname)

def doconnect(ip, userid, passwd, host):
    import paramiko
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=userid, password=passwd)
    paramiko.util.log_to_file('connect.log')
    stdin, stdout, stderr = client.exec_command('echo %s %s >> /etc/hosts' % (ip, host))
    print 'done.'
