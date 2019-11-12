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

    # Creates the default Profile embed
    def profile_help(self, ctx):
        embed = discord.Embed(title="Register your Profile", description="Create a Profile to identify yourself to other members using the following syntax:\n\n_* indicates an optional argument_\n```!register\n<name> i.e. Tom Smith\n<description> i.e. Software Developer\n<link> * i.e. https://www.github.com/TomSmith\n<htb> * Hack The Box User ID```",color=COLOR_INFO, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

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
            # Required arguments, full name and description
            if len(arg_list) == 2:
                name, role = arg_list
                profile, created = Users.objects.get_or_create(discord_id=ctx.message.author.id)
                if created:
                    profile.description = role
                    profile.full_name = name
                    profile.discord_tag = "{}#{}".format(ctx.message.author.name, ctx.message.author.discriminator)
                    profile.save()
                    await ctx.send(embed=self.successful_profile(ctx))
                    logger.warning("Profile created for %s", profile.discord_tag)
                else:
                    await ctx.send(embed=self.existing_profile(ctx))
            # Additional optional argument "Link"
            elif len(arg_list) == 3:
                name, role, link = arg_list
                profile, created = Users.objects.get_or_create(discord_id=ctx.message.author.id)
                if created:
                    profile.description = role
                    profile.full_name = name
                    profile.link = link
                    profile.discord_tag = "{}#{}".format(ctx.message.author.name, ctx.message.author.discriminator)
                    profile.save()
                    await ctx.send(embed=self.successful_profile(ctx))
                    logger.warning("Profile created for %s", profile.discord_tag)
                else:
                    profile.link = link
                    profile.save()
                    await ctx.send(embed=self.existing_profile(ctx))
            # Additional optional argument "Hack The Box ID"
            elif len(arg_list) == 4:
                name, role, link, htb = arg_list
                profile, created = Users.objects.get_or_create(discord_id=ctx.message.author.id)
                if created:
                    profile.description = role
                    profile.full_name = name
                    profile.link = link
                    profile.htb = htb
                    profile.discord_tag = "{}#{}".format(ctx.message.author.name, ctx.message.author.discriminator)
                    profile.save()
                    await ctx.send(embed=self.successful_profile(ctx))
                    logger.warning("Profile created for %s", profile.discord_tag)
                else:
                    profile.link = link
                    profile.htb = htb
                    profile.save()
                    await ctx.send(embed=self.existing_profile(ctx))
            else:
                await ctx.send(embed=self.profile_help(ctx))
        else:
            await ctx.send(embed=self.profile_help(ctx))

def setup(bot):
    bot.add_cog(RegisterCog(bot))