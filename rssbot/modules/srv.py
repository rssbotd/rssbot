# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W0212
# ruff: noqa: E402


"service"


import os


from ..config  import Config


Cfg = Config()


def srv(event):
    "create service file (pipx)."
    import getpass
    if event.args:
        username = event.args[0]
    else:
        username  = getpass.getuser()
    path = os.path.normpath(f"/home/{username}/.local/bin/")
    txt = f"""[Unit]
Description={Cfg.name.upper()}
Requires=network-online.target
After=network-online.target

[Service]
Type=simple
User={username}
Group={username}
ExecStartPre={path}/{Cfg.name} skl
ExecStart={path}/{Cfg.name}s
Restart=no

[Install]
WantedBy=multi-user.target"""
    event.reply(txt)


srv.target = "cli"
