from discord.ext import commands
import discord
import random

class Fun(commands.Cog):
  """Fun commands"""
  def __init__(self, bot):
    self.bot = bot

  @commands.command(help="Scientifically calculates how femboy someone is.")
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
  
  @commands.command(help="Get a very scientific and fully correct answer to your question")
  async def eightball(self, ctx, *, question):
    answers = [
    "Certainly.",
    "Without a doubt.",
    "Definitely.",
    "Probably.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Outlook not so good.",
    "Don't count on it.",
    "Probably not.",
    "Very doubtful.",
    "Definitely not."
    ]

    if question == "is mush a femboy" or question == "is mush femboy":
      await ctx.send("Why do you even ask? Of course he is.")
    else:
      await ctx.send(f"The 8ball says: {random.choice(answers)}")

  @commands.command(help="Gives you a random Blåhaj image")
  async def blahaj(self, ctx):
    await ctx.send(file=discord.File(f'assets/blahaj/blahaj-{random.randint(1, 5)}.jpg'))





async def setup(bot):
  await bot.add_cog(Fun(bot))