import discord
from discord.ext import commands
from discord.utils import get

class UtilityExamples(commands.Cog):
    """Provides basic utility commands"""
    def __init__(self, bot):
        self.bot = bot


    @group.command()
    async def get(self, ctx, member: discord.Member = None):
        """Gets a user's group"""
        member = member or ctx.author
        role = get(member.server.roles, name="Media")
        await bot.add_roles(member, role) 


def setup(bot):
    bot.add_cog(UtilityExamples(bot))
