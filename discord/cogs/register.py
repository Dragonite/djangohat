import discord
import logging
import datetime
from discord.ext import commands
from users.models import *
from utils.lib import *

logger = logging.getLogger()

class RegisterCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def register(self, ctx, *, arg=None):
        if arg:
            arg_list = arg.split('\n')
            print(arg_list)
            # Name
            # Role
            # Link
            # HackTheBox

            # Bare minimum is name role and link, optional hackthebox url.
            if len(arg_list) == 2:
                name, role = arg_list
                profile, created = Users.objects.get_or_create(discord_id=ctx.message.author.id)
                if created:
                    profile.description = role
                    profile.full_name = name
                    profile.discord_tag = "{}#{}".format(ctx.message.author.name, ctx.message.author.discriminator)
                    profile.save()
                    # Profile created embed
                else:
                    # Profile already exists
                    await ctx.send("Users created")
            # elif len(arg_list) == 3:
            # elif len(arg_list) == 4:
            # else:

            await ctx.send("arg")
        else:
            await ctx.send("no arg")

def setup(bot):
    bot.add_cog(RegisterCog(bot))