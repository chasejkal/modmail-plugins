from collections import defaultdict
from datetime import datetime

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel
from core.time import UserFriendlyTime


class TopSupporters(commands.Cog):
    """Sets up top supporters command in Modmail discord"""
    def __init__(self, bot):
        self.bot = bot

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    @commands.command()
    async def qp(self, ctx):
        await ctx.message.add_reaction()


def setup(bot):
    bot.add_cog(TopSupporters(bot))
