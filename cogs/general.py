from discord.ext import commands
import discord

class General(commands.Cog):
  """General commands"""
  def __init__(self, bot):
    self.bot = bot

  @commands.command(help="Gets Novi's brain delay")
  async def ping(self, ctx):
    latency = round(self.bot.latency * 1000)
    await ctx.send(f"🏓 Pong! Latency: {latency} ms")

  @commands.command(help="Shows some info about the bot")
  async def about(self, ctx):
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

#  @commands.command()
 # async def help(self, ctx):
  #  embed=discord.Embed(
      #title="Help",
     # description="My prefix is *n!*. Commands:\nhelp - displays this page\nabout - displays basic bot info\nping - displays bot brain delay",
    #  color=0xfff600
    #)
   # await ctx.send(embed=embed)

  
async def setup(bot):
  await bot.add_cog(General(bot))