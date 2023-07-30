# Discord Bot を起動するためのエントリーポイントとなるファイルです。
import os
from dotenv import load_dotenv

from bot import Bot

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からDiscordのトークンと接続するサーバーの名前を取得する
TOKEN = os.getenv("MTEwMzYwMzUxMjE5MDk2Mzc1NQ.G9cuvw.3iZ8HJiTHKSPZUv2Jg5iypBlvdLHwdZue7kekw")
GUILD = os.getenv("- ̗̀ 𖤐いゔる。ーむ𖤐´-")

# Botクラスのインスタンスを作成する
bot = Bot()

# Botを起動する
bot.run(TOKEN, GUILD)


# -------------------------------------------------------------------------------------
# dotenv ライブラリを使用して、.env ファイルから環境変数を読み込みます。
# .env ファイルには、Bot のトークンや接続先の Discord サーバーの名前など、機密情報を含めることができます。

# 次に、Bot クラスのインスタンスを作成し、そのインスタンスの run() メソッドを呼び出して、Bot を起動します。
# run() メソッドには、先に読み込んだトークンと接続する Discord サーバーの名前を渡します。

#このファイルは、ターミナルで以下のように実行することで、Bot を起動できます。
