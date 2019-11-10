import discord
import django
from discord.ext import commands
from django.conf import settings
from utils.lib import *
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'whitehat.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whitehat.settings")
django.setup()
from users.models import *

prefix = settings.DISCORD_BOT_PREFIX

bot = commands.Bot(command_prefix=settings.DISCORD_BOT_PREFIX)

@bot.event
async def on_ready():
    activity = discord.Activity(name="you hack ethically!", type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    print("Bot connected!")

# @bot.event
# async def on_message(message):
#     if message.channel.type == discord.ChannelType.private and message.author != bot.user:
#         profile = Users.objects.filter(discord_id=message.author.id)
#         print(profile)
#         await message.channel.send(message.content)
#     print(message.channel.type)
    # if message.channel is None and message.author != bot.user:
    #     # profile = Users.objects.filter(discord_id=message.author.id)
    #     # print(profile)
    #     # await bot.send_message(message.content)
    #     print('hi')


@bot.command()
async def register(ctx, *args):
    for arg in args:
        await ctx.send(arg)

initial_extensions = ['cogs.link']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


bot.run(settings.DISCORD_BOT_TOKEN, bot=True, reconnect=True)