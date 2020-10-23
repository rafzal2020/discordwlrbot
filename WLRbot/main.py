import asyncio
import discord
from discord.ext import commands
import random
from datetime import date

client = commands.Bot(command_prefix='!')

d0 = date(2018, 8, 23)
d_today = date.today()
delta = d_today - d0
songs = []

@client.event
async def on_ready():
    print("The bot is running.")


@client.command(aliases=['com'])
async def commands(ctx):
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
		await ctx.send(song.title())


@client.command(aliases=['s'])
async def sotd(ctx):
    sotd_random = random.choice(songs)
    await ctx.send(f"Today's song of the day is {sotd_random.title()}.")


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
	

client.run("TOKEN")
