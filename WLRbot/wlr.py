import asyncio
import discord
from discord.ext import commands
import random
from datetime import date
from datetime import datetime
from threading import Timer


songs = []

d0 = date(2018, 8, 23)
d_today = date.today()
delta = d_today - d0
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("The bot is running.")

@client.command(aliases=['i'])
async def info(ctx):
	command_list = open("commands.txt", "r")
	file_contents = command_list.read()
	await ctx.send(file_contents)
	command_list.close()

@client.command()
async def wlr(ctx):
    await ctx.send(f"It has been {delta.days} days since Whole Lotta Red was announced.")
    embed = discord.Embed(color=discord.Colour.red())
    embed.set_image(url='https://i.kym-cdn.com/photos/images/original/001/096/564/2f7.jpg')
    await ctx.send(embed=embed)


@client.command(aliases=["as"])
async def add(ctx, *, song):
	song_name = songs.append(song)
	await ctx.send(f"Adding {song}...")


@client.command(aliases=['q'])
async def queue(ctx):
	for song in songs:
		await ctx.send(song)


x = datetime.today()
y = x.replace(day=x.day+1, hour=0, minute=0, second=1, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def sotd_1():
	sotd_random = random.choice(songs)
	print(f"Today's song of the day is {sotd_random}.")

t = Timer(secs, sotd_1)
t.start()

@client.command(aliases=['c'])
async def clear(ctx):
    await ctx.send("All songs have been cleared.")
    await ctx.send(songs.clear())


@client.command(aliases=['hm'])
async def howmany(ctx):
    if len(songs) == 0:
        await ctx.send("**There are no songs found!** Please add a song by entering '!as (link to the song)'")
    else:
        await ctx.send(f"There are **{len(songs)}** songs in the list.")


@client.command()
async def kidboy(ctx):
	await ctx.send("<:l_:763574607742631986>")

@client.command()
async def kjr(ctx):
    embed = discord.Embed(color=discord.Colour.blue())
    embed.set_image(url='https://i.imgflip.com/4jiciv.jpg')
    await ctx.send(embed=embed)

@client.command()
async def poi(ctx):
    embed = discord.Embed(color=discord.Colour.green())
    embed.set_image(url='https://i.imgflip.com/4jid14.jpg')
    await ctx.send(embed=embed)



client.run("NzY4ODU4MDI0ODAxODYxNjMy.X5Gk1Q.9r9RDnZo4H5L7qtTiO8T31nF8g0")
