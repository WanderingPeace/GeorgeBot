# This is the 4rd new engine I've made for this hecking bot
# ??? 4rd?
# Love you too robot
# Main credit belongs to me
# But also thanks Robb and Jerry
GeorgeVersion = "1.0.0 Syndicaction"

import os
import discord
from discord.ext import commands
import json
import datetime
import time
import random
print(f'Relevant files imported.')

# Loading the existence of the bot
bot = commands.Bot(command_prefix="gTest", description="This really doesn't tell you anything that interesting",
                   intents=discord.Intents.all())
print(f'Bot functionality has been loaded.')

# Redirect the director just for the lols
os.chdir(r'C:\Users\geolo\OneDrive\Documents\Server\WanderingDetente\testing')
print(f'OS Directory redirected.')

# Update the date
text = open("InterestDate.txt","w")
text.write(str(datetime.datetime.now()))

# Function Junction, what's your Confunction?
def AwardInterest(time):
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
text = open("InterestDate.txt","r")
closed_time=text.readline()
closed_time = datetime.datetime.strptime(closed_time, '%Y-%m-%d %H:%M:%S.%f')
opened_time=datetime.datetime.now()
timedifferenceinhours = (opened_time-closed_time).total_seconds()
AwardInterest(timedifferenceinhours)
print(f'The time has been checked.')

#Loading any command functionality
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
    channel = bot.get_channel(769104543224037376)
    embed = discord.Embed(
        colour=discord.Colour.gold())
    embed.set_author(name='GeorgeBot™ Case Archive Protocol')
    embed.add_field(name='Case 1', value='Boot Cycle is Complete (FnF5 Restart)')
    await channel.send(embed=embed)
    print(
        f'Case 1 Announced.\n'
        f'{discord.version_info}.'
    )
    game = discord.Game('with Humans')
    await bot.change_presence(activity=game)
    print(
        f'Presence announced.'
    )
    # These two print messages must be the last in the event on_ready
    print(
        f'Startup cycle complete.'
    )
    print(
        f'GeorgeBot™ Version: {GeorgeVersion}'
    )


# Love events
@bot.event
async def change_nick(member, nick):
    print(f'Editing {member.name}')
    if member.id == "461751763154763798":
        pass
    else:
        if len(nick) > 32:
            nick = nick.split("|", 1)[0]
        await member.edit(nick=nick)


@bot.event
async def on_invite_create(member):
    channel = bot.get_channel(769104543224037376)
    embed = discord.Embed(
        colour=discord.Colour.blurple())
    embed.set_author(name='GeorgeBot™ Case Archive Protocol')
    embed.add_field(name='Case 4', value='Server Invite Generated (Non-Terminal Invite Creation)')
    await channel.send(embed=embed)


@bot.event
async def on_invite_delete(member):
    channel = bot.get_channel(769104543224037376)
    embed = discord.Embed(
        colour=discord.Colour.blurple())
    embed.set_author(name='GeorgeBot™ Case Archive Protocol')
    embed.add_field(name='Case 5', value='Server Invite Deleted (Non-Terminal Invite Deletion)')
    await channel.send(embed=embed)


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(716251537298685992)
    welcomemessage = [
        f'Welcome to the server, {member.name}!',
        f'Enjoy your stay, {member.name}!',
        f'Welcome, {member.name}, to Chaos!',
        f'Have fun while you’re here, {member.name}! :]',
    ]
    await channel.send(f'{random.choice(welcomemessage)}')
    channel = bot.get_channel(769104543224037376)
    embed = discord.Embed(
        colour=discord.Colour.magenta())
    embed.set_author(name='GeorgeBot™ Case Archive Protocol')
    embed.add_field(name='Case 9',
                    value=f'Unexpected Member Pickup (New Member Detected),\nCase was successfully called by {member.name}')
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(716251537298685992)
    leftmessage = [
        f'Come back soon, {member.name}!',
        f'We hope to see you again, {member.name}!',
        f'Goodbye, {member.name}, enjoy your journey!',
        f'We’ll miss you, {member.name}! :[',
    ]
    await channel.send(f'{random.choice(leftmessage)}')
    channel = bot.get_channel(769104543224037376)
    embed = discord.Embed(
        colour=discord.Colour.magenta())
    embed.set_author(name='GeorgeBot™ Case Archive Protocol')
    embed.add_field(name='Case 8',
                    value=f'Member Acknowledgement Pickup Failed (Member Cannot be Found),\nCase was successfully called by {member.name}')
    await channel.send(embed=embed)


