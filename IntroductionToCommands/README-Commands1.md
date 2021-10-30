# How to make a discord bot

## Making a basic command:
### Go to your main.py file and type in the following:
```py
@client.command()
async def ping(ctx):
  await ctx.send("Pong!")
```
### This sends a message to the channel where someone writes !ping with the content of the message being `Pong!`
