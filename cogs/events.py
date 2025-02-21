import disnake
from disnake.ext import commands as dis_commands

class Events(dis_commands.Cog):
    def __init__(self, bot: dis_commands.Bot):
        self.bot = bot

    @dis_commands.Cog.listener()
    async def on_connect(self):
        print('Successful connection')

    @dis_commands.Cog.listener()
    async def on_ready(self):
        print('Client already')

def setup(bot: dis_commands.Bot):
    bot.add_cog(Events(bot))