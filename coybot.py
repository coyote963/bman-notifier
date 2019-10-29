import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

from datetime import datetime
from sqlscripts.sqlmethods import create_discorduser, delete_discord_user, get_discord_user, create_connection,update_threshold
from sqlscripts.parsediscordconfigs import token, filelocation
client = discord.Client()
conn = create_connection(filelocation)

@client.event
async def on_ready():
    print('Just joined... {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!svl'):
        discord_id = get_discord_user(conn, str(message.author.id))
        if discord_id == None:
            now = str(datetime.now())
            create_discorduser(conn, (message.author.id, 5, now, now))
            conn.commit()
            await message.channel.send('Added u to the svl mailing list!')

        else:
            delete_discord_user(conn, message.author.id)
            conn.commit()
            await message.channel.send('Removed u from the svl mailing list!')
    if message.content.startswith('!setcap'):
        discord_id = get_discord_user(conn, str(message.author.id))
        if discord_id == None:
            await message.channel.send('U need to be registered in this list before you can set cap')
        else:
            cropped_message = message.content.split("!setcap ")
            if (len(cropped_message) > 1):
                new_threshold = message.content.split("!setcap ")[1]
                if new_threshold.isdigit() and int(new_threshold) > 0 and int(new_threshold) < 10:
                    user_input = int(new_threshold)
                    update_threshold(conn, discord_id[0], user_input)
                    await message.channel.send('Updated, now it is {}'.format(user_input))
                else:
                    await message.channel.send('Check ur syntax')
    if message.content.startswith("!getcap"):
        discord_id = get_discord_user(conn, str(message.author.id))
        if discord_id == None:
            await message.channel.send('U need to be registered in this list before you can set cap')
        else:
            await message.channel.send('Your current cap is set to {}'.format(discord_id[1]))
#change this to coybot?
client.run(token)