import os
import discord
from discord.ext import commands
from features.musicPlayer import musicPlayer

client = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

# Remove default help command
client.remove_command('help')

# Adding Discord Cogs
client.add_cog(musicPlayer(client))

# Signed in message
@client.event
async def on_ready():
  print(f"Signed in as {client.user}")

@client.command()
async def help(ctx):
  await ctx.reply("Help yay!", mention_author=False)

# Simple Test Command
@client.command()
async def hello(ctx):
  await ctx.reply(f"Hello {ctx.message.author.mention}!", mention_author=False)

client.run(os.environ['discordToken'])