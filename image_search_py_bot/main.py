import discord
import os
from discord.ext import commands
from googleapiclient.discovery import build
##from keep_alive import keep_alive

client = commands.Bot(command_prefix=".")#bot prefix example: (.show)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("with your mom"))
    print(f"we are in {client.user}'s butt")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

#keep_alive()
client.run('your boy token')
