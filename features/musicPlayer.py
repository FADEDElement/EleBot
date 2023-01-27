import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

class musicPlayer(commands.Cog):
  def __init__(self, client): 
    self.client = client

    self.isPlaying = False

    self.musicQueue = []
    self.YDL_OPTIONS = {
      "format": "bestaudio",
      "noplaylist": "True"
    }
    self.FFMPEG_OPTIONS = {
      "before_options": "-reconnect 1 -reconnected_streamed 1 -reconnect_delay_max 5",
      "options": "-vn"
    }

    self.vs = None