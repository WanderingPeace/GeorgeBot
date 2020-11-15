from discord.ext import commands
import discord
import sys
import traceback

bot = commands.Bot(command_prefix="gTest")


class General(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    async def rules(self, ctx):
        await ctx.send(file=discord.File('rules.pdf'))

    # This is the Error Handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on.error'):
            return
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        error = getattr(error, 'original', error)
        if isinstance(error, commands.DisabledCommand):
            embed = discord.Embed(
                colour=discord.Colour.dark_red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 13', value='Command Withheld (Accessed Cog is Disabled)')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                colour=discord.Colour.dark_red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 14', value='Argument Error (Required Argument Missing)')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                colour=discord.Colour.dark_red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 15', value='Command Error (Requested Command Not Found)')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 1013',
                            value='Unable to Comply (Command Entered with Insufficient Authorisation)')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                colour=discord.Colour.dark_red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 16', value='Command Error (Prerequisite Check Failure)')
            await ctx.send(embed=embed)
        elif isinstance(error, ValueError):
            embed = discord.Embed(
                colour=discord.Colour.dark_red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 17', value='Value Error (Number Inputted is Unusable)')
            await ctx.send(embed=embed)
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)



def setup(bot):
    bot.add_cog(General(bot))
