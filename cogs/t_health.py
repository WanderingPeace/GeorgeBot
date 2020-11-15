import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix="gTest")

class Health(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.group()
    async def health(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 7', value='Insufficient Extension (Subcommand Invoked is None)')
            await ctx.send(embed=embed)

    @health.command()
    async def compounds(self, ctx, thing):
        fileload("aminoacids.json")
        loaddata(f"{thing}", "info")
        if data == False:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 7', value='Insufficient Extension (Subcommand Invoked is None) (Make sure you correctly capitalise the compound you are looking for)')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                colour=discord.Colour.blue())
            embed.set_author(name='GeorgeBot™ Healthy Living Database')
            embed.add_field(name=f"{thing}", value=f'{contents}')
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Health(bot))


def fileload(file):
    global data
    data = False
    with open(f'health_database/{file}', 'r') as f:
        data = json.load(f)
        return data

def loaddata(locale, value):
    global contents
    contents = data[locale][value]
    return contents

