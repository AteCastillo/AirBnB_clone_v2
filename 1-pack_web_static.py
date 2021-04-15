#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
using the function do_pack'''

from fabric.api import *
from os.path import isdir
import datetime


def do_pack():
    if not isdir('versions'):
        run('mkdir /versions')
    today = datetime.date.today()
    new_date = today.strftime("%Y%m%d%H%M%S")
    local('tar zcvf web_static_{}.tgz web_static'.format(new_date))
