import random
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="gTest")


class Minigames(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx):
        eightball = [
            'As I see it, *yes*',
            'Ask again later, {0.author.name}'.format(ctx),
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            "Don't count on it",
            'It is *certain*, {0.author.name}'.format(ctx),
            'It is decidedly so',
            'Most likely, {0.author.name}'.format(ctx),
            'My reply is *no*, {0.author.name}'.format(ctx),
            'My sources say *no*, {0.author.name}, not at all'.format(ctx),
            'Outlook not so good',
            'Outlook good, {0.author.name}'.format(ctx),
            'Reply hazy, try again',
            'Signs point to *yes*',
            'Very doubtful, {0.author.name}'.format(ctx),
            'Without a doubt',
            'Yes, {0.author.name}'.format(ctx),
            'Yes, *definitely*',
            'You may rely on it',
        ]
        await ctx.send(f'{random.choice(eightball)}')

    @commands.command()
    async def quotes(self, ctx):
        # I do be defining quotes doe
        quotes = [
            '"Progress is progress" - George Love, Good Advice in General',
            '"This is a placeholder while I find some quotes to stick in here. Please wait." - GeorgeBot™, General.py',
            '"Yes" - Protegent Antivirus',
            '"Hard times make strong people. Strong people make good times. Good times make weak people, and weak people make hard times." - G. Michael Hopf, Those Who Remain',
            '"If you can’t win here, go win somewhere that you can, and hope that the victories count the same." - George Love, Good Advice in General',
            '"Appear weak when you are strong, and strong when you are weak." - Sun Tzu, Art of War',
            '"If you know your enemy, and know yourself, you need not fear the outcome of a hundred battles." - Sun Tzu, Art of War',
            '"Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt." - Sun Tzu, Art of War',
            '"In the midst of chaos, there is also opportunity." - Sun Tzu, Art of War',
            '"Even the finest sword plunged into salt water will rust." - Sun Tzu, Art of War',
            '"So it begins." - Théoden son of Thengel, Lord of the Rings: the Two Towers',
            '"It’s the job thats never started as takes longest to finish." - Samwise Gamgee, The Lord of the Rings',
            '"It is useless to meet revenge with revenge; it will heal nothing." - Frodo Baggins, The Lord of the Rings',
            '"Deeds are not less valiant because they are unpraised." - Aragorn, The Lord of the Rings',
            '"A hunted man sometimes wearies distrust and longs for friendship." - Aragorn, The Lord of the Rings',
            '"Such is oft the course of deeds that move the wheels of the world: small hands do them because they must, while the eyes of the great are elsewhere." - Elrond, The Lord of the Rings'
            '"Ayyy that’s hella sus bro" - Byju Thomas',
            '"ちょっと怪しいですね" - George Love',
            '"All we have to do is decide what to do with the time that is left to us." - Gandalf, The Lord of the Rings',
            '"Many are the strange chances of the worlds, and help shall oft come from the weak when the wise falter." - Gandalf, The Lord of the Rings',
            '"The burned hand teaches best. That advice about fire goes straight to the heart." - Gandalf, The Lord of the Rings',
            '"Faithless is he that says farewell when the road darkens." - Gimli, The Lord of the Rings',
            '"Who knows? Have patience. Go where you must go, and hope!" - Gandalf, The Lord of the Rings',
            '"It is not despair, for despair is only for those who see the end beyond all doubt. We do not!" - Gandalf, The Lord of the Rings',
            '"Maybe the paths you each shall tread are already laid before your feet, though you do not see them." - Galadriel, The Lord of the Rings',
            '"If more of us valued food and cheer and song above hoarded gold, it would be a merrier world." - Thorin Oakenshield, The Hobbit',
            '"But in the end it’s only a passing thing, this shadow; even darkness must pass." - Samwise Gamgee, The Lord of the Rings',
            '"The world is indeed full of peril, and in it there are many dark places; but there is still much that is fair, and though in all lands love is now mingled with grief, it grows perhaps the greater." - Haldir, The Lord of the Rings',
            '"It is not the strength of the body but the strength of the spirit." - J.R.R. Tolkien',
            '"It is not our part to master the tides of the world, but to do what is in us for the succor of those years wherein we are set, uprooting the evil in the fields that we know, so that those who live after may have clean earth to till. What weather they may have is not ours to rule." - Gandalf, The Lord of the Rings',
            '"What will happen? There is only one way of finding out." - Aslan, The Chronicles of Narnia',
            '"What would have happened? Nobody is ever told that." - Aslan, The Chronicles of Narnia',
            '"Courage, dear heart." - Aslan, The Chronicles of Narnia',
            '"In accepting the inevitable, one finds peace." - Tuvok, Star Trek: Voyager',
            '"What is, is." - Margaret Bonanno, Dwellers in the Crucible',
            '"Doubt is the beginning, not the end of wisdom." - George Illes',
            '"After a time, you may find that having is not so pleasing a thing as wanting after all. It is not logical, but it is often true." - Spock, Star Trek: The Original Series',
            '"Nothing unreal exists." - Spock, Star Trek IV: The Voyage Home',
            '"Challenge your preconceptions, or they will challenge you." - Unknown',
            '"Nothing that is, is unimportant." - Margaret Bonanno, Strangers From the Sky',
            '"We make mistakes, but we’re human - and maybe that’s the word that best explains us." - James T. Kirk, Star Trek: The Original Series',
            '"I am pleased to see that we have differences. May we together become greater than the sum of both of us." - Surak, Star Trek: The Original Series',
            '"It is possible to commit no errors and still lose. That is not a weakness. That is life." - Jean-Luc Picard, Star Trek: The Next Generation',
            '"Yesterday is history, tomorrow is a mystery, but today is a gift. That is why it is called the present." - Master Oogway, Kung Fu Panda',
            '"You can use logic to justify almost anything. That is its power. And its flaw." - Kathryn Janeway, Star Trek: Voyager',
            '"There is a way out of every box, a solution to every puzzle; it’s just a matter of finding it." - Jean-Luc Picard, Star Trek: The Next Generation',
            '"One often meets his destiny on the road he takes to avoid it." - Master Oogway, Kung Fu Panda',
            '"Running may help for a little while, but sooner or later the pain catches up with you. And the only way to get rid of it is to stand your ground and face it." - Benjamin Sisko, Star Trek: Deep Space Nine',
            '"I’d want to poke my head up once in a while and take a look around, see what’s going on. It’s life! You can miss it if you don’t open your eyes." - Benjamin Sisko, Star Trek: Deep Space Nine',
            '"You win some, you lose some. I always had problems with the ’lose some’ part of that." - Benjamin Sisko, Star Trek: Deep Space Nine',
            '"Even in the darkest moments, you can always find something that will make you smile." - Benjamin Sisko, Star Trek: Deep Space Nine',
            '"There is only one thing I want from you. Find something you love, then do it the best you can." - Benjamin Sisko, Star Trek: Deep Space Nine',
            '"I have fought the good fight. I have finished the course. I have kept the faith." - 2 Timothy 4:7, the Bible',
            '"It doesn’t matter what you’re made of. What matters is who you are." - Chakotay, Star Trek: Voyager',
            '"You can’t go through life trying to avoid getting a broken heart. If you do, it’ll break from loneliness anyway." - Julian Bashir, Star Trek: Deep Space Nine',
            '"The universe is a sphereoid region 705 metres in diameter." - Computer, Star Trek: The Next Generation',
            '"Through joining, they have been healed. Grief has been transmuted to joy. Loneliness to belonging." - Data, Star Trek: The Next Generation',
            '"I would gladly risk feeling bad at times, if it also meant I could taste my dessert." - Data, Star Trek: The Next Generation',
            '"Bad manners are the fault of the parent, not the child." - Gul Dukat, Star Trek: Deep Space Nine',
            '"Ah, an open mind! The essence of intellect!" - Elim Garak, Star Trek: Deep Space Nine',
            '"I believe in coincidences. Coincidences happen every day. But I don’t trust coincidences." - Elim Garak, Star Trek: Deep Space Nine',
            '"Well, the truth is usually just an excuse for a lack of imagination." - Elim Garak, Star Trek: Deep Space Nine',
            '"I’d like to think so, but one can never say. We live in uncertain times." - Elim Garak, Star Trek: Deep Space Nine',
            '"You can’t just walk away from your responsibilities because you made a mistake." - Kathryn Janeway, Star Trek: Voyager',
            '"It’s never easy, but if we turn our backs on our principles, we stop being human." - Kathryn Janeway, Star Trek: Voyager',
            '"We all have scars, of one kind or another." - Kira Nerys, Star Trek: Deep Space Nine',
            '"The best way to survive a knife fight is never to get in one." - Kira Nerys, Star Trek: Deep Space Nine',
            '"What can I say? To us it’s a slime pit, but to them it’s a home." - Geordi La Forge, Star Trek: The Next Generation',
            '"I tell you, war is much more fun when you’re winning!" - Martok, Star Trek: Deep Space Nine',
            '"Irrationality is the spice of life." - Aleksei Solntsev',
            '"We are not accorded the luxury of who we fall in love with. Do you think Sirella is anything like the woman I thought I’d marry? She is a prideful, arrogant, mercurial woman who shares my bed far too infrequently for my taste. And yet, I love her deeply." - Martok, Star Trek: Deep Space Nine',
            '"Some spice is a good thing. Too much becomes unbearable. The same goes for life. And salt." - George Love, Good Advice in General',
            '"I’ve hated his name for almost thirty years. I’ve dreamt of the moment when I would finally see him stripped of his rank and title, when he would suddenly find himself without a friend in the world, without the power of his birthright. Well, I’ve had that moment now. And I took no joy from it." - Martok, Star Trek: Deep Space Nine',
            '"You know the old saying, a man who is always looking over his shuolder is waiting for trouble to find him." - Miles O’Brien, Star Trek: Deep Space Nine',
            '"We’ve grown apart, the lot of us. We didn’t mean for it to happen but it did. Life has changed us, pulled us apart. Lisa Cusak was my friend. But you are also my friends, and I want friends in my life. Because one day we’re going to wake up and discover that someone is missing from this friendship circle, and on that day we’re going to mourn. And we shouldn’t have to mourn alone." - Miles O’Brien, Star Trek: Deep Space Nine',
            '"I’ll never understand this obsession with accumulating material wealth. You spend your entire life plotting and scheming to acquire more and more possessions, until your living areas are bursting with useless junk. Then you die, your relatives sell everything, and start the cycle all over again." - Odo, Star Trek: Deep Space Nine',
            '"There is no profit in kindness." - Quark, Star Trek: Deep Space Nine',
            '"Too many people dream of places they’ll never go, wish for things they’ll never have, instead of paying adequate attention to their real lives." - Odo, Star Trek: Deep Space Nine',
            '"It has been my observation that one of the prices of giving people freedom of choice is that sometimes they make the wrong choice." - Odo, Star Trek: Deep Space Nine',
            '"There can be no justice so long as laws are absolute. Even life itself is an exercise in exceptions." - Jean-Luc Picard, Star Trek: The Next Generation',
            '"Let the dead rest, and the past remain the past." - Jean-Luc Picard, Star Trek: The Next Generation',
            '"The claim ’I was only following orders’ has been used to justify too many tragedies in our history." - Jean-Luc Picard, Star Trek: The Next Generation',
            '"Every once in a while, declare peace. It confuses the hell out of your enemies." - Quark, Star Trek: Deep Space Nine',
            '"One day I decided I would collate a list of quotes. Did anyone ever use my list of quotes? No, not really, but I learnt a lot; about people, about the universe, and about me. I do not regret any of it. It may be a failure, but it was a worthwhile one." - George Love, Good Advice in General',
            '"If you drop a hammer on your foot, it’s hardly useful to get mad at the hammer." - William Riker, Star Trek: The Next Generation',
            '"If you can’t take a little bloody nose, maybe you ought to go back home and crawl under your bed. It’s not safe out here. It’s wondrous, with treasures to satiate desires both subtles and gross... but it’s not for the timid." - Q, Star Trek: Deep Space Nine',
            '"You are erratic. Conflicted. Disorganised. Every decision is debated, every action questioned, every individual entitled to their own small opinion. You lack harmony, cohesion, greatness. It will be your undoing." - Seven of Nine, Star Trek: Voyager',
            '"Physiologically, love bears a striking similarity to disease. A series of biochemical responses that trigger an emotional cascade impairing normal functioning." - Seven of Nine, Star Trek: Voyager',
            '"When every logical course of action is exhausted, the only option that remains is inaction." - Tuvok, Star Trek: Voyager',
            '"Violence may keep an enemy at bay, but only peace can make him a friend." - Winn Adami, Star Trek: Deep Space Nine',
            '"A thing is not beautiful because it lasts." - Vision, Avengers: Age of Ultron',
            '"Your name is unknown but your deeds are immortal." - Tomb of the Unkown Soldier',
            '"Ya come from nothin’, yer goin’ back to nothin’, what’ve you lost? Nothing!" - Monty Python, Always Look on the Bright Side of Life',
            '"Adjust before you draw your terminal breath!" - Monty Python, Always Look on the Bright Side of Life',
            '"Ayy carambe donde esta la bibliotekaaaaaaaaaaaa" - Technoblade',
            '"But if SkyBlock has taught me anything it’s that if you have a problem, the answer is slavery." - Technoblade',
            '"Know your bounds, or your bounds will be made known to you." - George Love, Good Advice in General',
            '"A relationship built on one-sided trust is like slicing pumpkin blindfolded. It’s going to end in blood and tears unless you remove the blindfold." - George Love, Good Advice in General',
            '"Surprises come out of the oblivious." - George Love, Good Advice in General',
            '"’Winter is coming!’, ’We do not sow!’ Strong, strong words. Krakens and direwolves, fierce beasts. But a golden rose growing strong? Hah! That strikes fear in the heart." - Olenna Tyrell, A Game of Thrones',
            '"A teacup that is broken cannot be mended by filling it with more tea. The same goes for love." - Edgar Alvyra, Love is a Force',
            '"All this has happened before, and will happen again." - Cylon Hybrid, Battlestar Galactica',
            '"Can you take what I just said about Nazis as my quote?" - Emrys Gregory. The answer was no.',
            '"No." - George Love',
            '"Some wounds never truly heal, and bleed again at the slightest word." - Eddard Stark, A Game of Thrones',
            '"Power resides where you believe it resides. It’s a trick, a shadow on the wall." - Varys, A Game of Thrones',
            '"A ruler who kills those devoted to them is not a ruler that inspires devotion." - Tyrion Lannister, A Game of Thrones',
            '"Never forget what you are. The rest of the world will not. Wear it like armour, and it can never be used to hurt you." - Tyrion Lannister, A Game of Thrones',
            '"No need to assume the last word, I’ll assume it was something clever." - Sansa Stark, A Game of Thrones',
            '"The world is overflowing with horrible things, but they’re all a tray of cakes next to death." - Olenna Tyrell, A Game of Thrones',
            '"It is beautiful beneath the sea, but stay too long and you’ll drown." - Three-Eyed Raven, A Game of Thrones',
            '"The freedom to make my own mistakes was all I’ve ever wanted." - Mance Rayder, A Game of Thrones',
            '"It doesn’t matter what we want. Once we get it, we want something else." - Petyr Baelish, A Game of Thrones',
            '"You’re not ready? No one ever is. We don’t get to choose our time." - Ancient One, Doctor Strange',
            '"We believe in ordinary acts of bravery, in the courage that drives one person to stand up for another." - Will, Divergent',
            '"My father used to say that sometimes, the best way of helping someone is just to be near them." - Tris Prior, Divergent',
            '"I have found that whoever wields the sword decides who holds the pen." - Lucas Grey, Hitman 2016',
            '"What was will be, what will be was." - The Worm-in-Waiting, Stellaris',
            '"Don’t be envious of those who live in bliss while you work yourself into the ground. It is because of people like you that there are others who can afford to live in bliss. Some are not so lucky." - George Love, Good Advice in General',
            '"Any man who must say "I am the King" is no true King." - Tywin Lannister, A Game of Thrones',
            '"The greatest glory in living lies not in ever falling, but in rising every time we fall." - Nelson Mandela,',

        ]

        comma = [
            "This is what you are looking for: ’",
        ]

        ctx.send(f'{random.choice(quotes)}')

    @commands.command()
    async def choose(self, ctx, *choices: commands.clean_content):
        if len(choices) < 2:
            embed = discord.Embed(
                colour=discord.Colour.dark_red())
            embed.set_author(name='GeorgeBot™ Case Return Protocol')
            embed.add_field(name='Case 19', value='Minigame Error (Insufficient Arguments Inputted)')
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'I choose {random.choice(choices)} :D')


def setup(bot):
    bot.add_cog(Minigames(bot))
