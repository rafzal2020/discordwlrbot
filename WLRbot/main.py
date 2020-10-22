import asyncio
import discord
from discord.ext import commands
import random
from datetime import date

songs = []
# empty list where user inputted songs will go

d0 = date(2018, 8, 23)
d_today = date.today()
delta = d_today - d0
# calculates the amount of days since wlr was announced
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("The bot is running.")
    #notifies the bot is running in the console

@client.command()
async def wlr(ctx):
    await ctx.send(f"It has been {delta.days} days since Whole Lotta Red was announced.")
    embed = discord.Embed(color=discord.Colour.red())
    embed.set_image(url='https://i.kym-cdn.com/photos/images/original/001/096/564/2f7.jpg')
    await ctx.send(embed=embed)
	# will tell you the exact amount of days since the announcement of wlr
	# displays an image


@client.command(aliases=["as"])
async def add(ctx,*,song):
    await ctx.send(songs.append(song))
# this command will add a song to the empty list


@client.command(aliases=['q'])
async def queue(ctx):
    await ctx.send(songs)
# this command prints the list


@client.command(aliases=['s'])
async def sotd(ctx):
    sotd_random = random.choice(songs)
    await ctx.send(f"Today's song of the day is {sotd_random}.")
# randomly chooses an item from the list and prints the message

# THIS PART IS STILL WIP
## async def daily_song():
    ## wait asyncio.sleep(1)
    ##await sotd()


client.run("TOKEN")
