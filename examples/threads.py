import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix="?")

"""
creates a thread with command
"""

@bot.command()
async def thread(ctx):
    thread = await ctx.channel.create_thread(name=f"thread", type=nextcord.ChannelType.public_thread)
    await thread.send("your thread is here")


bot.run("token")
