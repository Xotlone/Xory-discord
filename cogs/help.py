""""
На будущее: Нужно будет разделить команды, на разные группы или добавить кнопку переноса
"""

import disnake

from disnake.ext import commands
from disnake.embeds import Embed
from disnake.ui import WrappedComponent

class Help(commands.Cog):
    DECORATION = '```'
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def get_locale(self, name_key: str, inter: disnake.CommandInteraction):
        try:
            return self.bot.i18n.get(name_key)[str(inter.locale)]
        except KeyError:
            return self.bot.i18n.get(name_key)['en-US']

    @commands.slash_command(name='help', description='Command sends list with all command')
    async def help(self, inter: disnake.CommandInteraction):
        embed_help = Embed(
            title=self.get_locale('help.title', inter),
        )

        embed_help.description = ''

        for help_c in self.bot.slash_commands:
            embed_help.description += f'```{help_c.name}: {help_c.description}```'

        await inter.send(embed=embed_help,
                         ephemeral=True
                         )

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))