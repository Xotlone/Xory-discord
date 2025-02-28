import disnake

from disnake.ext import commands
from disnake import Option, OptionType
from disnake import Permissions
from disnake.abc import Snowflake

class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name='ban',
        description='Ban member',
        options=[
            Option(
                name='user',
                description='Select user for ban',
                required=True,
                type=OptionType.user
            ),
            Option(
                name='reason',
                description='Write reason for ban user',
                type=OptionType.string
            ),
        ],
        default_member_permissions=Permissions(
            administrator=True
        )
    )
    async def ban(self, inter: disnake.CommandInteraction, user: disnake.User, reason: str=None):
        await inter.guild.ban(user=user, clean_history_duration=7, reason=reason)
        await inter.send(content=f'{user} has been baned', ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Ban(bot))