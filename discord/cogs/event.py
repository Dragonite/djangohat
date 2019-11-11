import discord
import logging
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions
from users.models import *
from events.models import *
from utils.lib import *
from django.conf import settings

logger = logging.getLogger()

class EventCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	# Creates the default help embed.
	def event_help(self):
		embed = discord.Embed(title='Create an Event',
							  description='To create an event, please follow the following structure with the `!event` command.\n```!event\n<Title>\n<Location>\n<Time>\n<Information>```',
							  color=COLOR_INFO, timestamp=datetime.datetime.now())
		embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
		return embed

	# Gets the next meeting date and time. By default, the time will be the next Wednesday 3PM
	# inclusive of the current day, i.e. If it is Wednesday, it will return today's date 3PM.
	def get_next_default_meeting_time(self, d, weekday):
		days_ahead = (weekday - d.weekday()) % 7
		if days_ahead < 0: days_ahead += 7
		next_date_string = (d + datetime.timedelta(days_ahead)).strftime("%A %-d %B at 3PM")
		return next_date_string

	# Creates a default event with next Wednesday 3PM as the time, and the default Event model constants.
	def default_event(self):
		embed = discord.Embed(title=Event.DEFAULT_TITLE, color=COLOR_INFO, timestamp=datetime.datetime.now())
		embed.add_field(name="Location", value=Event.DEFAULT_LOCATION, inline=False)
		embed.add_field(name="Time", value=self.get_next_default_meeting_time(datetime.datetime.now(), WEDNESDAY), inline=False)
		embed.add_field(name="Information", value=Event.DEFAULT_INFO, inline=False)
		embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
		return embed

	# Creates a custom event based on argument list, created through the event command.
	def custom_event(self, arg_list):
		title = arg_list[0]
		location = arg_list[1]
		time = arg_list[2]
		information = arg_list[3]
		embed = discord.Embed(title=title, color=COLOR_INFO, timestamp=datetime.datetime.now())
		embed.add_field(name="Location", value=location, inline=False)
		embed.add_field(name="Time", value=time, inline=False)
		embed.add_field(name="Information", value=information, inline=False)
		embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
		return embed

	# Creates a custom event with the user's avatar and name when successful.
	def successful_custom_event(self, ctx):
		embed = discord.Embed(title="Event successfully created!", color=COLOR_SUCCESS, timestamp=datetime.datetime.now())
		embed.set_footer(text="Created by {}".format(ctx.message.author.display_name), icon_url=ctx.message.author.avatar_url)
		return embed

	# Creates a custom event with the user's avatar and name when successful.
	def failed_custom_event(self, ctx):
		embed = discord.Embed(title="Event creation failed!", color=COLOR_DANGER, timestamp=datetime.datetime.now())
		embed.set_footer(text="Attempted by {}".format(ctx.message.author.display_name), icon_url=ctx.message.author.avatar_url)
		return embed

	@commands.command()
	@has_permissions(administrator=True)
	async def event(self, ctx, *, arg=None):
		if arg:
			arg_list = arg.split('\n')
			channel = self.bot.get_channel(settings.EVENT_CHANNEL)
			# For !event default command, posts the default event
			if len(arg_list) == 1 and arg == 'default':
				arg_list[0]
				try:
					await channel.send(embed=self.default_event())
					await(await channel.send("@everyone")).delete()
					Event.objects.create(time=self.get_next_default_meeting_time(datetime.datetime.now(), WEDNESDAY))
					logger.warning("Event created by %s", ctx.message.author.display_name)
					await ctx.send(embed=self.successful_custom_event(ctx))
				except:
					await ctx.send(embed=self.failed_custom_event(ctx))
			# For a custom event
			elif len(arg_list) == 4:
				title = arg_list[0]
				location = arg_list[1]
				time = arg_list[2]
				info = arg_list[3]
				try:
					await channel.send(embed=self.custom_event(arg_list))
					await(await channel.send("@everyone")).delete()
					Event.objects.create(title=title, location=location, time=time, info=info)
					logger.warning("Event created by %s", ctx.message.author.display_name)
					await ctx.send(embed=self.successful_custom_event(ctx))
				except:
					await ctx.send(embed=self.failed_custom_event(ctx))
			else:
				await ctx.send(embed=self.event_help())
		else:
			await ctx.send(embed=self.event_help())
						
def setup(bot):
	bot.add_cog(EventCog(bot))