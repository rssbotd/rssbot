**NAME**

| ``rssbot`` - 24/7 Feed Fetcher, a contribution back to society.
|


**SYNOPSIS**

| ``rssbot [-h] [-a] [-c] [-d] [-l LEVEL] [-m MODS] [-n] [-s] [-t] [-v] [-w] [--local] [--wdr WDR]``
|
| ``rssbot <cmd> [key=val] [key==val]``
| ``rssbot -cvaw [mods=mod1,mod2]``
|

**DESCRIPTION**

``rssbot`` is a python3 bot able to display rss feeds in your channel.

``rssbot`` comes with a cli to configure and a daemon to run in the
background, hooking the daemon in systemd brings a 24/7 available
rssbot in your channel.

``rssbot`` is Public Domain.


**INSTALL**


installation is done with pipx

| ``$ pipx install rssbot``
| ``$ pipx ensurepath``
|
| <new terminal>
|
| ``$ rssbot srv > rssbot.service``
| ``$ sudo mv rssbot.service /etc/systemd/system/``
| ``$ sudo systemctl enable rssbot --now``
|
| joins ``#rssbot`` on localhost
|


**USAGE**


use ``rssbot`` to control the program, default it does nothing

| ``$ rssbot``
| ``$``
|

the -h option will show you possible options

| ``$ rssbot -h``
|
| options:
|
| ``-h,--help          show this help message and exit``
| ``-a,--all           load all modules``
| ``-c,--console       start console``
| ``-d,--daemon        start background daemon``
| ``-l,--level LEVEL   set loglevel``
| ``-m,--mods MODS     modules to load``
| ``-n,--noignore      disable ignore```
| ``-s,--service       start service``
| ``-t,--threaded      enable multiple workers``
| ``-v,--verbose       enable verbose``
| ``-w,--wait          wait for services to start``
| ``--local            use local mods directory``
| ``--wdr <WDR>        set working directory``
|

see list of commands

| ``$ rssbot cmd``
| ``cfg,cmd,dne,dpl,err,exp,imp,log,mod,mre,nme,``
| ``pwd,rem,req,res,rss,srv,syn,tdo,thr,upt``
|

start console

| ``$ rssbot -c``
|

start console and run irc and rss clients

| ``$ rssbot -c init=irc,rss``
|

list available modules

| ``$ rssbot mod``
| ``err,flt,fnd,irc,llm,log,mbx,mdl,mod,req,rss,``
| ``rst,slg,tdo,thr,tmr,udp,upt``
|

start daemon

| ``$ rssbot -d``
| ``$``
|

start service

| ``$ rssbot -s``
| ``<runs until ctrl-c>``
|


**COMMANDS**


here is a list of available commands

| ``cfg`` - irc configuration
| ``cmd`` - commands
| ``dpl`` - sets display items
| ``err`` - show errors
| ``exp`` - export opml (stdout)
| ``imp`` - import opml
| ``log`` - log text
| ``mre`` - display cached output
| ``pwd`` - sasl nickserv name/pass
| ``rem`` - removes a rss feed
| ``res`` - restore deleted feeds
| ``req`` - reconsider
| ``rss`` - add a feed
| ``syn`` - sync rss feeds
| ``tdo`` - add todo item
| ``thr`` - show running threads
| ``upt`` - show uptime
|

**CONFIGURATION**


irc

| ``$ rssbot cfg irc server=<server>``
| ``$ rssbot cfg irc channel=<channel>``
| ``$ rssbot cfg irc nick=<nick>``
|

sasl

| ``$ rssbot pwd <nsnick> <nspass>``
| ``$ rssbot cfg irc password=<frompwd>``
|

rss

| ``$ rssbot rss <url>``
| ``$ rssbot dpl <url> <item1,item2>``
| ``$ rssbot rem <url>``
| ``$ rssbot nme <url> <name>``
|

opml

| ``$ rssbot exp``
| ``$ rssbot imp <filename>``
|


**PROGRAMMING**

| rssbot has it's user modules in the ~/.rssbot/mods directory so for a
| hello world command you would  edit a file in ~/.rssbot/mods/hello.py
| and add the following
|

::

    def hello(event):
        event.reply("hello world !!")


|
| typing the hello command would result into a nice hello world !!
|

::

    $ rssbot hello
    hello world !!


|
| commands run in their own thread and the program borks on exit to enable a
| short debug cycle, output gets flushed on print so exceptions appear in the
| systemd logs. modules can contain your own written python3 code.
|


**FILES**

|
| ``~/.rssbot``
| ``~/.local/bin/rssbot``
| ``~/.local/share/pipx/venvs/rssbot/*``
|

**AUTHOR**

|
| ``Bart Thate`` <``rssbotd@gmail.com``>
|

**COPYRIGHT**

|
| ``rssbot`` is Public Domain.
|

