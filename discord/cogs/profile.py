import discord
import logging
import datetime
from discord.ext import commands
from django.db.models import Q
from users.models import *
from utils.lib import *

logger = logging.getLogger()

class ProfileCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def existing_profile(self, ctx, profile):
        embed = discord.Embed(title=profile.full_name, description=profile.description,color=COLOR_INFO)
        embed.add_field(name="Discord Tag", value=profile.discord_tag, inline=False)
        if profile.link:
            embed.add_field(name="Link", value=profile.link, inline=False)
        if profile.htb:
            embed.set_image(url=profile.get_htb_url())
        embed.set_footer(text=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        return embed

    def missing_profile(self, ctx):
        embed = discord.Embed(title="No profile exists.", description="Create your profile using `!register`.",color=COLOR_INFO, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    @commands.command()
    async def profile(self, ctx, *args):
        if args:
            # Handle searches, should regex for an @, their tag and their discord ID.
            for arg in args:
                await ctx.send(arg)
                print(arg)
            print("args")
        else:
            try:
                profile = Users.objects.get(discord_id=ctx.message.author.id)
                await ctx.send(embed=self.existing_profile(ctx, profile))
            except Users.DoesNotExist:
                await ctx.send(embed=self.missing_profile(ctx))


def setup(bot):
    bot.add_cog(ProfileCog(bot))