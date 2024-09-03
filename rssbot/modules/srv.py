# This file is placed in the Public Domain.


"service"


import getpass
import os


from ..config import Config as Cfg


def srv(event):
    "create service file (pipx)."
    username  = getpass.getuser()
    path = os.path.normpath(f"/home/{username}/.local/bin/")
    txt = f"""[Unit]
Description=24/7 Feed Fetcher
Requires=network-online.target
After=network-online.target

[Service]
Type=simple
User={username}
Group={username}
ExecStart={path}/{Cfg.name}s
Restart=no

[Install]
WantedBy=basic.target"""
    event.reply(txt)


srv.target = "cli"
