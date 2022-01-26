import discord
from discord.ext import commands
from discord.utils import get

from core import checks
from core.models import PermissionLevel

class UtilityExamples(commands.Cog):
    """Provides basic utility commands"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def get(self, ctx, member: discord.Member = None):
        """Gets a user's group"""
        member = member or ctx.author
        role = get(member.guild.roles, name="Trusted")
        e = discord.Embed(description="**Given artist role.**", color=0X00FF00)
        await ctx.send(embed=em)
        await member.add_roles(role) 


def setup(bot):
    bot.add_cog(UtilityExamples(bot))
