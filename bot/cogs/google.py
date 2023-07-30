import os
from discord.ext import commands
import googlesearch


class Google(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="google", aliases=["search"])
    async def google_search(self, ctx: commands.Context, *, query: str):
        """指定したクエリでGoogle検索を行います。"""
        results = googlesearch.search(query, num_results=3)
        await ctx.send(f"検索結果：{', '.join(results)}")


def setup(bot: commands.Bot):
    bot.add_cog(Google(bot))
