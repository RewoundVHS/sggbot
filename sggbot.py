#! /bin/python

import discord
from discord.ext import commands
import pysmash

description = '''A bot used to embed smash.gg tournament data.'''
bot = commands.Bot(command_prefix='sgg!', description=description)

# Print bot information
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game('sgg!help for command list')
    await bot.change_presence(status=discord.Status.online, activity=game)

# Embeds tournament details
@bot.command()
async def embed(ctx, link: str):
    embed = discord.Embed(title="Super Smash Boro", colour=discord.Colour(0xca3339), url="https://smash.gg/tournament/super-smash-boro/", description="Welcome to Super Smash Boro! Come down to the basement of Hamilton Hall for our first event in the eSports room. Please bring a setup, everything except for your TV.")

    embed.set_thumbnail(url="https://smashgg.imgix.net/images/tournament/167681/image-2ae63e0be031c69a9e48461a055cb6fe.png?auto=compress,format&w=280&h=280&fit=crop")

    embed.add_field(name="Date", value="08/17/2019", inline=True)
    embed.add_field(name="Time", value="6:00 PM", inline=True)
    embed.add_field(name="Address", value="Hamilton Hall, 210 Glasgow Rd, Edinboro, PA 16412, USA", inline=True)

    await ctx.send(embed=embed)

bot.run('TOKEN')
