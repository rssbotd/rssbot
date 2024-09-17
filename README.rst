R S S B O T
===========


**NAME**

::

    RSSBOT - 24/7 Feed Fetcher


**SYNOPSIS**

::

    rssbot <cmd> [key=val] [key==val]
    rssbotc [-v] [-i]
    rssbotd
    rssbots


**DESCRIPTION**

::

    RSSBOT is a python3 bot able to display rss feeds in your channel.

    RSSBOT comes with a cli to configure and a daemon to run in the
    background, hooking the daemon in systemd brings a 24/7 available
    rssbot in your channel.


**INSTALL**

::

    $ pipx install rssbot
    $ pipx ensurepath


**CONFIGURATION**

::

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


**SYSTEMD**

::

    $ rssbot srv > rssbot.service
    $ sudo mv rssbot.service /etc/systemd/system/
    $ sudo systemctl enable rssbot --now

    joins #rssbot on localhost


**COMMANDS**

::

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


**FILES**

::

    ~/.rssbot
    ~/.local/bin/rssbot
    ~/.local/bin/rssbotc
    ~/.local/bin/rssbotd
    ~/.local/bin/rssbots
    ~/.local/pipx/venvs/rssbot/


**AUTHOR**

::

    Bart Thate <rssbotd@gmail.com>


**COPYRIGHT**

::

    RSSBOT is Public Domain.
