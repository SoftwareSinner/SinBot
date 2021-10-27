import discord
from discord.ext import commands
import random as r
import aiohttp
from virustotal_python import Virustotal
import shodan


# Bot command actions 
def bot_commands():
    
    bot = commands.Bot(command_prefix = '+')
    vtotal_key = open("virustotalapikey.txt","r").read()
    token = open("token.txt","r").read()
    discord_rules = open("rules.txt","r").read()
    vt = Virustotal(vtotal_key)

    # Ready message for bot client which will output to the terminal showing that its runnning
    @bot.event
    async def on_ready():
        print(f"SinBot has been summoned from the depths of hell!")

    # Displays users that join the channel with a welcome message
    @bot.event
    async def on_member_join(member):
        # channel id Change this and hide the id to read from file
        embed = discord.Embed(colour=0x95efcc,description=f"Welcome!, You are the {len(list(member.guild.members))} member!")
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.set_footer(text=f"{member.guild}",icon_url=f"{member.guild.icon_url}")
        barb_chan = bot.get_channel(id=<insert channel id here>)
        await barb_chan.send(embed=embed)

    # Discord server rules
    @bot.command()
    async def rules(ctx):
        await ctx.send(discord_rules)
    
    # Takes in questions and answers your destiny
    @bot.command()
    async def falseprophet(ctx,*, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes – definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Dont count on it',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        await ctx.send(f'```Question: {question}\nAnswer: {r.choice(responses)}```')
    
    # Generates random photos of foxes
    @bot.command()
    async def foxes(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://randomfox.ca/floof") as f:
                data = await f.json()
                embed = discord.Embed(title="Foxy")
                embed.set_image(url=data['image'])
                embed.set_footer(text='Source: https://randomfox.ca/')
                await ctx.send(embed=embed)
    
   # Virus total API call to scan a URL
    @bot.command()
    async def urlscan(ctx,*,urlscanner):
        vscan = vt.url_scan([urlscanner])
        await ctx.send(vscan)

    #@bot.command()
    #async def shodan(ctx):
        #shod = 


    # Grabs random Photography Photos 
    @bot.command()
    async def random(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://picsum.photos/400/400") as r:
                await ctx.send(r.url)


    
    
    bot.run(token)


bot_commands()

