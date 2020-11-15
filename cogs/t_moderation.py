import discord
from discord.ext import commands
from .utils import checks

bot = commands.Bot(command_prefix="gTest")


class Moderation(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    @checks.has_permissions(manage_messages=True)
    async def cleanse(self, ctx, *args, mentions=None):
        deleted = []
        try:
            count = int(next(iter(args or []), 'fugg'))
        except ValueError:
            count = 100
        mentions = ctx.message.mentions
        await ctx.message.delete()
        if mentions:
            for user in mentions:
                try:
                    deleted += await ctx.channel.cleanse(limit=count, check=lambda x: x.author == user)
                except discord.Forbidden as e:
                    embed = discord.Embed(
                        colour=discord.Colour.dark_red())
                    embed.set_author(name='GeorgeBot™ Case Return Protocol')
                    embed.add_field(name='Case 18', value='Command Error (Requested Action Failed Server-Side)')
                    return await ctx.send(embed=embed)
        else:
            try:
                deleted += await ctx.channel.purge(limit=count)
            except discord.Forbidden:
                embed = discord.Embed(
                    colour=discord.Colour.dark_red())
                embed.set_author(name='GeorgeBot™ Case Return Protocol')
                embed.add_field(name='Case 18', value='Command Error (Requested Action Failed Server-Side)')
                return await ctx.send(embed=embed)

    @commands.group()
    async def perms(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 7', value='Insufficient Extension (Subcommand Invoked is None)')
            await ctx.send(embed=embed)

    @perms.command()
    @checks.has_permissions(manage_channels=True)
    async def add(self, ctx, user, channel):
        try:
            await channel.set_permissions(user, read_messages=True)
        except Exception:
            embed = discord.Embed(
                colour=discord.Colour.dark_red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 18', value='Command Error (Requested Action Failed Server-Side)')
            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
