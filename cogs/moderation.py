from discord.ext import commands
import discord

class Moderation(commands.Cog):
  """Moderation commands"""
  def __init__(self, bot):
    self.bot = bot

  @commands.command(help="Kicks a user")
  async def kick(self, ctx, member: discord.Member):
    pass
  