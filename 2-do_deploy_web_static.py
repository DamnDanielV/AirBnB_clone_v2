#!/usr/bin/python3
"""generarates a tgz archive in the servers"""
from fabric.api import *
from datetime import datetime
from os.path import isfile

env.hosts = ['34.74.16.58', '34.75.114.192']


def do_pack():
    """
        generates a .tgz archive from the contents
        of the web_static folder of your AirBnB Clone repo
    """
    local("mkdir -p ./versions")
    local("tar czvf ./versions/web_static_{}.tgz ./web_static/*"
          .format(datetime.now().strftime("%Y%m%d%I%M%S")))


def do_deploy(archive_path):
    """
        distributes an archive to your web servers
    """
    if (isfile(archive_path) is False):
        return False
    ff = archive_path.split('/')[-1]
    try:
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}/".format(ff[:-4]))
        with cd('/tmp/'):
            run('sudo tar xzf {} -C /data/web_static/releases/{}/'.format(ff,
                ff[:-4]))
            sudo('sudo rm ./{}'.format(ff))
        with cd('/data/web_static/'):
            run('sudo mv releases/{}/web_static/* /data/web_static/releases/\
                {}/'.format(ff[:-4], ff[:-4]))
            run('sudo rm -rf ./current')
            run('sudo ln -s /data/web_static/releases/{}/\
                 /data/web_static/current'.format(ff[:-4]))
        return True
    except Exception:
        return False
