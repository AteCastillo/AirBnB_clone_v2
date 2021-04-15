#!/usr/bin/python3
'''distributes an archive to your web servers,
using the function do_deploy''',

from fabric.api import *
from os import path getcwd
from datetime import datetime

env.hosts = ['34.74.47.238', '35.231.230.80']