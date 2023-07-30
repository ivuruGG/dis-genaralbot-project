import os
from discord.ext import commands


def setup(bot: commands.Bot):
    """各Cogを登録する関数"""
    for filename in os.listdir("./bot/cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"bot.cogs.{filename[:-3]}")

#-------------------------------------------------------------------------------------
# setup 関数は、Bot インスタンスに各 Cog を登録するために使用されます。
# 引数の bot には、登録対象の Bot インスタンスが渡されます。

# os.listdir("./bot/cogs") は、./bot/cogs ディレクトリ内のファイル名のリストを返します。
# if filename.endswith(".py") は、.py で終わるファイルのみを対象とする条件です

# bot.load_extension(f"bot.cogs.{filename[:-3]}") は、Cog を登録するためのコードです。
# load_extension メソッドは、Cog を Python モジュールとして読み込み、Bot インスタンスに登録するメソッドです。
# 引数には、Python モジュールの名前を指定します。
# ここでは、Cog のファイル名から .py を除いたものを、bot.cogs の下にあるモジュール名として指定しています。

# このように、cogs/__init__.py ファイルを作成することで、Bot の機能を拡張するための準備が整います。
# Cog の実装を作成したら、bot.cogs ディレクトリにファイルを保存するだけで、自動的に登録されるようになります。
