# This file is placed in the Public Domain.
# pylint: disable=C,I,R


"list of commands"


from rssbot.command import Commands
from rssbot.object  import keys


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(keys(Commands.cmds))))
