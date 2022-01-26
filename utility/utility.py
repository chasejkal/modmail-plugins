import discord
from discord.ext import commands
from discord.utils import get

class UtilityExamples(commands.Cog):
    """Provides basic utility commands"""
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)


    @group.command()
    async def get(self, ctx, member: discord.Member = None):
        """Gets a user's group"""
        member = member or ctx.author
        data = await self.db.find_one({'user_id': str(member.id)})
        role = get(member.server.roles, name="Media")
        await bot.add_roles(member, role) 


def setup(bot):
    bot.add_cog(UtilityExamples(bot))
