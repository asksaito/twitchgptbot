import os
from twitchio.ext import commands
from chatgpt import call_chatgpt

# Load environment variables
channel_name = os.environ["TWITCH_CHANNEL_NAME"]
oauth_token = os.environ["TWITCH_OAUTH_TOKEN"]

# Create Twitch Bot instance
bot = commands.Bot(
    token=oauth_token,
    prefix="!",
    initial_channels=[channel_name],
)

# Sample command
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hello!! {ctx.author.name}")

# ChatGPT command
@bot.command(name="chatgpt")
async def chatgpt(ctx):
    await ctx.send("Now requesting to ChatGPT..")

    # Call ChatGPT API
    response = call_chatgpt(ctx.message.content)

    # Send ChatGPT response
    await ctx.send(response)

# Execute Bot
if __name__ == "__main__":
    print("twitch_gpt_bot is running...")
    bot.run()
    print("twitch_gpt_bot is stopped.")
