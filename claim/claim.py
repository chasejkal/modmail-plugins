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
        thread = await self.db.find_one({'thread_id': str(ctx.thread.channel.id)})
        if thread is None:
            await self.db.insert_one({'thread_id': str(ctx.thread.channel.id), 'claimers': [str(ctx.author.id)]})
            await ctx.channel.set_permissions(ctx.message.author, view_channel=True)
            await ctx.send(f'Thread claimed by {ctx.message.author}, use `;addstaff (userid)` if you require assistance from other staff members.')
            helper = discord.utils.get(ctx.guild.roles, name="Helper")
            mod = discord.utils.get(ctx.guild.roles, name="yo can i get mod?")
            await ctx.channel.set_permissions(helper, view_channel=False)
            await ctx.channel.set_permissions(mod, view_channel=False)
        else:
            await ctx.send('Thread is already claimed')

    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @checks.thread_only()
    @commands.command()
    async def addstaff(self, ctx, *, member: discord.Member):
        """Adds another user to the thread claimers"""
        thread = await self.db.find_one({'thread_id': str(ctx.thread.channel.id)})
        if thread and str(ctx.author.id) in thread['claimers']:
            await self.db.find_one_and_update({'thread_id': str(ctx.thread.channel.id)}, {'$addToSet': {'claimers': str(member.id)}})
            await ctx.channel.set_permissions(member, view_channel=True)
            await ctx.send(f'Added {member.mention}')

    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @checks.thread_only()
    @commands.command()
    async def removestaff(self, ctx, *, member: discord.Member):
        """Removes a user from the thread claimers"""
        thread = await self.db.find_one({'thread_id': str(ctx.thread.channel.id)})
        if thread and str(ctx.author.id) in thread['claimers']:
            await self.db.find_one_and_update({'thread_id': str(ctx.thread.channel.id)}, {'$pull': {'claimers': str(member.id)}})
            await ctx.channel.set_permissions(member, view_channel=False)
            await ctx.send(f'Removed {member.mention}')





def setup(bot):
    bot.add_cog(ClaimThread(bot))
