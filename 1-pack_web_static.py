#!/usr/bin/python3
"""Fabric file to automate deployment of web_static"""

from fabric.api import local
from datetime import datetime
import os


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
