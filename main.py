import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from checkers import Board

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

UNUSED = 'x' # represent empty board spaces
RED = 'r'
YELLOW = 'y'
EMPTY = '*'

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
#         await message.channel.send("hey loser")

@bot.command()
async def play(ctx):
    new_player1 = ctx.author
    new_player2 = ctx.message.mentions[0]

    global red_player
    global yellow_player
    global board 
    global thread

    red_player = new_player1
    yellow_player = new_player2
    board = Board()

    new_thread = await ctx.message.create_thread(
        name = f'{red_player.display_name} VERSUS '
            f'{yellow_player.display_name}'
    )
    thread = new_thread

    await thread.send(
        f'{red_player.display_name}: :red_circle:\n'
        f'{yellow_player.display_name}: :yellow_circle:\n'
    )

    await thread.send(board.print_board())

# Move a piece
# r and c = row and column of piece to move
# r2 and c2 = row and column to move piece to
@bot.command()
async def move(ctx, r: int, c: int, r2: int, c2: int):
    # player set to author of command
    player = ctx.author

    if player == red_player:
        if board.cur_piece(r2, c2) == EMPTY:
            board.red_move_no_jump(r, c, r2, c2)
        if board.cur_piece(r2, c2) == YELLOW:
            board.red_jump_move(r, c, r2, c2)

    if player == yellow_player:
        if board.cur_piece(r2,c2) == EMPTY:
            board.yellow_move_no_jump(r, c, r2, c2)
        if board.cur_piece(r2, c2) == RED:
            board.yellow_jump_move(r, c, r2, c2)
            

    print("in move func")
    await thread.send(board.print_board())


    


bot.run(DISCORD_TOKEN)