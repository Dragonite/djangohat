import discord
from django.conf import settings
from utils.lib import *
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'whitehat.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whitehat.settings")

prefix = settings.DISCORD_BOT_PREFIX

client = discord.Client()


@client.event
async def on_ready():
    activity = discord.Activity(name="you hack ethically!", type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("Bot connected!")


@client.event
async def on_message(message):
    # Prevent infinite bot loop
    checkBotLoop(message, client)

    # Get parameters

    params = message.content.split()

    if len(params) == 0:
        return
    else:
        params[0] = params[0][1:]

    if params[0] == 'test':
        await message.channel.send("hello")


client.run(settings.DISCORD_BOT_TOKEN)