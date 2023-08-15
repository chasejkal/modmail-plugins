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
        """Give a user the 'artists' role"""
        thread = ctx.thread
        if thread is None:
            await ctx.send("This command must be used in a thread.")
        else:
            member = thread.recipient
            role = get(member.guild.roles, name="artists")
            if role is None:
                await ctx.send("The 'artists' role does not exist on this server.")
            else:
                await member.add_roles(role)
                e = discord.Embed(description="**Given artist role.**", color=0X00FF00)
                await ctx.send(embed=e)

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def userid(self, ctx):
        """Get the user ID of the thread recipient"""
        thread = ctx.thread
        if thread is None:
            await ctx.send("This command must be used in a thread.")
        else:
            member = thread.recipient
            await ctx.send(f"User ID: {member.id}")

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def qv(self, ctx):
        """Generate a quick verify command for the user"""
        thread = ctx.thread
        if thread is None:
            await ctx.send("This command must be used in a thread.")
        else:
            member = thread.recipient
            await ctx.send(f">verify {member.id}")

def setup(bot):
    bot.add_cog(UtilityExamples(bot))
