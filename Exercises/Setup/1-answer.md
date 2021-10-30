# HowToMakeADiscordBot
## Well Done on completing your first exercise!

### The solution is below:
```py
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=commands.when_mentioned_or("?"), description="This is my discord.py bot!", case_insensative=False)

@client.event
async def on_ready():
  print("Hello World!")

client.run(os.getenv("TOKEN"))
```
### Well done if this is the answer you got!
