import discord
import django
from discord.ext import commands
from users.models import *

class LinkCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def key(self, ctx, arg=None):
        if ctx.channel.type == discord.ChannelType.private and ctx.author != self.bot.user:
            profile = Users.objects.get(discord_id=ctx.message.author.id)
            if profile:
                if profile.site_key == arg:
                    profile.site_verified = True
                    profile.save()
                    print("Discord Profile Link for {} established.".format(profile.discord_tag))
            await ctx.send(arg)

def setup(bot):
    bot.add_cog(LinkCog(bot))