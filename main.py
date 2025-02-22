import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

from utils import constants


load_dotenv('.env')

command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands = True
intents = disnake.Intents.all()
localization_provider = disnake.LocalizationStore(strict=True)
localization_provider.load('locale')
bot = commands.Bot(
    command_prefix='/',
    help_command=None,
    owner_ids=constants.OWNER_IDS,
    command_sync_flags=command_sync_flags,
    test_guilds=constants.TEST_GUILDS,
    intents=intents,
    localization_provider=localization_provider
)

for cog_name in os.listdir('./cogs'):
    if cog_name.endswith('.py'):
        bot.load_extension(f'cogs.{cog_name[:-3]}')

bot.run(os.getenv('TOKEN'))