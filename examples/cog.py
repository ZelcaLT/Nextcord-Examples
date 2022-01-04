import nextcord
from nextcord.ext import commands

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """
    Instead of @bot.command(), we use
    @commands.command().

    Instead of @bot.event, we use
    @commands.Cog.listener()
    """

    """
    Your code here
    ...
    """




def setup(bot):
    bot.add_cog(Cog(bot))
