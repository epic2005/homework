#!/usr/bin/env python

from fabric.api import *
import os

env.username = 'root'
env.password = 'aaasss'

myhosts =  ['172.23.201.11',]

wwwroot = '/var/www/html/deploy'
package = os.path.join(wwwroot,'package')

@hosts(myhosts)
def deploy():
    with cd(wwwroot):
        lastver  = run('cat lastwar')
        print 'lastver: %s' % lastver
    
    with lcd(wwwroot):
        if not os.path.isfile('livever'):
            local('echo %s > livever' % lastver)
            livever = ""
        else:
            livever = run('cat livever')
        
        print lastver, livever
        if lastver != livever:
            local('echo %s > livever' % lastver)
            with lcd(package):
                get(os.path.join(package,'wordpress-%s.tar' % lastver),'wordpress-%s.tar' % lastver)
                get(os.path.join(package,'wordpress-%s.tar.md5' % lastver),'wordpress-%s.tar.md5' % lastver)
        
