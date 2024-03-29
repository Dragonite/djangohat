import logging
import os
import sys
from datetime import datetime

import django
from discord.ext import commands
from django.conf import settings
from discord.utils import get
from utils.embeds import *

import discord

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'whitehat.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whitehat.settings")
django.setup()

bot = commands.Bot(command_prefix=settings.DISCORD_BOT_PREFIX)

logging.basicConfig(filename='discord/logs/whitehat.log'.format(datetime.today().strftime('%Y-%m-%d')), format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


@bot.event
async def on_ready():
    activity = discord.Activity(name="you hack ethically!", type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    logging.warning("Bot started")
    print("Bot connected!")


@bot.event
async def on_raw_reaction_add(payload):
	guild = bot.get_guild(settings.GUILD_ID)
	member = guild.get_member(payload.user_id)
	# Welcome reaction role assignment
	if payload.message_id == settings.WELCOME_MESSAGE and payload.channel_id == settings.WELCOME_CHANNEL:
		if payload.emoji.id == settings.EMOJI_HTB:
			role = get(guild.roles, name="Hack The Box")
			await member.add_roles(role)
			logging.warning("{} added to {}".format(member.nick, "Hack The Box"))
			await member.send(embed=successful_role_assigned(bot, "Hack The Box"))
		if payload.emoji.id == settings.EMOJI_HELPER:
			role = get(guild.roles, name="General Help")
			await member.add_roles(role)
			logging.warning("{} added to {}".format(member.nick, "Helper"))
			await member.send(embed=successful_role_assigned(bot, "Helper"))
		if payload.emoji.id == settings.EMOJI_LINUX:
			role = get(guild.roles, name="Linux")
			await member.add_roles(role)
			logging.warning("{} added to {}".format(member.nick, "Linux"))
			await member.send(embed=successful_role_assigned(bot, "Linux"))


@bot.event
async def on_raw_reaction_remove(payload):
	guild = bot.get_guild(settings.GUILD_ID)
	member = guild.get_member(payload.user_id)
	# Welcome reaction role removal
	if payload.message_id == settings.WELCOME_MESSAGE and payload.channel_id == settings.WELCOME_CHANNEL:
		if payload.emoji.id == settings.EMOJI_HTB:
			role = get(guild.roles, name="Hack The Box")
			await member.remove_roles(role)
			logging.warning("{} removed from {}".format(member.nick, "Hack The Box"))
			await member.send(embed=successful_role_removed(bot, "Hack The Box"))
		if payload.emoji.id == settings.EMOJI_HELPER:
			role = get(guild.roles, name="General Help")
			await member.remove_roles(role)
			logging.warning("{} removed from {}".format(member.nick, "Helper"))
			await member.send(embed=successful_role_removed(bot, "Helper"))
		if payload.emoji.id == settings.EMOJI_LINUX:
			role = get(guild.roles, name="Linux")
			await member.remove_roles(role)
			logging.warning("{} removed from {}".format(member.nick, "Linux"))
			await member.send(embed=successful_role_removed(bot, "Linux"))


initial_extensions = ['cogs.link', 'cogs.event', 'cogs.register', 'cogs.profile']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(settings.DISCORD_BOT_TOKEN, bot=True, reconnect=True)
