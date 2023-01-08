import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@client.command()
async def test(ctx):
  await ctx.send("I am not a robot!")

client.run(os.environ['discordToken'])