import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from checkers import Board

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents=discord.Intents.all()
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print("CheckersBot is in " +str(guild_count) + " guilds.")


# @bot.event
# async def on_message(message):
#     print(message.content)
#     if message.content == "hello":
#         await message.channel.send("hey shitter")

@bot.command()
async def play(ctx):
    print("in play function")
    board = Board()
    await ctx.send(board.print_board())


bot.run(DISCORD_TOKEN)