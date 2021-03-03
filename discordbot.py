from discord.ext import commands
import os
import traceback
import asyncio 
import random 

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')



@bot.event
async def on_message(message):
    if message.content.startswith("!dice6"): #ここの!diceは好きなのにしていいぞ
        if bot.user != message.author:
            num_random = random.randrange(1,6)
            m = str(num_random)
            await bot.send_message(message.channel, m)

bot.run("[手に入れたトークンを記入しよう]")


bot.run(token)
