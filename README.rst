**NAME**

::

   rssbot- 24/7 IRC Feed Fetcher


**SYNOPSIS**

::

    rssbot [options] [cmd] [key=val] [key==val] [key-=val] [arguments]
    rssbot -h


**DESCRIPTION**

::

    RSSBOT is a python3 bot able to display rss feeds in your channel.

    RSSBOT comes with a cli to configure and a daemon to run in the
    background, hooking the daemon in systemd brings a 24/7 available
    rssbot in your channel.

    RSSBOT is Public Domain.


**INSTALL**

::

    due to difficulty accessing my pypi account you can use my git repo

    $ git clone ssh://git@github.com/rssbotd/rssbot
    $ cd rssbot
    $ pipx install . --force
    $ pipx ensurepath

    <new terminal>

    $ rssbot --admin srv > rssbot.service
    $ sudo mv rssbot.service /etc/systemd/system/
    $ sudo systemctl enable rssbot --now

    joins ``#rssbot`` on localhost


**USAGE**


::

    the -h option will show you possible options

    usage: rssbot [options] [cmd] [key=val] [key==val] [key-=val] [arguments]

    RSSBOT

    options:
      -h, --help         show this help message and exit
      -c, --console      start a console.
      -d, --daemon       run as background daemon.
      -s, --service      run as service.

      -a, --all          load all modules.
      -v, --verbose      enable verbose.
      -w, --wait         wait for services to start.

      -l, --level level  set loglevel.
      -m, --mods m1,m2   modules to load.
      -p, --path path    path to modules directory.

      --admin            enable admin mode.
      --scanner          do full modules scan on boot.
      --wdr WDR          set modules directory.

    use "rssbot cmd" for a list of commands.

::

    use rssbot to control the program, default it does nothing

    $ rssbot
    $

    see list of commands

    $ rssbot cmd
    cfg,cmd,dne,dpl,err,exp,imp,log,mod,mre,nme,
    pwd,rem,req,res,rss,srv,syn,tdo,thr,upt


    start daemon

    $ rssbotd --daemon
    $


    start service

    $ rssbotd --service
    <runs until ctrl-c>


**COMMANDS**

::

    here is a list of available commands


    cfg - irc configuration
    cmd - commands
    dpl - sets display items
    err - show errors
    exp - export opml (stdout)
    imp - import opml
    log - log text
    mre - display cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    res - restore deleted feeds
    rss - add a feed
    syn - sync rss feeds
    tdo - add todo item
    thr - show running threads
    upt - show uptime


**CONFIGURATION**

::

    irc

    $ rssbot cfg irc server=<server>
    $ rssbot cfg irc channel=<channel>
    $ rssbot cfg irc nick=<nick>

    sasl

    $ rssbot pwd <nsnick> <nspass>
    $ rssbot cfg irc password=<frompwd>

    rss

    $ rssbot rss <url>
    $ rssbot dpl <url> <item1,item2>
    $ rssbot rem <url>
    $ rssbot nme <url> <name>

    opml

    $ rssbot exp
    $ rssbot imp <filename>


**FILES**

::

    ~/.rssbot
    ~/.local/bin/rssbot
    ~/.local/share/pipx/venvs/rssbot/*


**AUTHOR**

::

    Bart Thate <rssbotd@gmail.com>


**COPYRIGHT**

::

   RSSBOT is Public Domain.
