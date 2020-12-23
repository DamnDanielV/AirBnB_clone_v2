#!/usr/bin/python3
"""generarates a tgz archive in the servers"""
from fabric.api import *
from datetime import datetime
from os.path import isfile

env.use_ssh_config = True
env.user = 'ubuntu'
env.hosts = ['34.74.16.58', '35.196.98.184']
env.key_fileff = '~/.ssh/holberton'


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
    put(archive_path, '/tmp/')
    run("mkdir -p /data/web_static/releases/{}/".format(ff[:-4]))
    with cd('/tmp/'):
        run('tar xzf {} -C /data/web_static/releases/{}/'.format(ff,
            ff[:-4]))
        sudo('rm ./{}'.format(ff))
    with cd('/data/web_static/'):
        run('mv releases/{}/web_static/* /data/web_static/releases/{}/'
            .format(ff[:-4], ff[:-4]))
        run('rm -rf ./current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(ff[:-4]))
    return True
