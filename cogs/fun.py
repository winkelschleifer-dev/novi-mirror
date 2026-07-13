from discord.ext import commands
import discord

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def howfemboy(self, ctx, member:discord.Member = None):
    if member is None:
      member = ctx.author

    percent = member.id % 101

    await ctx.send(f"{member.display_name} is {percent}% femboy")





async def setup(bot):
  await bot.add_cog(Fun(bot))