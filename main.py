import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
  print(f"Logged in as {client.user}")


@client.command()
async def test(ctx):
  await ctx.send("I am not a robot!")


client.run(os.environ['discordToken'])
