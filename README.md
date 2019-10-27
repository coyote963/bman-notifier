# bman-notifier

A system for notifying users when a server reaches capacity

Contains two components: first component is for connection to a spasman server. it has code from his example rcon file found here https://github.com/Spasman/rcon_example

The second portion is a discord bot that connects to a channel and posts pings to users when the first component detects that the number of players in the spasman server reach a certain number.

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

