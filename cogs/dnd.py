import disnake
from disnake.ext import commands as dis_commands

class Dnd(dis_commands.Cog):
    def __init__(self, bot: dis_commands.Bot):
        self.bot = bot

    @dis_commands.slash_command(name='hello_world')
    async def hello_world(self, inter: disnake.CommandInteraction):
        await inter.send(content="Hello world!", ephemeral=True)

def setup(bot: dis_commands.Bot):
    bot.add_cog(Dnd(bot))