import os
from twitchio.ext import commands
from chatgpt import call_chatgpt

# 環境変数から設定を読み込む
channel_name = os.environ["TWITCH_CHANNEL_NAME"]
oauth_token = os.environ["TWITCH_OAUTH_TOKEN"]

# ボットのインスタンスを作成
bot = commands.Bot(
    token=oauth_token,
    prefix="!",
    initial_channels=[channel_name],
)

# シンプルなコマンドの例
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hello!! {ctx.author.name}")

@bot.command(name="chatgpt")
async def chatgpt(ctx):
    await ctx.send("Now requesting to ChatGPT..")

    # Call ChatGPT API
    response = call_chatgpt(ctx.message.content)

    # Send ChatGPT response
    await ctx.send(response)

# ボットを実行
if __name__ == "__main__":
    print("twitch_gpt_bot is running...")
    bot.run()
