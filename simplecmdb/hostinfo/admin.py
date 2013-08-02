from models import Host,HostGroup
from django.contrib import admin

class HostAdmin(admin.ModelAdmin):
    list_display = ['vendor',
        'product',
        'osver',
        'sn',
        'hostname',
        'osbit',
        'osver',
        'cpumodel',
        'cpunum',
        'memory',
        #'ipaddr',
        'identity',
    ]

class IPaddrAdmin(admin.ModelAdmin):
    list_display = ['ipaddr','host']


class HostGroupAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Host, HostAdmin)
#admin.site.register(IPaddr, IPaddrAdmin)
admin.site.register(HostGroup, HostGroupAdmin)