@bot.event
async def on_member_ban(guild, user):
    channel = bot.get_channel(769104543224037376)
    embed = discord.Embed(
        colour=discord.Colour.blurple())
    embed.set_author(name='GeorgeBot™ Case Archive Protocol')
    embed.add_field(name='Case 10',
                    value=f'Member Forcibly Removed (Ban Hammer Swung),\nCase was successfully executed upon {user.name} in server {guild.name}')
    await channel.send(embed=embed)


@bot.event
async def on_member_unban(guild, user):
    channel = bot.get_channel(769104543224037376)
    embed = discord.Embed(
        colour=discord.Colour.blurple())
    embed.set_author(name='GeorgeBot™ Case Archive Protocol')
    embed.add_field(name='Case 11',
                    value=f'Member Restriction Removed (Ban Hammer Unswung),\nCase was successfully executed upon {user.name} in server {guild.name}')
    await channel.send(embed=embed)


# Case commands
# We use the old style for case commands because wheeeeeeeeeeeeee and also correct distinction

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Case 0 Shutdown Cycle Complete (Command-Side Forced Close)
    if message.content == ('g@event 0'):
        print(message.author.id)
        if message.author.id == 461751763154763798:
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(0, 0, 0))
            embed.set_author(name='GeorgeBot™ Case Archive Protocol')
            embed.add_field(name='Case 0',
                            value=f'Shutdown Cycle Complete (Command-Side Forced Close),\nCase was successfully called by {message.author.name}')
            channel = bot.get_channel(769104543224037376)
            await channel.send(embed=embed)
            text = open("InterestDate.txt", "w")
            text.write(str(datetime.datetime.now()))
            time.sleep(1)
            await bot.close()
            print(f'Executive close was called by {message.author.name}')
        else:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 1013',
                            value='Unable to Comply (Command Entered with Insufficient Authorisation)')
            await message.channel.send(embed=embed)

    # Case 1 Boot Cycle is Complete (FnF5 Restart)
    if message.content == 'g@event 1':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 2 Successful Test of Functionality (Experimental Features Test)
    if message.content == 'g@event 2':
        if message.author.id == 461751763154763798:
            embed = discord.Embed(
                colour=discord.Colour.green())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 2', value='Successful Test of Functionality (Experimental Features Test)')
            await message.channel.send(embed=embed)
            channel = bot.get_channel(769104543224037376)
            embed = discord.Embed(
                colour=discord.Colour.green())
            embed.set_author(name='GeorgeBot™ Case Archive Protocol')
            embed.add_field(name='Case 2',
                            value=f'Successful Test of Functionality (Experimental Features Test),\nCase was successfully called by {message.author.name}')
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 1013',
                            value='Unable to Comply (Command Entered with Insufficient Authorisation)')
            await message.channel.send(embed=embed)

    # Case 3 Unable to Comply (Command Context is Invalid)
    if message.content == 'g@event 3':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 4 Server Invite Generated (Non-Terminal Invite Creation)
    if message.content == 'g@event 4':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 5 Server Invite Deleted (Non-Terminal Invite Deletion)
    if message.content == 'g@event 5':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 6 System-Side Profile Update (Picture Updated)
    if message.content == 'g@event 6':
        if message.author.id == 461751763154763798:
            channel = bot.get_channel(769104543224037376)
            embed = discord.Embed(
                colour=discord.Colour.dark_green())
            embed.set_author(name='GeorgeBot™ Case Archive Protocol')
            embed.add_field(name='Case 6',
                            value=f'System-Side Profile Update (Picture Updated),\nCase was successfully called by {message.author.name}')
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
            await message.channel.send(embed=embed)

    # Case 7 Insufficient Extension (Subcommand Invoked is None)
    if message.content == 'g@event 7':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 8 Member Acknowledgement Pickup Failed (Member Cannot be Found)
    if message.content == 'g@event 8':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 9 Unexpected Member Pickup (New Member Detected)
    if message.content == 'g@event 9':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 10 Member Forcibly Removed (Ban Hammer Swung)
    if message.content == 'g@event 10':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 11 Member Restriction Removed (Ban Hammer Unswung)
    if message.content == 'g@event 11':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 12 Minigame Functionality Restricted (Improper Context)
    if message.content == 'g@event 12':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 13 Command Withheld (Accessed Cog is Disabled)
    if message.content == 'g@event 13':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 14 Argument Error (Required Argument Missing)
    if message.content == 'g@event 14':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 15 Command Error (Request Command Inaccessible)
    if message.content == 'g@event 15':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 16 Command Error (Prerequisite Check Failure)
    if message.content == 'g@event 16':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 17 Value Error (Number Inputted is Unusable)
    if message.content == 'g@event 17':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 18 Command Error (Requested Action Failed Server-Side)
    if message.content == 'g@event 18':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 19 Minigame Error (Insufficient Arguments Inputted)
    if message.content == 'g@event 19':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 1011 Submarhrine Mode Activated (r:rhr)
    if message.content == 'g@event 1011':
        if message.author.id == 461751763154763798:
            embed = discord.Embed(
                colour=discord.Colour.green())
            embed.set_author(name='GeorhrgeBot™ Case Rhreturhrn Prhrotocol')
            embed.add_field(name='Case 1011', value='Submarhrine Mode Activated (r:rhr)')
            await message.channel.send(embed=embed)
            guild = discord.utils.get(bot.guilds, name="Cult of Chaos")
            members = guild.members
            for member in members:
                newnick = str(member.nick).replace("r", "rhr", 4)
                await change_nick(member, newnick)
            for member in members:
                newnick = str(member.nick).replace("R", "Rhr", 4)
                await change_nick(member, newnick)
            channel = bot.get_channel(769104543224037376)
            embed = discord.Embed(
                colour=discord.Colour.green())
            embed.set_author(name='GeorhrgeBot™ Case Arhrchive Prhrotocol')
            embed.add_field(name='Case 1011',
                            value=f'Submarhrine Mode Fully Activated (r:rhr),\nCase was successfully called by {message.author.name}')
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 1013',
                            value='Unable to Comply (Command Entered with Insufficient Authorisation)')
            await message.channel.send(embed=embed)

    # Case 1012 Submarine Mode Deactivated (rhr:r)
    if message.content == 'g@event 1012':
        if message.author.id == 461751763154763798:
            embed = discord.Embed(
                colour=discord.Colour.green())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 1012', value='Submarine Mode Deactivated (rhr:r)')
            await message.channel.send(embed=embed)
            guild = discord.utils.get(bot.guilds, name="Cult of Chaos")
            members = '\n - '.join([member.name for member in guild.members])
            print(f'Guild Members:\n - {members}')
            members = guild.members
            for member in members:
                newnick = str(member.nick).replace("rhr", "r", 4)
                await change_nick(member, newnick)
            for member in members:
                newnick = str(member.nick).replace("Rhr", "R", 4)
                await change_nick(member, newnick)
            channel = bot.get_channel(769104543224037376)
            embed = discord.Embed(
                colour=discord.Colour.green())
            embed.set_author(name='GeorgeBot™ Case Archive Protocol')
            embed.add_field(name='Case 1012',
                            value=f'Submarine Mode Fully Deactivated (rhr:r),\nCase was successfully called by {message.author.name}')
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 1013',
                            value='Unable to Comply (Command Entered with Insufficient Authorisation)')
            await message.channel.send(embed=embed)

    # Case 1013 Unable to Comply (Command Entered with Insufficient Authorisation)
    if message.content == 'g@event 1013':
        embed = discord.Embed(
            colour=discord.Colour.red())
        embed.set_author(name='GeorgeBot™ Case Return Protocol')
        embed.add_field(name='Case 3', value='Unable to Comply (Command Context is Invalid)')
        await message.channel.send(embed=embed)

    # Case 1014 Angry Mode Activated (George is in a Bad Mood)
    if message.content == 'g@event 1014':
        if message.author.id == 461751763154763798:
            embed = discord.Embed(
                colour=discord.Colour.dark_orange())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 1014', value='Angry Mode Activated (George is in a Bad Mood)')
            await message.channel.send(embed=embed)
            channel = bot.get_channel(769104543224037376)
            embed = discord.Embed(
                colour=discord.Colour.dark_orange())
            embed.set_author(name='GeorgeBot™ Case Archive Protocol')
            embed.add_field(name='Case 1014',
                            value=f'Angry Mode Activated (George is in a Bad Mood),\nCase was called by {message.author.name}')
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(
                colour=discord.Colour.red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 1013',
                            value='Unable to Comply (Command Entered with Insufficient Authorisation)')
            await message.channel.send(embed=embed)

        # This is necessary
    await bot.process_commands(message)

bot.run("NzI5MTYzMzIwMDc4MzY4Nzk5.XwE9Zg.Rr9f7TMjD-N7qM8XuW_Ra-2crSE")
