from discord.ext import commands
import discord

def isMod(ctx):
  return any(role.id == 1521471584983056496 for role in ctx.author.roles)

def isAdmin(ctx):
  return any(role.id == 1521471495463763990 for role in ctx.author.roles)

def isOwner(ctx):
  return any(role.id == 1521471351989211237 for role in ctx.author.roles)