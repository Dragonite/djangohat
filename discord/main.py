import discord
from discord.ext import commands
from django.conf import settings
from utils.lib import *
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'whitehat.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whitehat.settings")

prefix = settings.DISCORD_BOT_PREFIX

bot = commands.Bot(command_prefix=settings.DISCORD_BOT_PREFIX)


@bot.event
async def on_ready():
    activity = discord.Activity(name="you hack ethically!", type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    print("Bot connected!")


@bot.command()
async def register(ctx, *args):
    for arg in args:
        await ctx.send(arg)


bot.run(settings.DISCORD_BOT_TOKEN)