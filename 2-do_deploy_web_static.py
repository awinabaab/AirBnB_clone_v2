#!/usr/bin/python3
"""Fabric file to automate deployment of web_static"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['100.26.158.187', '34.204.60.177']
env.user = 'ubuntu'


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    directory_name = "versions"
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

    current_date = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f"web_static_{current_date}.tgz"
    archive_path = os.path.join(directory_name, archive_name)

    try:
        local(f"tar -cvzf {archive_path} web_static")
    except Exception:
        return None

    return archive_path


def do_deploy(archive_path):
    """Distributes an archive to your webservers"""
    try:
        if os.path.exists(archive_path):
            return False

        archive_name_tgz = archive_path.split('/')[-1]
        archive_name = archive_name_tgz.replace('.tgz', '')
        releases_path = "/data/web_static/releases"
        extract_path = f"{releases_path}/{archive_name}"

        put(archive_path, '/tmp/')

        run(f"mkdir -p {extract_path}")

        run(f"tar -xzf /tmp/{archive_name_tgz} -C {extract_path}")

        run(f"rm /tmp/{archive_name_tgz}")

        run(f"mv {extract_path}/web_static/* {extract_path}")

        run(f"rm -rf {extract_path}/web_static")

        run("rm -rf /data/web_static/current")

        run(f"ln -s {releases_path}/{archive_name}/ /data/web_static/current")

        print("New version deployed!")

        return True
    except Exception:
        return False
