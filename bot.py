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

emojis = [
    "🏳️‍⚧️",
    "🦀",
    "🎈",
    "👗",
    "☕️",
    "🐶",
    "🐍",
    "🎛",
    "🎮",
    "💜",
    "🏳️‍🌈",
    "🚃",
    "🥳",
    "👩‍💻",
    "💕",
    "👾",
    "🤖",
    "🐕",
    "🦞",
    "🚨",
    "🔥",
    "⚡",
    "✨",
    "🎤",
    "💾",
    "📸",
    "♀️",
    "⚠️",
    "🏴‍☠️",
    "🆒",
    "🌈",
    "🌆",
    "🎀",
    "🧋",
    "😈",
    "⚛️",
    "🎸",
    "⚔️",
    "💅",
    "🐾",
    "⚧️",
]


@aiocron.crontab("*/1 * * * *")
async def replace_emoji():
    emoji = random.sample(emojis, 3)
    print(f"Replacing emoji with: {emoji}")

    name = "bronke" if random.random() > 0.95 else "brooke"
    pronouns = "she/they" if random.random() > 0.95 else "she/her"

    api.update_profile(
        name=name + " chalmers ⊃ {" + ", ".join(emoji) + "}",
        location=f"{pronouns} - boston & maine",
    )


asyncio.get_event_loop().run_forever()
