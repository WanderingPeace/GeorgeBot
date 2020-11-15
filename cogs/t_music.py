import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="g!")


# For the KPop stans, me included :)

class Music(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @bot.group()
    async def kpop(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 7', value='Insufficient Extension (Subcommand Invoked is None)')
            await ctx.send(embed=embed)

    @kpop.command(aliases=['kpop bests'])
    async def picks(self, ctx):
        picks = [
            # Keep it in alphabetical order or else :)
            # Also you are obligated not to judge the volume of Stray Kids here; Will was here
            # Will, no you
            'https://youtu.be/vEwmc87yTpo',  # 3racha, Matryoshka
            'https://youtu.be/Vk4Md4K8xRg',  # 3racha, We Go
            'https://youtu.be/tf6a0XjexKw',  # 3racha, Wow
            'https://youtu.be/GebMoTIS_pg',  # Ateez, Answer
            'https://youtu.be/Dx_b25a__NY',  # Ateez, Inception
            'https://youtu.be/W6BP_q_wi7I',  # Ateez, Thanxx
            'https://youtu.be/KhZ5DCd7m6s',  # BTS, Dynamite
            'https://youtu.be/aMPZN3hv0qg',  # BTS, Savage Love feat. Jason Derulo
            'https://youtu.be/g2X2LdJAIpU',  # Day6, Shoot Me
            'https://youtu.be/MjTLxf1SN1c',  # NCT127, Kick It
            'https://youtu.be/jE-cjjbKXgI',  # NCT127, Regular English Version
            'https://youtu.be/tyrVtwE8Gv0',  # NCT U, Make a Wish
            'https://youtu.be/N5qWjQ9j6l0',  # WayV, Love Talk
            'https://youtu.be/3QfXK3t8wuc',  # Stray Kids, Airplane
            'https://youtu.be/dIpDHCH5opM',  # Stray Kids, Any
            'https://youtu.be/ZnpEBYvgiAU',  # Stray Kids, Astronaut
            'https://youtu.be/ECtRFjD7BCA',  # Stray Kids, B Me
            'https://youtu.be/cPwzLzy97L8',  # Stray Kids, Back Door
            'https://youtu.be/x8PkgClZVVM',  # Stray Kids, Easy
            'https://youtu.be/Pb6C8DWyqmM',  # Stray Kids, Haven
            'https://youtu.be/4YS9fGu5nEg',  # Stray Kids, Mixtape: Gone Days
            'https://youtu.be/pweS9VbaTk4',  # Stray Kids, My Universe
            'https://youtu.be/F-AZwNRRRWw',  # Stray Kids, Pacemaker
            'https://youtu.be/G28O89j3SqI',  # Stray Kids, Phobia
            'https://youtu.be/90qS-h-oxRo',  # Stray Kids, Slump English Version
            'https://youtu.be/7SPnJMGB9u4',  # Stray Kids, Slump Japanese Version
            'https://youtu.be/vWzo_QjJoLQ',  # Stray Kids, Slump Korean Version
            'https://youtu.be/ku8zU4fRA1s',  # Stray Kids, Sunshine
            'https://youtu.be/0RNL1oQrUYY',  # Stray Kids, The Tortoise and the Hare
            'https://youtu.be/o7lqCcE4Lho',  # Stray Kids, Top Japanese Version
            'https://youtu.be/mQXv864OnXc',  # Stray Kids, Wow
            'https://youtu.be/OyrK9AH0Y5A',  # TXT, Can't You See Me?
            'https://youtu.be/sB2YVGPPXW0',  # WayV, Bad Alive
            'https://youtu.be/UZayJwapb-Q',  # WayV, Turn Back Time
        ]
        await ctx.send(f'{random.choice(picks)}')

    @bot.group()
    async def gameost(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 7', value='Insufficient Extension (Subcommand Invoked is None)')
            await ctx.send(embed=embed)

    @gameost.command()
    async def picks(self, ctx):
        picks = [
            # Keep it in alphabetical order or else :)
            'https://youtu.be/eTWWk8zpA2o',  # Dead Cells, Collector
            'https://youtu.be/-yRz7bS2VLM',  # Dead Cells, Pan Master Slash
            'https://youtu.be/rGWFMBugG2I',  # Galaxy on Fire 2, Sounds of Space
            'https://youtu.be/ibUOxEBxVsE',  # Minecraft, Subwoofer Lullaby
            'https://youtu.be/_3ngiSxVCBs',  # Minecraft, Sweden
            'https://youtu.be/PCkYR5nErXU',  # Plants vs Zombies, Moongrains
            'https://youtu.be/5FnNatcOdIo',  # Stellaris, Hidden Motives
        ]
        await ctx.send(f'{random.choice(picks)}')

    @bot.group()
    async def movieost(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 7', value='Insufficient Extension (Subcommand Invoked is None)')
            await ctx.send(embed=embed)

    @movieost.command()
    async def picks(self, ctx):
        picks = [
            # Keep it in alphabetical order or else :)
            'https://youtu.be/Qemb3iBlp1o',  # Rogue One: A Star Wars Story, Your Father Would Be Proud
        ]
        await ctx.send(f'{random.choice(picks)}')

    @bot.command()
    async def calm(self, ctx):
        picks = [
            # Keep it in alphabetical order or else :)
            'https://youtu.be/rGWFMBugG2I',  # Galaxy on Fire 2, Sounds of Space
            'https://youtu.be/ibUOxEBxVsE',  # Minecraft, Subwoofer Lullaby
            'https://youtu.be/_3ngiSxVCBs',  # Minecraft, Sweden
            'https://youtu.be/PCkYR5nErXU',  # Plants vs Zombies, Moongrains
        ]
        await ctx.send(f'{random.choice(picks)}')

def setup(bot):
    bot.add_cog(Music(bot))
