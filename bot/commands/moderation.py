from discord.ext.commands import Cog, command, has_permissions


class Moderation(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name='clear')
    @has_permissions(manage_messages=True)
    async def clear_messages(self, ctx, num_messages: int):
        if num_messages <= 0:
            await ctx.send("The number of messages to be deleted must be positive.")
            return

        deleted_messages = await ctx.channel.purge(limit=num_messages + 1)

        await ctx.send(f"Deleted {len(deleted_messages) - 1} messages.")

    @command(name='kick')
    @has_permissions(kick_members=True)
    async def kick_member(self, ctx, member):
        try:
            await member.kick()
            await ctx.send(f"Kicked {member.display_name}.")
        except Exception as e:
            await ctx.send(f"Failed to kick member: {e}.")

    @command(name='ban')
    @has_permissions(ban_members=True)
    async def ban_member(self, ctx, member):
        try:
            await member.ban()
            await ctx.send(f"Banned {member.display_name}.")
        except Exception as e:
            await ctx.send(f"Failed to ban member: {e}.")

    @command(name='unban')
    @has_permissions(ban_members=True)
    async def unban_member(self, ctx, *, member):
        banned_users = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}.")
                return

        await ctx.send(f"Could not find member {member}.")


# ----------------------------------------------------------------------------
# clear_messages関数: Discordチャンネルのメッセージを削除する関数です。削除するメッセージ数を引数として取ります。
# kick_member関数: DiscordサーバーからメンバーをKickする関数です。Kick対象のメンバーを引数として取ります。
# ban_member関数: DiscordサーバーからメンバーをBanする関数です。Ban対象のメンバーを引数として取ります。
# unban_member関数: DiscordサーバーでBanされたメンバーを解除する関数です。 解除する対象のメンバー名と  # タグを一つの文字列として引数として取ります。
