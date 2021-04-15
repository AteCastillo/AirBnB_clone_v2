#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
using the function do_pack'''

from fabric.api import *
from os.path import isdir
from datetime import datetime


def do_pack():
        '''convert the content of a dir to a tar file'''
        if not isdir('versions'):
                if local("mkdir versions").failed:
                        return None
        now = datetime.now()
        formated = now.strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(formated)
        if local("tar -cvzf {} web_static".format(path)).failed:
                return None
        return path
