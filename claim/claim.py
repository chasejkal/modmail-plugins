import discord
from discord.ext import commands
from core import checks
from core.checks import PermissionLevel

class ClaimThread(commands.Cog):
    """Allows supporters to claim thread by sending claim in the thread channel"""

    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.plugin_db.get_partition(self)

    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @checks.thread_only()
    @commands.command()
    async def claim(self, ctx):
            await ctx.send('Claimed')
            new_name = f"{ctx.author.name}-{ctx.channel.name}"
            B = discord.utils.get(ctx.guild.channels, name="Claimed Tickets")
            await ctx.channel.edit(category=B)
            await ctx.channel.edit(name=new_name)

async def setup(bot):
    await bot.add_cog(ClaimThread(bot))
