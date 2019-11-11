import logging
import os
import sys
from datetime import datetime

import django
from discord.ext import commands
from django.conf import settings

import discord

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'whitehat.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whitehat.settings")
django.setup()

prefix = settings.DISCORD_BOT_PREFIX

bot = commands.Bot(command_prefix=settings.DISCORD_BOT_PREFIX)

logging.basicConfig(filename='discord/logs/whitehat-{}.log'.format(datetime.today().strftime('%Y-%m-%d')), filemode='w', format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


@bot.event
async def on_ready():
    activity = discord.Activity(name="you hack ethically!", type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    logging.warning("Bot started")
    print("Bot connected!")


initial_extensions = ['cogs.link']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(settings.DISCORD_BOT_TOKEN, bot=True, reconnect=True)
