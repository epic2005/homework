#!/usr/bin/env python
from fabric.api import *
import os

env.username = 'root'
env.password = ''

myhosts =  ['10.1.0.104',]

CODE_REPO_PATH = '/var/www/html/deploy'
CODE_PACKAGE = os.path.join(CODE_REPO_PATH,'package')

def get_last_ver():
    with cd(CODE_REPO_PATH):
        lastver  = run('cat lastvar')
    return lastver

def get_live_ver():
    lastver = get_last_ver()
    with lcd(CODE_REPO_PATH):
        if not os.path.isfile('livever'):
            local('echo %s > livever' % lastver)
            livever = lastver
        else:
            livever = run('cat livever')
    return livever

@hosts(myhosts)
def deploy():
    lastver = get_last_ver()
    livever = get_live_ver()

    print lastver, livever
    if lastver != livever:
        local('echo %s > livever' % lastver)
    
    with lcd(CODE_PACKAGE):
        get(os.path.join(CODE_PACKAGE, 'wordpress-%s.tar' % lastver),'wordpress-%s.tar' % lastver)
        local_md5 = local('md5sum wordpress-%s.tar' % lastver)
        get(os.path.join(CODE_PACKAGE, 'wordpress-%s.tar.md5' % lastver),'wordpress-%s.tar.md5' % lastver)
        remote_md5 = local('cat wordpress-%s.tar.md5' % lastver)
        if local_md5 == remote_md5 :
            local('tar -zxvf wordpress-%s.tar' % lastver)
        else:
            print 'file distribute error.'
        
        f = os.path.join(CODE_PACKAGE, 'wordpress-%s' % lastver)
        local('ln -s %s /var/www/html/htdocs ' %  f)

