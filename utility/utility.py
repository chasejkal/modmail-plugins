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
    async def art(self, ctx):
        """Gets a user's group"""
        thread = ctx.thread
        if thread == None:
            member = ctx.author
        else:
            member = thread.recipient
        role = get(member.guild.roles, name="artists")
        e = discord.Embed(description="**Given artist role.**", color=0X00FF00)
        await ctx.send(embed=e)
        await member.add_roles(role) 
    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def userid(self, ctx):
        thread = ctx.thread
        if thread == None:
            await ctx.send("You have to use in a thread.")
        else:
            member = thread.recipient
        await ctx.send(f"{member.id}")


def setup(bot):
    bot.add_cog(UtilityExamples(bot))
