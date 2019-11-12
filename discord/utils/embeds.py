import discord
from .lib import *
from datetime import datetime

def successful_role_assigned(bot, role):
	embed = discord.Embed(title="Added to {}!".format(role), color=COLOR_SUCCESS, timestamp=datetime.now())
	embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=bot.user.avatar_url)
	return embed