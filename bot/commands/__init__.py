from discord.ext.commands import Bot

bot = Bot(command_prefix='!')

# コマンドの読み込み
bot.load_extension("commands.help")
bot.load_extension("commands.ping")
bot.load_extension("commands.emoji")
bot.load_extension("commands.clear")

# Botの起動
bot.run(config.TOKEN)

# discord.ext.commands.Bot をインポートしています。
# Bot クラスのインスタンスを bot という名前で作成し、コマンドのプレフィックスを ! に設定
# bot.load_extension で commands.help、commands.ping、commands.emoji、commands.clear の各コマンドを読み込んでいます
# 最後に bot.run で config.TOKEN を引数に渡してBotを起動しています。
# ここで config.TOKEN は config.py 内で設定されたBotのトークンです。
