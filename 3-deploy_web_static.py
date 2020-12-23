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
    ans = local("tar czvf ./versions/web_static_{}.tgz ./web_static/*"
                .format(datetime.now().strftime("%Y%m%d%I%M%S")))
    if ans.succeeded:
        return ("./versions/web_static_{}.tgz"
                .format(datetime.now().strftime("%Y%m%d%I%M%S")))
    else:
        return None


def do_deploy(archive_path):
    """
        distributes an archive to your web servers
    """
    if (isfile(archive_path) is False):
        return False
    ff = archive_path.split('/')[-1]
    c2 = 'sudo mv releases/{}/web_static/* /data/web_static/releases/{}/'
    c3 = 'sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'
    try:
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}/".format(ff[:-4]))
        with cd('/tmp/'):
            run('sudo tar xzf {} -C /data/web_static/releases/{}/'.format(ff,
                ff[:-4]))
            sudo('sudo rm ./{}'.format(ff))
        with cd('/data/web_static/'):
            run(c2.format(ff[:-4], ff[:-4]))
            run('sudo rm -rf ./current')
            run(c3.format(ff[:-4]))
        return True
    except Exception:
        return False


def deploy():
    """
        creates and distributes an archive to your web servers
    """
    try:
        path_file = do_pack()
        return do_deploy(path_file)
    except Exception:
        return False
