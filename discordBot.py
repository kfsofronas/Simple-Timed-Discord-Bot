# Work with Python 3.6
import discord
import time
from discord.ext import commands
import random
import asyncio

client = commands.Bot();
client.remove_command('help')

BOTTOKEN =  '''your bot token in string form'''

isOn = False

@client.event
async def on_message(message):
    global isOn

    await client.process_commands(message)
    if message.author == client.user:
        return

    elif (isOn):
        print("isOn is " + str(isOn))
        return
    else:

        print("recieved message: " + message.content)
        await sendLink(message)
        return

async def sendLink(message):
    await client.wait_until_ready()
    global isOn

    channel = message.channel

    if(channel.id != str('''channel ID where you want to send the message in integer form''')):
        print("wrong channel, brother")

        return
    else:
        isOn = True
        while not client.is_closed:
            await client.send_message(channel, '''funny image or message in string form''' "")
            await asyncio.sleep((math.random()*18000)+3600) #or however long you want it to wait between messages, in seconds


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(BOTTOKEN)
