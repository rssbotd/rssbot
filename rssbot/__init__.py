# This file is placed in the Public Domain.
# pylint: disable=C,I,R


"""24/7 Feed Fetcher


SYNOPSIS

    rssbot <cmd> [key=val] [key==val]

DESCRIPTION

    RSSBOT is a python3 bot able to display rss feeds in your channel.

    RSSBOT comes with a cli to configure and a daemon to run in the
    background, hooking the daemon in systemd brings a 24/7 available
    rssbot in your channel.

INSTALL

    $ pipx install rssbot
    $ pipx ensurepath

    <new terminal>

    $ rssbot srv > rssbot.service
    $ sudo mv rssbot.service /etc/systemd/system/
    $ sudo systemctl enable rssbot --now
    $ rssbot rss <url>

    joins #rssbot on localhost
    
COMMANDS

    cfg - irc configuration
    cmd - commands
    dpl - sets display items
    err - show errors
    exp - export opml (stdout)
    imp - import opml
    mre - display cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    res - restore deleted feeds
    rss - add a feed
    srv - create service file
    syn - sync rss feeds
    thr - show running threads

CONFIGURATION

    irc

    $ rssbot cfg server=<server>
    $ rssbot cfg channel=<channel>
    $ rssbot cfg nick=<nick>

    sasl
 
    $ rssbot pwd <nsvnick> <nspass>
    $ rssbot cfg password=<frompwd>

    rss

    $ rssbot rss <url>
    $ rssbot dpl <url> <item1,item2>
    $ rssbot rem <url>
    $ rssbot res <url>
    $ rssbot nme <url> <name>

    opml

    $ rssbot exp
    $ rssbot imp <filename>

COPYRIGHT

    RSSBOT is Public Domain.


"""


__author__ = "\nBart Thate <rssbotd@gmail.com>"
