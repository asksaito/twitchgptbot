import os
from twitchio.ext import commands

# 環境変数から設定を読み込む
channel_name = os.environ["TWITCH_CHANNEL_NAME"]
bot_name = os.environ["TWITCH_BOT_NAME"]
oauth_token = os.environ["TWITCH_OAUTH_TOKEN"]

# ボットのインスタンスを作成
bot = commands.Bot(
    token=oauth_token,
    nick=bot_name,
    prefix="!",
    initial_channels=[channel_name],
)

# シンプルなコマンドの例
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"こんにちは、{ctx.author.name}さん！")

# ボットを実行
if __name__ == "__main__":
    print("twitch_gpt_bot is running...")
    bot.run()
