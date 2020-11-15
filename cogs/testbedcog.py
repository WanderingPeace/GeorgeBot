from discord.ext import commands

bot = commands.Bot(command_prefix="gTest")


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def print(self, ctx, printer):
        print(printer)
        await ctx.send(f'{printer}')


def setup(bot):
    bot.add_cog(Test(bot))
