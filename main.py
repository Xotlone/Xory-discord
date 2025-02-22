import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

from utils import constants


load_dotenv('.env')

localization_provider = disnake.LocalizationStore(strict=True)
localization_provider.load('localization')
intents = disnake.Intents.all()
bot = commands.Bot(
    command_prefix='/',
    help_command=None,
    owner_ids=constants.OWNER_IDS,
    intents=intents,
    localization_provider=localization_provider
)

for cog_name in os.listdir('./cogs'):
    if cog_name.endswith('.py'):
        bot.load_extension(f'cogs.{cog_name[:-3]}')

bot.run(os.getenv('TOKEN'))