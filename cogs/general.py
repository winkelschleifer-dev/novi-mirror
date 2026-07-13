from discord.ext import commands
import discord

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def ping(ctx):
    latency = round(self.bot.latency * 1000)
    await ctx.send(f"🏓 Pong! Latency: {latency} ms")

  @commands.command()
  async def about(ctx):
    embed = discord.Embed(
      title="Novi",
      description="Custom bot for Nova's Discord community",
      color=0xfff600
    )
    embed.add_field(
      name="Novi version",
      value="v0.1.7",
      inline=True
    )

    await ctx.send(embed=embed)

    async def setup(bot):
      await bot.add_cog(General(bot))