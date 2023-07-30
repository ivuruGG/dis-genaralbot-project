import os
from dotenv import load_dotenv

load_dotenv()

# Botの設定
BOT_NAME = "Yamshita"  # Botの名前
BOT_PREFIX = "!"  # コマンドのプレフィックス
BOT_DESCRIPTION = "My Awesome Bot"  # Botの説明
BOT_VERSION = "1.0.0"  # Botのバージョン

# モジュールの設定
MODULES = [
    "cogs.greetings",
    "cogs.admin",
]

# Discordの設定
DISCORD_TOKEN = os.getenv("MTEwMzYwMzUxMjE5MDk2Mzc1NQ.G9cuvw.3iZ8HJiTHKSPZUv2Jg5iypBlvdLHwdZue7kekw")
DISCORD_GUILD = os.getenv("- ̗̀ 𖤐いゔる。ーむ𖤐´-")

# dotenv ライブラリを使用して、.env ファイルから環境変数を読み込みます。
# .env ファイルには、Bot のトークンや接続先の Discord サーバーの名前など、機密情報を含めることができます。

# BOT_NAME、BOT_PREFIX、BOT_DESCRIPTION、BOT_VERSION のように、Bot の設定を定義しています。
# MODULES には、Bot の機能ごとに別々の Python モジュールを用意し、そのモジュール名をリストで指定します。
# 例えば、cogs.greetings は、挨拶機能のためのモジュールであるということを示しています。
# 最後に、Discord のトークンと接続する Discord サーバーの名前を環境変数から取得しています。

# config.py ファイルを作成することで、Bot の設定を中心に管理できるようになります。
# また、機能を追加する場合は、MODULES にモジュール名を追加するだけで済むため、拡張性が高くなります。
