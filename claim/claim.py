
import discord
from discord.ext import commands

from core import checks
from core.checks import PermissionLevel


class ClaimThread(commands.Cog):
    """Allows supporters to claim thread by sending claim in the thread channel"""
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.plugin_db.get_partition(self)
        check_reply.fail_msg = 'This thread has been claimed by another user.'
        self.bot.get_command('reply').add_check(check_reply)
        self.bot.get_command('areply').add_check(check_reply)
        self.bot.get_command('fareply').add_check(check_reply)
        self.bot.get_command('freply').add_check(check_reply)

    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @checks.thread_only()
    @commands.command()
    async def claim(self, ctx):
        thread = await self.db.find_one({'thread_id': str(ctx.thread.channel.id)})
        if thread is None:
            await ctx.send(f'Thread claimed by {ctx.message.author}, use `;adduser (userid)`  if you require assistance from other staff members.')
            helper = discord.utils.get(ctx.guild.roles, name="Helper")
            mod = discord.utils.get(ctx.guild.roles, name="yo can i get mod?")
            await ctx.channel.set_permissions(helper, view_channel=False)
            await ctx.channel.set_permissions(mod, view_channel=False)
            await ctx.channel.set_permissions(ctx.message.author, view_channel=True)

    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @checks.thread_only()
    @commands.command()
    async def addclaim(self, ctx, *, member: discord.Member):
        """Adds another user to the thread claimers"""
        thread = await self.db.find_one({'thread_id': str(ctx.thread.channel.id)})
        if thread and str(ctx.author.id) in thread['claimers']:
            await ctx.channel.set_permissions(member, view_channel=True)
            await ctx.send(f'Added {member.mention} to the channel.')





def setup(bot):
    bot.add_cog(ClaimThread(bot))
