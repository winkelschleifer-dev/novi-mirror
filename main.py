import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="n!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("about testing")

@bot.command()
async def about(ctx):
  embed = discord.Embed(
    title="Novi",
    descriprion="Bot for Nova's Discord community",
    color=0xEA00FF
  )
  embed.add_field(
    name="Novi version",
    value="v0.1.5",
    inline=True
  )
    await ctx.send(embed=embed)



@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! Latency: {latency} ms")

print(TOKEN is not None)
bot.run(TOKEN)