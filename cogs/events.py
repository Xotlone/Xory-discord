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
        channel = utils.get(self.bot.get_all_channels(), name=self.bot.user.locale)

        embed = Embed(title='New level!')

        out = 0
        buffer = 0

        level = 1000

        try:
            score = database.cursor.execute(f"""SELECT score FROM Member WHERE ID = '{message.author}'""").fetchall()

            content = len(message.content)

            for i in score[0]:
                buffer = int(i)
                out = int(i)+content

            last_level = buffer/level
            current_level = out/level

            embed.description = f'User {message.author} have new level: {int(current_level)}'

            if int(last_level) != int(current_level):
                await message.channel.send(embed=embed)

            database.cursor.execute(f"""UPDATE Member SET score = {out} WHERE ID='{message.author}'""")
            database.connect.commit()
        except IndexError:
            database.cursor.execute(f"""INSERT INTO Member (ID, Score) 
                                VALUES ('{message.author}', {0})""")

def setup(bot: dis_commands.Bot):
    bot.add_cog(Events(bot))