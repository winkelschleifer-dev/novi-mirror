import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class NoviHelp(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__(
            no_category="Other",
            dm_help=False
        )
      


bot = commands.Bot(
    command_prefix="n!",
    intents=intents,
    help_command=NoviHelp()
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


async def load_cogs():
    await bot.load_extension("cogs.general")
    await bot.load_extension("cogs.moderation")
    await bot.load_extension("cogs.fun")


async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)


import asyncio
asyncio.run(main())