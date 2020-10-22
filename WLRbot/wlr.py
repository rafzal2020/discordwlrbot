import discord
from discord.ext import commands
import time
from datetime import date

d0 = date(2018, 8, 23)
d_today = date.today()
delta = (d_today) - d0
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
	print("The bot is running.")

@client.command()
async def wlr(ctx):
	await ctx.send(f"It has been {delta.days} days since Whole Lotta Red was announced.")
	embed = discord.Embed(color = discord.Colour.red())
	embed.set_image(url = "https://i.kym-cdn.com/photos/images/original/001/096/564/2f7.jpg")
	await ctx.send(embed = embed)

client.run("NzY4ODU4MDI0ODAxODYxNjMy.X5Gk1Q.NiaKaZc7zHQOT5K3S3B7F3cXiNs")

