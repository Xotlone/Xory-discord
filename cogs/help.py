""""
На будущее: Нужно будет разделить команды, на разные группы или добавить кнопку переноса
"""
import disnake

from disnake.ext import commands
from disnake.embeds import Embed
from disnake.app_commands import Option, OptionChoice

class Help(commands.Cog):
    DECORATION = '```'
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def get_locale(self, name_key: str, inter: disnake.CommandInteraction):
        try:
            return self.bot.i18n.get(name_key)[str(inter.locale)]
        except KeyError:
            return self.bot.i18n.get(name_key)['en-US']

    @commands.slash_command(
        name='help',
        description='Command sends list with all command',
        options=[
            Option(name='lists',
                   description='Choose the list of command',
                   choices=[
                       OptionChoice('slash commands', value='0'),
                       OptionChoice('simple commands', value='1')
                   ],
                   required=True
                   ),
        ])
    async def help(self, inter: disnake.CommandInteraction, lists):
        embed = Embed(
            title=self.get_locale('help.title', inter),
        )

        embed.description = ''

        if lists == '0':
            for com in self.bot.slash_commands:
                embed.description += f'```{com.name}: {com.description}```'
        else:
            if self.bot.commands == set():
                embed.description += f'```Simple commands not exists```'
            else:
                for com in self.bot.commands:
                    embed.description += f'```{com.name}: {com.description}```'

        await inter.send(embed=embed,
                         ephemeral=True
                         )

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))