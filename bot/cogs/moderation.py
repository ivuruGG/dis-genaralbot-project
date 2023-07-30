import discord
from discord.ext import commands


class Moderation(commands.Cog):
    """モデレーション用のCog"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        """メンバーをキックするコマンド"""
        await member.kick(reason=reason)
        await ctx.send(f"{member}をキックしました。")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        """メンバーをBANするコマンド"""
        await member.ban(reason=reason)
        await ctx.send(f"{member}をBANしました。")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, *, member):
        """メンバーのBANを解除するコマンド"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user}のBANを解除しました。")
                return


# Moderation クラスは、commands.Cog クラスを継承しています。
# Cog を実装するためには、このクラスを継承し、Cog の機能を実装する必要があります。

# __init__ メソッドでは、bot 引数を受け取り、self.bot 属性に保存します。
# これは、この Cog が属する Bot インスタンスを参照するために使用されます。

# @commands.command() デコレータは、メソッドをコマンドとして登録するために使用されます。
# @commands.has_permissions() デコレータは、コマンドを使用できるのは特定の権限を持つメンバーだけに制限するためのものです。

# kick メソッドは、メンバーをキックするためのコマンドです。
# @commands.has_permissions(kick_members=True) デコレータにより、kick_members 権限を持つメンバーだけがこのコマンドを使用できます。
# コマンドを実行すると、メンバーをキックし、"{member}をキックしました。" というメッセージを送信します。
