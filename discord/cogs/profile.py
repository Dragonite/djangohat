import discord
import logging
import datetime
from discord.ext import commands
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

    @commands.command()
    async def profile(self, ctx, *args):
        if args:
            print("args")
        else:
            try:
                profile = Users.objects.get(discord_id=ctx.message.author.id)
                await ctx.send(embed=self.existing_profile(ctx, profile))
            except Users.DoesNotExist:
                await ctx.send("no profile exists")


def setup(bot):
    bot.add_cog(ProfileCog(bot))