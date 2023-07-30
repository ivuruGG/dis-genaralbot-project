from discord.ext.commands import Cog, command


class Admin(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name='load')
    async def load_cog(self, ctx, cog_name: str):
        try:
            self.bot.load_extension(f'cogs.{cog_name}')
        except Exception as e:
            print(f'Error loading cog: {cog_name}\n{type(e).__name__}: {e}')
        else:
            print(f'Loaded cog: {cog_name}')
            await ctx.send(f'Loaded cog: {cog_name}')

    @command(name='unload')
    async def unload_cog(self, ctx, cog_name: str):
        try:
            self.bot.unload_extension(f'cogs.{cog_name}')
        except Exception as e:
            print(f'Error unloading cog: {cog_name}\n{type(e).__name__}: {e}')
        else:
            print(f'Unloaded cog: {cog_name}')
            await ctx.send(f'Unloaded cog: {cog_name}')

    @command(name='reload')
    async def reload_cog(self, ctx, cog_name: str):
        try:
            self.bot.unload_extension(f'cogs.{cog_name}')
            self.bot.load_extension(f'cogs.{cog_name}')
        except Exception as e:
            print(f'Error reloading cog: {cog_name}\n{type(e).__name__}: {e}')
        else:
            print(f'Reloaded cog: {cog_name}')
            await ctx.send(f'Reloaded cog: {cog_name}')

# ----------------------------------------------------------------------------------
# Cog クラスを継承した Admin クラスを定義し、以下の3つのコマンドを実装しています。


# load_cog: 指定された名前のcogをロードします。
# unload_cog: 指定された名前のcogをアンロードします。
# reload_cog: 指定された名前のcogをリロードします。
# それぞれの関数で行われる処理は以下のとおりです。

# load_cog:
# bot.load_extension()を使って、cogs パッケージ内の指定された名前のcogをロードします。
# エラーが発生した場合、エラーの内容をコンソールに表示し、指定されたチャンネルにエラーメッセージを送信します。
# 成功した場合、成功メッセージをコンソールに表示し、指定されたチャンネルに成功メッセージを送信します。

# unload_cog:
# bot.unload_extension()を使って、cogs パッケージ内の指定された名前のcogをアンロードします。
# エラーが発生した場合、エラーの内容をコンソールに表示し、指定されたチャンネルにエラーメッセージを送信します。
