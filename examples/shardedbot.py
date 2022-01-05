import nextcord
from nextcord.ext import commands

bot = commands.AutoShardedBot(shard_count="your shard count here", command_prefix="?")

"""
your code here
...
"""

bot.run("token")

