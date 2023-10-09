import discord
from discord.ext import commands

from constants import *
from constants import BOT_TOKEN
from youtube import fetch_audio_from_yt

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents = intents)

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def play(ctx, url):
    voice_channel = ctx.voice_client

    if not voice_channel:
        await ctx.send("I'm not in a voice channel. Use `!join` to invite me.")
        return

    voice_channel.stop()
    audio_file = fetch_audio_from_yt(url)
    voice_channel.play(discord.FFmpegPCMAudio(audio_file))



@bot.command()
async def pause(ctx):
    voice_channel = ctx.voice_client
    if voice_channel and voice_channel.is_playing():
        voice_channel.pause()

# Resume playback
@bot.command()
async def resume(ctx):
    voice_channel = ctx.voice_client
    if voice_channel and voice_channel.is_paused():
        voice_channel.resume()

# Stop playback and disconnect from the voice channel
@bot.command()
async def stop(ctx):
    voice_channel = ctx.voice_client
    if voice_channel:
        voice_channel.stop()
        await voice_channel.disconnect()

# Run the bot with your bot token
bot.run(BOT_TOKEN)