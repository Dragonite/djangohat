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

    # Successful profile creation embed
    def successful_profile(self, ctx):
        embed = discord.Embed(title="Profile successfully created!", description="View your profile using `!profile`.",color=COLOR_SUCCESS, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    # Profile already exists
    def existing_profile(self, ctx):
        embed = discord.Embed(title="Profile already exists!", description="View your profile using `!profile`.",color=COLOR_INFO, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    @commands.command()
    async def register(self, ctx, *, arg=None):
        if arg:
            arg_list = arg.split('\n')
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
                    await ctx.send(embed=self.successful_profile(ctx))
                    # Log newly created profile
                else:
                    await ctx.send(embed=self.existing_profile(ctx))
            # elif len(arg_list) == 3:
            # elif len(arg_list) == 4:
            # else:
        else:
            await ctx.send("no arg")

def setup(bot):
    bot.add_cog(RegisterCog(bot))