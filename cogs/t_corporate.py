import discord
import json
from discord.ext import commands
import math
import datetime

bot = commands.Bot(command_prefix="gTest")


def is_channel(channel_id):
    def predicate(ctx):
        return ctx.message.channel.id == 769472678137692162

    return commands.check(predicate)


class Corporate(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @bot.group()
    async def corp(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 7', value='Insufficient Extension (Subcommand Invoked is None)')
            await ctx.send(embed=embed)
        updateInterest()

    @corp.command()
    @is_channel('CHANNEL_ID')
    async def daily(self, ctx):
        jsonload('cash.json')
        update_data(users, ctx.message.author.id, 'money')
        add_money(users, ctx.message.author.id, 200)
        jsondump('cash.json', users)
        check_balance(users, ctx.message.author.id, 'money')
        embed = discord.Embed(
            colour=discord.Colour.gold())
        embed.set_author(name='GeorgeBot™ Corporate Simulator')
        embed.add_field(name=f'{ctx.message.author.name}’s Account Balance',
                        value=f'Daily money added :)\nYou now have ${balance} in cash.')
        await ctx.send(embed=embed)
        updateInterest()

    @corp.command()
    async def wealthshare(self, ctx):
        jsonload('cash.json')
        update_data(users, ctx.message.author.id, 'money')
        money_share(users, ctx.message.author.id)
        embed = discord.Embed(
            colour=discord.Colour.gold())
        embed.set_author(name='GeorgeBot™ Corporate Simulator')
        embed.add_field(name=f'Wealth Share Calculator',
                        value=f'{ctx.message.author.name} owns {relative_wealth}% of the cash wealth of the economy.')
        await ctx.send(embed=embed)
        updateInterest()

    @corp.command()
    async def balance(self, ctx, target):
        jsonload(f'{target}.json')
        update_data(users, ctx.message.author.id, 'money')
        check_balance(users, ctx.message.author.id, 'money')
        embed = discord.Embed(
            colour=discord.Colour.gold())
        embed.set_author(name='GeorgeBot™ Corporate Simulator')
        embed.add_field(name=f'{ctx.message.author.name} Account Balances',
                        value=f'{ctx.message.author.name} has:\n ${balance} in {target}.')
        await ctx.send(embed=embed)
        updateInterest()

    @corp.command()
    async def admindaily(self, ctx):
        if ctx.message.author.id is not None:
            # CHANGE TO == 461751763154763798
            jsonload('cash.json')
            update_data(users, ctx.message.author.id, 'money')
            add_money(users, ctx.message.author.id, 200)
            jsondump('cash.json', users)
            check_balance(users, ctx.message.author.id, 'money')
            embed = discord.Embed(
                colour=discord.Colour.gold())
            embed.set_author(name='GeorgeBot™ Corporate Simulator')
            embed.add_field(name=f'{ctx.message.author.name}’s Account Balance',
                            value=f'Daily money added :)\nYou now have ${balance} in cash.')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 12', value='Minigame Functionality Restricted (Improper Context)')
            await ctx.send(embed=embed)
        updateInterest()

    @corp.command()
    async def accounts(self, ctx):
        await ctx.send(
            f'All users have two accounts:\nCash - The amount of money in your wallet.\nSavings - The amount of money in your savings account.\nDebt - The amount of debt you owe to the bank.')
        updateInterest()

    @corp.command()
    async def transfer(self, ctx, former, latter, amount):
        if int(amount) == 0:
            await ctx.send('You can’t transfer $0!')
        elif int(amount) < 0:
            await ctx.send('You can’t transfer negative money!')
        elif former == 'debt':
            await ctx.send('You cannot transfer from your debts!')
        elif latter == 'debt':
            await ctx.send(
                'You cannot transfer to your debts! If you wish to pay off a loan, use g!corp payoff *amount* :]')
        else:
            jsonload(f'{former}.json')
            update_data(users, ctx.message.author.id, 'money')
            sub_money(users, ctx.message.author.id, int(amount), 'money')
            if zero >= 0:
                jsondump(f'{former}.json', users)
                jsonload(f'{latter}.json')
                update_data(users, ctx.message.author.id, 'money')
                add_money(users, ctx.message.author.id, int(amount))
                jsondump(f'{latter}.json', users)
                embed = discord.Embed(
                    colour=discord.Colour.green())
                embed.set_author(name='GeorgeBot™ Corporate Simulator')
                embed.add_field(name=f'{ctx.message.author.name}’s Account',
                                value=f'Transfer successful :]')
                await ctx.send(embed=embed)
            else:
                jsonload(f'{former}.json')
                update_data(users, ctx.message.author.id, 'money')
                check_balance(users, ctx.message.author.id, 'money')
                embed = discord.Embed(
                    colour=discord.Colour.red())
                embed.set_author(name='GeorgeBot™ Corporate Simulator')
                embed.add_field(name=f'{ctx.message.author.name}’s Account',
                                value=f'Transfer unsuccessful :[\nYou only have ${balance}!')
                await ctx.send(embed=embed)
        updateInterest()

    @corp.command()
    async def loan(self, ctx, amount):
        if int(amount) == 0:
            await ctx.send('You can’t ask for a loan of $0!')
        elif int(amount) < 0:
            await ctx.send('You can’t ask for a negative loan!')
        else:
            jsonload('debt.json')
            update_data(users, ctx.message.author.id, 'money')
            add_money(users, ctx.message.author.id, int(amount))
            jsondump('debt.json', users)
            jsonload('cash.json')
            update_data(users, ctx.message.author.id, 'money')
            add_money(users, ctx.message.author.id, int(amount))
            jsondump('cash.json', users)
            await ctx.send('Loan granted :]')
        updateInterest()

    @corp.command()
    async def payoff(self, ctx, amount):
        if int(amount) == 0:
            await ctx.send('You can’t pay off $0!')
        elif int(amount) < 0:
            await ctx.send('You can’t pay off negative money!')
        else:
            jsonload('cash.json')
            update_data(users, ctx.message.author.id, 'money')
            sub_money(users, ctx.message.author.id, int(amount), 'money')
            if zero >= 0:
                jsonload('debt.json')
                sub_money(users, ctx.message.author.id, int(amount), 'money')
                if zero >= 0:
                    jsondump('debt.json', users)
                    jsonload('cash.json')
                    sub_money(users, ctx.message.author.id, int(amount), 'money')
                    jsondump('cash.json', users)
                    jsonload('debt.json')
                    check_balance(users, ctx.message.author.id, 'money')
                    embed = discord.Embed(
                        colour=discord.Colour.green())
                    embed.set_author(name='GeorgeBot™ Corporate Simulator')
                    embed.add_field(name=f'{ctx.message.author.name}’s Account',
                                    value=f'You have successfully paid off ${amount} :]\nYou have ${balance} left in debt.')
                    await ctx.send(embed=embed)
                else:
                    jsonload('debt.json')
                    update_data(users, ctx.message.author.id, 'money')
                    check_balance(users, ctx.message.author.id, 'money')
                    embed = discord.Embed(
                        colour=discord.Colour.red())
                    embed.set_author(name='GeorgeBot™ Corporate Simulator')
                    embed.add_field(name=f'{ctx.message.author.name}’s Account',
                                    value=f'Payoff unsuccessful :[\nYou only have ${balance} in debt!')
                    await ctx.send(embed=embed)
            else:
                jsonload('cash.json')
                update_data(users, ctx.message.author.id, 'money')
                check_balance(users, ctx.message.author.id, 'money')
                embed = discord.Embed(
                    colour=discord.Colour.red())
                embed.set_author(name='GeorgeBot™ Corporate Simulator')
                embed.add_field(name=f'{ctx.message.author.name}’s Account',
                                value=f'Payoff unsuccessful :[\nYou only have ${balance} in cash!')
                await ctx.send(embed=embed)
        updateInterest()


def setup(bot):
    bot.add_cog(Corporate(bot))


def jsonload(file):
    global users
    with open(file, 'r') as f:
        users = json.load(f)
    users = {int(user): traits for user, traits in users.items()}


def jsondump(file, thing):
    with open(file, 'w') as f:
        json.dump(thing, f)


def update_data(users, user, value):
    if not int(user) in users:
        users[user] = {}
        users[user][value] = 0


def add_money(users, user, money):
    users[user]['money'] += money


def sub_money(users, user, change, value):
    global zero
    users[user][value] -= change
    zero = users[user][value]
    return zero


def money_share(users, person):
    global relative_wealth
    total_money = 0
    for user, traits in users.items():
        user_money = traits['money']
        total_money += user_money
    relative_wealth = ((users[person]['money'] / total_money) * 100)
    relative_wealth = round_to_n(relative_wealth, (4))
    return relative_wealth


def check_balance(users, user, value):
    global balance
    balance = users[user][value]
    return balance


def round_to_n(x, n):
    if not x: return 0
    power = -int(math.floor(math.log10(abs(x)))) + (n - 1)
    factor = (10 ** power)
    return round(x * factor) / factor


def updateInterest():
    text = open("InterestDate.txt", "r")
    closed_time = text.readline()
    closed_time = datetime.datetime.strptime(closed_time, '%Y-%m-%d %H:%M:%S.%f')
    opened_time = datetime.datetime.now()
    time = (opened_time - closed_time).total_seconds()
    with open('savings.json', 'r') as f:
        users = json.load(f)
        for user in users:
            users[user]['money'] = int(users[user]['money']) + (
                int(users[user]['money'] * (0.0000004134399219235))) * time
        with open('savings.json', 'w') as f:
            json.dump(users, f)
    with open('debt.json', 'r') as f:
        users = json.load(f)
        for user in users:
            users[user]['money'] = int(users[user]['money']) + (
                int(users[user]['money'] * (0.00004134399219235))) * time
            with open('debt.json', 'w') as f:
                json.dump(users, f)
