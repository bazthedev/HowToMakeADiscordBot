import discord
from discord.ext import commands

class Info(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def ping(self, ctx): # self must be provided
    await ctx.send("Pong!")
    
def setup(client):
  client.add_cog(Info(client))
