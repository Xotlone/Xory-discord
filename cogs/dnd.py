from random import randint

import disnake
from disnake import Option, OptionType, OptionChoice
from disnake.i18n import Localized
from disnake.ext import commands as dis_commands

class Dnd(dis_commands.Cog):
    def __init__(self, bot: dis_commands.Bot):
        self.bot = bot

    @dis_commands.slash_command(
        name='dice',
        description=Localized('Бросок игральной кости', key='dice.desc'),
        options=[
            Option(
                name='sides',
                description=Localized('Количество граней. По умолчанию 20',
                                      key='dice.option1.desc'),
                type=OptionType.integer,
                min_value=2
            ),
            Option(
                name='hidden',
                description=Localized('Скрытый бросок',
                                      key='dice.option2.desc'),
                choices=[
                    OptionChoice(Localized('да', key='yes'), '1'),
                    OptionChoice(Localized('нет', key='no'), '0')
                ]
            )
        ]
    )
    async def dice(self, inter: disnake.CommandInteraction, sides: int = 20,
                   hidden: str = False):
        value = randint(1, sides)

        color = disnake.Color.dark_embed()
        if value == 1: color = disnake.Color.red()
        elif value == 20: color = disnake.Color.gold()
        if (value == 1) or (value == 20): value = f'**{value}**'

        embed = disnake.Embed(
            title=value,
            timestamp=inter.created_at,
            color=color
        )
        embed.set_author(name=inter.author.display_name,
                         icon_url=inter.author.display_avatar.url)
        await inter.send(embed=embed, ephemeral=bool(int(hidden)))


def setup(bot: dis_commands.Bot):
    bot.add_cog(Dnd(bot))