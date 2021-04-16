#!/usr/bin/python3
'''distributes an archive to your web servers,
using the function do_deploy''',

from fabric.contrib import files
from fabric.api import *
from os import path

env.hosts = ['34.74.47.238', '35.231.230.80']


def do_deploy(archive_path):
    """distributes an archive to your web servers, using the function do_deploy"""
    if not path.exists(archive_path):
        return False

    file = archive_path.split('/')
    file_withextension = file[1]
    file0 = file_withextension.split('.')
    file_noextension = file0[0]
    new_tmpfile = "/tmp/{}".format(file_withextension)
    destination = "/data/web_static/releases"
    # print('mv {}/{}/web_static/* {}/{}'.format(destination, file_noextension, destination, file_noextension))
    try:
        put(archive_path, new_tmpfile)
        run('mkdir -p {}/{}'.format(destination, file_noextension))
        run('tar -xzf {} -C {}/{}'.format(new_tmpfile, destination, file_noextension))
        run('rm -f {}'.format(new_tmpfile))
        run('mv {}/{}/web_static/* {}/{}'.format(destination, file_noextension, destination, file_noextension))
        run('rm -rf {}/{}/web_static'.format(destination, file_noextension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/{} /data/web_static/current'.format(destination, file_noextension))
        return True
    except:
        return False
