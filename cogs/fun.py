from discord.ext import commands
import discord

class Fun(commands.Cog):
  """Fun commands"""
  def __init__(self, bot):
    self.bot = bot

  @commands.command(help="Scientifically clculates how femboy someone is.")
  async def howfemboy(self, ctx, member:discord.Member = None):
    if member is None:
      member = ctx.author
    if member.id == 852565771375738890:
      percent = 9223372036854775807
    else:
      percent = member.id % 101

    await ctx.send(f"{member.display_name} is {percent}% femboy")

  @commands.command(help="Makes you a cup of coffee")
  async def coffee(self, ctx):
    await ctx.send("418: I'm a teapot")
    





async def setup(bot):
  await bot.add_cog(Fun(bot))