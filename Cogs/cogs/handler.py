import discord
from discord.ext import commands

class Handler(commands.Cog):
  
  def __init__(self, client):
    
    self.client = client
    
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    print(error)
    
 def setup(client):
  client.add_cog(Handler(client))
