import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event 
async def on_ready():
    """
    When the bot is ready this event will run.
    """
    print(f"Ready as {bot.user}\n===========")
    
@bot.event
async def on_member_join(member):
    """
    When the bot sees a member join a server this event will run.
    """
    print(member + " just joined a server!")
    
    # Or...
    
    channel = nextcord.utils.get(bot.get_all_channels(), guild__name='Server', name='welcome')
    await channel.send(f"{member} joined a server!")
    
    """
    Maybe you want it so it only says it when a member joins *one* server...
    """
    
    if member.guild.id == [your_guild_id]:
        channel = nextcord.utils.get(bot.get_all_channels(), guild__name='Server', name='welcome')
        await channel.send(f"{member} joined a server!")
        
bot.run("token")
    
