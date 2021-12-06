import discord
from discord.ext import commands
import random as r
import aiohttp
from virustotal_python import Virustotal


def bot_commands():
 
    bot = commands.Bot(command_prefix = '+') 

    # API keys and files to read from go here. This helps from exposing keys in code.
    vtotal_key = open("virustotalapikey.txt","r").read()
    token = open("token.txt","r").read()
    vt = Virustotal(vtotal_key)

    # Ready message for bot client which will output to the terminal showing that its runnning
    @bot.event
    async def on_ready():
        print(f"SinBot has been summoned from the depths of hell!")
 
    # Displays users that join the channel with a welcome message
    @bot.event
    async def on_member_join(member):
        embed = discord.Embed(colour=0x95efcc,description=f"Welcome!, You are the {len(list(member.guild.members))} member!")
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.set_footer(text=f"{member.guild}",icon_url=f"{member.guild.icon_url}")


    # Discord server rules


    # Takes in questions and answers your destiny
    @bot.command(brief='-- Ask the false prophet anything', description='Usage Example:')
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
   # Error handler for when an argument is not addedd for the command bu user
    @falseprophet.error
    async def falseprophet_error(ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You are missing an argument with the command.. ```Example: +falseprophet <question>```')

    
    # Virus total API call to scan a URL
    @bot.command(brief='-- Scans any URL to make sure its safe using Virustotal', description='Usage Example:')
    async def urlscan(ctx,*,urlscanner):
        vscan = vt.url_scan([urlscanner])
        await ctx.send(vscan)
    # Error handler for when an argument is not addedd for the command bu user
    @urlscan.error
    async def urlscan_error(ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You are missing an argument with the command.. ```Example: +urlscan <url to scan>```')
 
    
    # Generates random photos of foxes
    @bot.command(brief='-- Generates Cute random photo of a fox', description='Usage Example:')
    async def foxes(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://randomfox.ca/floof") as f:
                data = await f.json()
                embed = discord.Embed(title="Foxy")
                embed.set_image(url=data['image'])
                embed.set_footer(text='Source: https://randomfox.ca/')
                await ctx.send(embed=embed)


# Generates random photos of cats
    @bot.command(brief='-- Generates a random cat photo', description='Example Usage:')
    async def cats(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://aws.random.cat/meow") as f:
                data = await f.json()
                embed = discord.Embed(title="Kitties")
                embed.set_image(url=data['file'])
                embed.set_footer(text='Source: https://aws.random.cat/')
                await ctx.send(embed=embed)
     

 # Grabs random dog Photos 
    @bot.command(brief='-- Generates a random doggo photo', description='Example Usage:')
    async def dogs(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random.dog/woof.json") as f:
                data = await f.json()
                embed = discord.Embed(title="Doggos")
                embed.set_image(url=data['url'])
                embed.set_footer(text='Source: https://random.dog')
                await ctx.send(embed=embed)

# Grabs random hentai photos
    @bot.command(brief='-- Generates a random Hentai photo ;)', description='Example Usage:')
    async def hentai(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/nsfw/waifu") as f:
                data = await f.json()
                embed = discord.Embed(title=";)")
                embed.set_image(url=data['url'])
                embed.set_footer(text='Source: https://api.waifu.pics/')
                await ctx.send(embed=embed)
   


# Grabs Pokemon 
    @bot.command(brief='-- Generates a random pokemon', description='Example Usage:')
    async def pokemon(ctx):
       async with aiohttp.ClientSession() as cs:
            async with cs.get("https://lorempokemon.fakerapi.it/pokemon") as r:
                await ctx.send(r.url)



    # Grabs random Photography Photos 
    @bot.command(brief='-- Generates a random photo', description='Example Usage:')
    async def random(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://picsum.photos/400/400") as r:
                await ctx.send(r.url)
    
    # Grabs random Gifs 
    @bot.command(brief='-- Generates a random gif', description='Example Usage:')
    async def gif(ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("") as r:
                await ctx.send(r.url)


    
    
    bot.run(token)


bot_commands()


