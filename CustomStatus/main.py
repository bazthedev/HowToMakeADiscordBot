import discord
from discord.ext import commands, tasks # tasks is the next thing we need
import os
from keep_alive import keep_alive # you only need this if you decide to host on replit

client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description="This is my discord.py bot!", case_insensative=True)

@client.event
async def on_ready():
  print("The bot is online")
  await change_status() # executes the change_status function when the bot has logged in
  
@tasks.loop(seconds=600) # changes every 10 minutes
async def change_status():
  await client.change_presence(activity=discord.Game("!help")) # changes bot status to !help

keep_alive() # you only need this if you decide to host on replit
client.run(os.getenv("TOKEN"))
