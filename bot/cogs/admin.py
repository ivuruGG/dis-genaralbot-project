from discord.ext import commands


class Admin(commands.Cog):
    """管理者用のCog"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx: commands.Context):
        """Botを停止するコマンド"""
        await ctx.send("Botを停止します。")
        await self.bot.close()

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context):
        """Cogをリロードするコマンド"""
        self.bot.reload_extension("bot.cogs.admin")
        await ctx.send("Cogをリロードしました。")

# Admin クラスは、commands.Cog クラスを継承しています。
# Cog を実装するためには、このクラスを継承し、Cog の機能を実装する必要があります。

# __init__ メソッドでは、bot 引数を受け取り、self.bot 属性に保存します。
# これは、この Cog が属する Bot インスタンスを参照するために使用されます。

# @commands.command() デコレータは、メソッドをコマンドとして登録するために使用されます。
# @commands.is_owner() デコレータは、コマンドを使用できるのは Bot のオーナーだけに制限するためのものです。

# shutdown メソッドは、Bot を停止するためのコマンドです。
# @commands.is_owner() デコレータにより、Bot のオーナーだけがこのコマンドを使用できます。
# コマンドを実行すると、"Botを停止します。" というメッセージを送信し、Bot を停止します。

# reload メソッドは、Cog をリロードするためのコマンドです。
# self.bot.reload_extension("bot.cogs.admin") により、bot.cogs.admin モジュールをリロードします。
# @commands.is_owner() デコレータにより、Bot のオーナーだけがこのコマンドを使用できます。
# コマンドを実行すると、"Cogをリロードしました。" というメッセージを送信します。

