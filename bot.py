import os
from dotenv import load_dotenv
import tweepy
import random
import asyncio
import aiocron

load_dotenv()

auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_CLIENT_KEY"),
    os.getenv("TWITTER_CLIENT_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET"),
)

api = tweepy.API(auth)

emojis = ["🦀", "🎈", "👗", "☕️", "🐶", "🐍", "🎛", "🎮", "💜", "🏳️‍🌈", "🚃", "🥳", "👩‍💻"]


@aiocron.crontab("*/5 * * * *")
async def replace_emoji():
    emoji = random.choice(emojis)
    print("Replacing emoji with: " + emoji)

    api.update_profile(name=f"Brooke Chalmers 🏳️‍⚧️ // {emoji}")


replace_emoji.start()


async def main():
    await asyncio.Event().wait()


asyncio.run(main())
