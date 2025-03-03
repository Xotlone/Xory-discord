from disnake import CommandInteraction
from disnake.ext import commands
from disnake import Option, OptionType, OptionChoice
from disnake.embeds import Embed

import database

class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='level',
        description='Send your info about level')
    async def level(self, inter: CommandInteraction):
        line = ''
        embed = Embed()

        score_member = database.cursor.execute(f"SELECT Score FROM Member WHERE ID = '{inter.author}'").fetchone()[0]

        if score_member is None:
            score_member = 1

        level = (float(score_member)**(1/2))/10

        score = (int(level) * 10)**2
        n_score = (((int(level)+1)*10)**2)

        embed.title = f'Your level {int(level)}'
        for i in range(11):
            if i/10 <= level-int(level):
                line+='#'
            else:
                line+='-'
        embed.description = f'Score: {score_member}/{int(n_score)}\n\n{int(level)}| {line} | {int(level+1)}'
        await inter.send(embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Level(bot))