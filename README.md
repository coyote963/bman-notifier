# bman-notifier / Coyote Bot
![Image of Coyote Bot](https://i.ibb.co/2Ywpxqm/coyotebot.jpg)

A system for notifying users when a server reaches capacity

Contains two components: first component is for connection to a spasman server. it has code from his example rcon file found here https://github.com/Spasman/rcon_example

The second portion is a discord bot that connects to a channel and posts pings to users when the first component detects that the number of players in the spasman server reach a certain number.

This was tested on python 3.7. Not sure if it'll work for earlier ones. Requires

discord.py library v=1.2.3

configparser

### Settings files ###

There are two settings files that will need to be created

./bmsettings.ini

```
[bm]
ip = 127.0.0.1
port = 43210
password = admin
```

./sqlscripts/discordsettings.ini
```
[connections]
filelocation = C:\path\to\your\sqlite\database.db
token = ThisIsYourDiscordBotToken
url = https://discordapp.com/api/webhooks/thisisyourwebhookurl
```

Add a way for users to configure their time delta and be notified more/less frequently

### sqlite ###

Install sqlite `https://www.sqlite.org/download.html`

Instantiate an empty db

run createdb.py to create your database file

### todo ###

There is a few things that I still need to do, and help would be appreciated.

I need to add a way for users to set custom time limits for sending notifications, add commands to the discord bot such that it can pull up stats on the player

### file structure ###

`example.py` is where json packets get parsed. start parser should be the entry point where you read packets by passing in a callback

`coybot.py` a minimalist discord bot for configuring their notifications

`helpers.py` useful functions for sockets

`matchupdater.py` contains a process that requests match info every X seconds

`parseconfigs.py` parses the config file

`rcontypes.py` enums for request_event, request_data

`startprocessing.py` Entry function for the matchupdater and the example.py.


#### In the sqlscripts ####

This folder isn't really just for sql scripts, it just contains some useful functionality for SQL on top of discord functions

`createdb`

`createtable`

`discord_webhook` contains a single function for sending a webhook request out

`insertdiscorduser.py` the only useful function here is the initial script

`parsediscordconfigs.py`

`sqlmethods.py` the crud operations for discord users go here

`notify.py` the logic for notifying users
