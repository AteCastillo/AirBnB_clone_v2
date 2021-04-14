#!/usr/bin/python3
'''Fabric Module'''
from fabric.api import local
import datetime
from os import path


def do_pack():
    '''Create a tarball file of web static'''
    fecha = datetime.datetime.now().isoformat()
    fecha = fecha[:-7].replace(":", "").replace(".",
                                                "").replace("T", "").replace("-", "")
    filename = "versions/web_static_" + fecha + ".tgz"
    if not path.exists('versions'):
        try:
            local("mkdir -p versions")
        except:
            return None
    try:
        local("tar -czvf {} web_static".format(filename))
    except:
        return None
    return filename
