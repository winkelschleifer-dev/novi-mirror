from discord.ext import commands
import discord
import utils.time

class Moderation(commands.Cog):
  """Moderation commands"""
  def __init__(self, bot):
    self.bot = bot

  @commands.command(help="Mutes a user")
  async def mute(self, ctx, member:discord.Member, time, reason=None):
    time_unformatted = utils.time.parse_time(time)
    await member.timeout(time_unformatted, reason=reason)
    await ctx.send(f"{member.display_name} was muted for {time}. Reason: {reason}")

  @commands.command(help="Kicks a user")
  async def kick(self, ctx, member: discord.Member, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.display_name} was kicked. Reason: {reason}")

  @commands.command(help="Bans a user")
  async def ban(self, ctx, member: discord.Member, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.display_name} was banned. {reason}")

  @commands.command(help="Unbans a user")
  async def unban(self, ctx, member: discord.Member):
    await member.unban()
    await ctx.send(f"{member.display_name} was unbanned.")


async def setup(bot):
  await bot.add_cog(Moderation(bot))