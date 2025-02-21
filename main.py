import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
bot.remove_command('help')

for cog_name in os.listdir('./cogs'):
    if cog_name.endswith('.py'):
        bot.load_extension(f'cogs.{cog_name[:-3]}')

bot.run(os.getenv('TOKEN'))