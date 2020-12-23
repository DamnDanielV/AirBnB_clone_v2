#!/usr/bin/python3
"""generarates a tgz archive in the servers"""
from fabric.api import *
from datetime import datetime

env.use_ssh_config = True
env.user = 'ubuntu'
env.hosts = ['34.74.16.58', '35.196.98.184']
env.key_filename = '~/.ssh/holberton'


def do_pack():
    """
        generates a .tgz archive from the contents
        of the web_static folder of your AirBnB Clone repo
    """
    local("mkdir -p ./versions")
    local("tar czvf ./versions/web_static_{}.tgz ./web_static/*"
          .format(datetime.now().strftime("%Y%m%d%I%M%S")))
