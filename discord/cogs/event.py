import discord
import logging
import datetime
from discord.ext import commands
from users.models import *
from utils.lib import *

logger = logging.getLogger()

class EventCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Gets the next meeting date and time. By default, the time will be the next Wednesday 3PM
    # inclusive of the current day, i.e. If it is Wednesday, it will return today's date 3PM.
    def get_next_default_meeting_time(self, d, weekday):
        days_ahead = (weekday - d.weekday()) % 7
        if days_ahead < 0: days_ahead += 7
        next_date_string = (d + datetime.timedelta(days_ahead)).strftime("%A %-d %B at 3PM")
        return next_date_string

    @commands.command()
    async def event(self, ctx, *, arg=None):
        if arg:
            arg_list = arg.split('\n')
            if len(arg_list) == 1 and arg == 'default':
                await ctx.send("arg")
        else:
            await ctx.send("no arg")

        # print(DEFAULT_LOCATION)
        # print(arg)
        # print(self.get_next_default_meeting_time(datetime.datetime.now(), WEDNESDAY))
                        

def setup(bot):
    bot.add_cog(EventCog(bot))