import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix="?")

@bot.command()
async def reply(ctx, msg):
    await ctx.send(msg + f" -{ctx.author}")
    
bot.run("token")
