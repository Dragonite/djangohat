import datetime
import logging

from discord.ext import commands

import discord
from users.models import *
from utils.lib import *

logger = logging.getLogger()


class ProfileCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def existing_profile(self, ctx, profile):
        discord_user = ctx.guild.get_member(int(profile.discord_id))
        embed = discord.Embed(title=profile.full_name, description=profile.description, color=COLOR_INFO)
        embed.add_field(name="Discord Tag", value=profile.discord_tag, inline=False)
        if profile.link:
            embed.add_field(name="Link", value=profile.link, inline=False)
        if profile.htb:
            embed.set_image(url=profile.get_htb_url())
        embed.set_footer(text=discord_user.display_name, icon_url=discord_user.avatar_url)
        return embed

    def missing_profile(self, ctx):
        embed = discord.Embed(title="No profile exists.", description="Create your profile using `!register`.",
                              color=COLOR_INFO, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    def other_missing_profile(self, ctx):
        embed = discord.Embed(title="No profile exists.", color=COLOR_INFO, timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    def successful_deleted_profile(self, ctx):
        embed = discord.Embed(title="Profile successfully deleted!", color=COLOR_SUCCESS,
                              timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    def lack_of_permissions(self, ctx):
        embed = discord.Embed(title="Only administrators can delete profiles!", color=COLOR_DANGER,
                              timestamp=datetime.datetime.now())
        embed.set_footer(text="{} {}".format(CLUB_NAME, CURRENT_YEAR), icon_url=self.bot.user.avatar_url)
        return embed

    @commands.command()
    async def profile(self, ctx, q=None, c=None):
        if q:
            # Handles nicknames that generate an additional !
            if q.startswith("<@!") and q.endswith(">"):
                arg_first = q.replace("!", "")
            else:
                arg_first = q
            # Handles an @ as a search
            if arg_first.startswith("<@") and arg_first.endswith(">"):
                query = arg_first[2:-1]
                try:
                    query = int(query)
                    profile = Users.objects.filter(discord_id=query).first()
                    if profile:
                        if c == 'delete':
                            if ctx.message.author.guild_permissions.administrator:
                                logger.warning("{} profile deleted by {}".format(profile.discord_tag,
                                                                                 ctx.message.author.display_name))
                                profile.delete()
                                await ctx.send(embed=self.successful_deleted_profile(ctx))
                            else:
                                await ctx.send(embed=self.lack_of_permissions(ctx))
                        else:
                            await ctx.send(embed=self.existing_profile(ctx, profile))
                    else:
                        await ctx.send(embed=self.other_missing_profile(ctx))
                except Exception:
                    await ctx.send(embed=self.other_missing_profile(ctx))
            # Search by tag contents
            else:
                profile = Users.objects.filter(discord_tag__icontains=arg_first).first()
                if profile:
                    if c == 'delete':
                        if ctx.message.author.guild_permissions.administrator:
                            logger.warning(
                                "{} profile deleted by {}".format(profile.discord_tag, ctx.message.author.display_name))
                            profile.delete()
                            await ctx.send(embed=self.successful_deleted_profile(ctx))
                        else:
                            await ctx.send(embed=self.lack_of_permissions(ctx))
                    else:
                        await ctx.send(embed=self.existing_profile(ctx, profile))
                else:
                    await ctx.send(embed=self.other_missing_profile(ctx))
        else:
            try:
                profile = Users.objects.get(discord_id=ctx.message.author.id)
                await ctx.send(embed=self.existing_profile(ctx, profile))
            except Users.DoesNotExist:
                await ctx.send(embed=self.missing_profile(ctx))


def setup(bot):
    bot.add_cog(ProfileCog(bot))
