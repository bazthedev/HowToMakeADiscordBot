import discord
from discord.ext import commands
import os
from keep_alive import keep_alive # you only need this if you decide to host on replit

client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description="This is my discord.py bot!", case_insensative=True)

@client.event
async def on_ready():
  print("The bot is online")

keep_alive() # you only need this if you decide to host on replit
client.run(os.getenv("TOKEN"))
