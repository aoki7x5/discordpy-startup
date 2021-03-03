
import asyncio #なんか必要らしい
import discord #さっきpipで取り入れたやつだぞ！
import random #ランダムな数字を作るモジュールだぞ！

client = discord.Client()

@client.event #コマンドラインに出力されるぞ。printのところが出ないなら何かが間違ってるぞ
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("!dice6"): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            num_random = random.randrange(1,6)
            m = str(num_random)
            await client.send_message(message.channel, m)

client.run("[手に入れたトークンを記入しよう]")

@client.event
async def on_message(message):
    if message.content.startswith("!dice5"): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            num_random = random.randrange(1,5)
            m = str(num_random)
            await client.send_message(message.channel, m)

client.run("[手に入れたトークンを記入しよう]")

@client.event
async def on_message(message):
    if message.content.startswith("!dice4"): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            num_random = random.randrange(1,4)
            m = str(num_random)
            await client.send_message(message.channel, m)

client.run("[手に入れたトークンを記入しよう]")

@client.event
async def on_message(message):
    if message.content.startswith("!dice3"): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            num_random = random.randrange(1,3)
            m = str(num_random)
            await client.send_message(message.channel, m)

client.run("[手に入れたトークンを記入しよう]")

@client.event
async def on_message(message):
    if message.content.startswith("!dice2"): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            num_random = random.randrange(1,2)
            m = str(num_random)
            await client.send_message(message.channel, m)

client.run("[手に入れたトークンを記入しよう]")
