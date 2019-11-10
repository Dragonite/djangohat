import discord
import logging
import datetime
from discord.ext import commands
from users.models import *
from utils.lib import *

logger = logging.getLogger()

class LinkCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def key_success(self):
        embed = discord.Embed(title='Discord Profile Link Successful!',
                              description='Your Discord Profile was successfully linked to the website!',
                              color=COLOR_SUCCESS, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    def key_failure(self):
        embed = discord.Embed(title='Discord Profile Link Failed!',
                              description='Your key is incorrect!',
                              color=COLOR_DANGER, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    def key_claimed(self):
        embed = discord.Embed(title='Discord Profile Link already exists!',
                              description='This profile has already been verified.',
                              color=COLOR_INFO, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    @commands.command()
    async def key(self, ctx, arg=None):
        if ctx.channel.type == discord.ChannelType.private and ctx.author != self.bot.user:
            profile = Users.objects.get(discord_id=ctx.message.author.id)
            if profile:
                if profile.site_verified:
                    await ctx.send(embed=self.key_claimed())
                else:
                    if profile.site_key == arg:
                        profile.site_verified = True
                        profile.save()
                        await ctx.send(embed=self.key_success())
                        print("{}'s key has successfully been verified.".format(profile.discord_tag))
                        logger.warning("%s's key has successfully been verified", profile.discord_tag)
                    else:
                        await ctx.send(embed=self.key_failure())

def setup(bot):
    bot.add_cog(LinkCog(bot))