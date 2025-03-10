# This file is placed in the Public Domain.


"man page"


from ..cmnd import Config


TXT = """%s
%s


**NAME**


|
| ``%s`` - %s
|


**SYNOPSIS**


|
| ``%s <cmd> [key=val] [key==val]``
| ``%s -cvw [init=mod1,mod2]``
| ``%s -d`` 
| ``%s -s``
|

**DESCRIPTION**


``%s`` has all you need to program a unix cli program, such as disk
perisistence for configuration files, event handler to handle the
client/server connection, deferred exception handling to not crash
on an error, etc.

``%s`` contains python3 code to program objects in a functional way.
It provides a base Object class that has only dunder methods, methods
are factored out into functions with the objects as the first argument.
It is called Object Programming (OP), OOP without the oriented.

``%s`` contains python3 code to program objects in a functional way.
it provides an "clean namespace" Object class that only has dunder
methods, so the namespace is not cluttered with method names. This
makes storing and reading to/from json possible.

``%s`` has a demo bot, it can connect to IRC, fetch and display RSS
feeds, take todo notes, keep a shopping list and log text. You can
run it under systemd for 24/7 presence in a IRC channel.


``%s`` is Public Domain.


**INSTALL**


installation is done with pipx

|
| ``$ pipx install %s``
| ``$ pipx ensurepath``
|
| <new terminal>
|
| ``$ %s srv > %s.service``
| ``$ sudo mv %s.service /etc/systemd/system/``
| ``$ sudo systemctl enable %s --now``
|
| joins ``#%s`` on localhost
|


**USAGE**


use ``%s`` to control the program, default it does nothing

|
| ``$ %s``
| ``$``
|

see list of commands

|
| ``$ %s cmd``
| ``cfg,cmd,dne,dpl,err,exp,imp,log,mod,mre,nme,``
| ``pwd,rem,req,res,rss,srv,syn,tdo,thr,upt``
|

start console

|
| ``$ %s -c``
|

start console and run irc and rss clients

|
| ``$ %s -c init=irc,rss``
|

list available modules

|
| ``$ %s mod``
| ``err,flt,fnd,irc,llm,log,mbx,mdl,mod,req,rss,``
| ``rst,slg,tdo,thr,tmr,udp,upt``
|

start daemon

|
| ``$ %s -d``
| ``$``
|

start service

|
| ``$ %s -s``
| ``<runs until ctrl-c>``
|


**COMMANDS**


here is a list of available commands

|
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

|
| ``$ %s cfg server=<server>``
| ``$ %s cfg channel=<channel>``
| ``$ %s cfg nick=<nick>``
|

sasl

|
| ``$ %s pwd <nsnick> <nspass>``
| ``$ %s cfg password=<frompwd>``
|

rss

|
| ``$ %s rss <url>``
| ``$ %s dpl <url> <item1,item2>``
| ``$ %s rem <url>``
| ``$ %s nme <url> <name>``
|

opml

|
| ``$ %s exp``
| ``$ %s imp <filename>``
|


**PROGRAMMING**


``%s`` has it's modules in the package, so edit a file in %s/modules/<name>.py
and add the following for ``hello world``

::

    def hello(event):
        event.reply("hello world !!")


save this and recreate the dispatch table

|
| ``$ %s tbl > %s/lookup.py``
|

``%s`` can execute the ``hello`` command now.

|
| ``$ %s hello``
| ``hello world !!``
|

commands run in their own thread, errors are deferred to not have loops
blocking/breaking on exception and can contain your own written python3
code, see the nixt/modules directory for examples.


**FILES**

|
| ``~/.%s``
| ``~/.local/bin/%s``
| ``~/.local/pipx/venvs/%s/*``
|

**AUTHOR**

|
| ``Bart Thate`` <``nixtniet@gmail.com``>
|

**COPYRIGHT**

|
| ``%s`` is Public Domain.
|
"""


def spaced(txt):
    res = ""
    for char in txt[:-1]:
       res += f"{char} "
    res += txt[-1]
    return res


def man(event):
    event.reply(TXT % tuple(
                            [spaced(Config.name.upper()), "="*(2*len(Config.name)-1), Config.name, Config.name.upper()]
                            + 4* [Config.name]
                            + 5*[Config.name.upper()]
                            + 34*[Config.name]
                            + [Config.name.upper()]
                           )
               )
