# This is the testing engine for GeorgeBot™
import os
import discord
from discord.ext import commands
import json
import datetime
import time

print(f'Relevant files imported.')

GeorgeVersion = "1.0.0 Syndicaction"

bot = commands.Bot(command_prefix="gTest", description="This really doesn't tell you anything that interesting",
                   intents=discord.Intents.all())
print(f'Bot functionality has been loaded.')

os.chdir(r'C:\Users\geolo\OneDrive\Documents\Server\WanderingDetente\testing')
print(f'OS Directory redirected.')

text = open("InterestDate.txt", "w")
text.write(str(datetime.datetime.now()))


# Function Junction, what's your Confunction?
def awardInterest(time):
    with open('savings.json', 'r') as f:
        users = json.load(f)
        for user in users:
            users[user]['money'] = int(users[user]['money']) + (int(users[user]['money'] * (0.0004134399219235))) * time
        with open('savings.json', 'w') as f:
            json.dump(users, f)
    with open('debt.json', 'r') as f:
        users = json.load(f)
        for user in users:
            users[user]['money'] = int(users[user]['money']) + (int(users[user]['money'] * (0.00004134399219235))) * time
            with open('debt.json', 'w') as f:
                json.dump(users, f)


# Time to get a watch
text = open("InterestDate.txt", "r")
closed_time = text.readline()
closed_time = datetime.datetime.strptime(closed_time, '%Y-%m-%d %H:%M:%S.%f')
opened_time = datetime.datetime.now()
timedifferenceinhours = (opened_time - closed_time).total_seconds()
awardInterest(timedifferenceinhours)
print(f'The time has been checked.')

# Loading any command functionality
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "_init_.py":
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Cogs loaded successfully.')


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    print(
        f'Launch information declared.\n'
        f'{discord.version_info}.'
    )
    game = discord.Game('1.0.0 Syndication')
    await bot.change_presence(activity=game)
    print(
        f'Presence announced.\n'
        f'Startup cycle complete.\n'
        f'Running GeorgeBot™ Version: {GeorgeVersion}'
    )

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Case 0 Shutdown Cycle Complete (Command-Side Forced Close)
    if message.content == ('gTevent 0'):
        print(message.author.id)
        if message.author.id == 461751763154763798:
            text = open("InterestDate.txt", "w")
            text.write(str(datetime.datetime.now()))
            time.sleep(1)
            message.channel.send('Shutting down :]')
            await bot.close()
            print(f'Executive close was called by {message.author.name}')
        else:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 1013',
                            value='Unable to Comply (Command Entered with Insufficient Authorisation)')
            await message.channel.send(embed=embed)

    await bot.process_commands(message)


bot.run("TOKEN")
