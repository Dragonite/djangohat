import discord
import logging
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions
from users.models import *
from utils.lib import *

logger = logging.getLogger()

class EventCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def event_help(self):
        embed = discord.Embed(title='Create an Event',
                              description='To create an event, please follow the following structure with the `!event` command.\n```!event\n<Title>\n<Location>\n<Time>\n<Information>```',
                              color=COLOR_INFO, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed


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

    # Gets the next meeting date and time. By default, the time will be the next Wednesday 3PM
    # inclusive of the current day, i.e. If it is Wednesday, it will return today's date 3PM.
    def get_next_default_meeting_time(self, d, weekday):
        days_ahead = (weekday - d.weekday()) % 7
        if days_ahead < 0: days_ahead += 7
        next_date_string = (d + datetime.timedelta(days_ahead)).strftime("%A %-d %B at 3PM")
        return next_date_string

    @commands.command()
    @has_permissions(administrator=True)
    async def event(self, ctx, *, arg=None):
        if arg:
            arg_list = arg.split('\n')
            if len(arg_list) == 1 and arg == 'default':
                arg_list[0]
                await ctx.send("arg")
            elif len(arg_list) == 4:
                await ctx.send(embed=self.custom_event(arg_list))
            else:
                await ctx.send(embed=self.event_help())
        else:
            await ctx.send(embed=self.event_help())

        # print(DEFAULT_LOCATION)
        # print(arg)
        # print(self.get_next_default_meeting_time(datetime.datetime.now(), WEDNESDAY))
                        

def setup(bot):
    bot.add_cog(EventCog(bot))