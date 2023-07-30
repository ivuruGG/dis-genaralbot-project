import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
intents = discord.Intents.all()  # すべてのIntentsを有効にする


# .env ファイルから環境変数を読み込む
load_dotenv()

# Discord Botのトークンを環境変数から取得する
TOKEN = os.getenv('DISCORD_TOKEN')

# Botクラスのインスタンスを生成する
bot = commands.Bot(command_prefix='!')

# Botが起動したときに呼び出されるイベントハンドラ


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# 「!ping」というコマンドを定義する


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')

# Discord Botを実行する
bot.run(TOKEN)
