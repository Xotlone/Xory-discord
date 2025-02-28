import disnake

from disnake.ext import commands
from disnake import Option

class Clear(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name='clear',
        description='remove message from channel',
        default_member_permissions=disnake.Permissions(
            administrator=True
        ),
        options=[Option(
            name='count',
            description='Count of message, what need deleted',
        )]
    )
    async def clear(self, inter: disnake.CommandInteraction, count=5):
        await inter.channel.purge(limit=int(count))
        await inter.send(content=f'Chat was cleaned from {count} messages!\nCommand was used: {inter.user}', ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Clear(bot))