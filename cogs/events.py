import disnake
from disnake.ext import commands as dis_commands

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
        database.connect.close()

    @dis_commands.Cog.listener()
    async def on_member_remove(self, id_member):
        database.cursor.execute(f"""DELETE FROM Member
                            WHERE '{id_member}'""")

        database.connect.commit()
        print(f"Remove member from database: {id_member}")
        database.connect.close()

def setup(bot: dis_commands.Bot):
    bot.add_cog(Events(bot))