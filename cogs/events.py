from types import NoneType

import disnake

from disnake.ext import commands as dis_commands
from disnake.embeds import Embed
from disnake import utils

import database

class Events(dis_commands.Cog):
    BEGIN_SCORE = 0
    def __init__(self, bot: dis_commands.Bot):
        self.bot = bot

    @dis_commands.Cog.listener()
    async def on_connect(self):
        print('Successful connection')

    @dis_commands.Cog.listener()
    async def on_ready(self):
        print('Client already')

    @dis_commands.Cog.listener()
    async def on_member_join(self, id_member):
        database.cursor.execute(f"""INSERT INTO Member (ID, Score) 
                                VALUES ('{id_member}', {Events.BEGIN_SCORE})""")

        database.connect.commit()
        print(f"Added new member in database: {id_member}")

    @dis_commands.Cog.listener()
    async def on_member_remove(self, id_member):
        database.cursor.execute(f"""DELETE FROM Member
                            WHERE '{id_member}'""")

        database.connect.commit()
        print(f"Remove member from database: {id_member}")

    @dis_commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        embed = Embed(title='New level!')

        out = 0
        buffer = 0

        try:
            score = database.cursor.execute(f"""SELECT Score FROM Member WHERE ID = '{message.author}'""").fetchone()[0]

            content = len(message.content)

            if score is None:
                buffer = 1
                out = 1
            else:
                buffer = int(score)
                out = int(score)+content

            b_current_level = (buffer ** (1 / 2)) // 10
            b_current_score = (b_current_level * 10) ** 2
            b_next_score = ((b_current_score + 1) * 10) ** 2

            current_level = (out**(1/2))//10
            current_score = (current_level*10)**2

            embed.description = f'User {message.author} has new level: {int(current_level)}'

            if current_score >= b_next_score:
                await message.channel.send(embed=embed)

            database.cursor.execute(f"""UPDATE Member SET score = {out} WHERE ID='{message.author}'""")
            database.connect.commit()
        except IndexError:
            database.cursor.execute(f"""INSERT INTO Member (ID, Score) 
                                VALUES ('{message.author}', {0})""")
        except TypeError:
            pass
def setup(bot: dis_commands.Bot):
    bot.add_cog(Events(bot))