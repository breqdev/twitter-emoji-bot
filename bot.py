import os
from dotenv import load_dotenv

# import tweepy
import random
import asyncio
import aiocron
import requests
import datetime

load_dotenv()

est = datetime.timezone(datetime.timedelta(hours=-5))
birthday = datetime.datetime(2003, 1, 2, 0, 0, 0, 0, est)

# auth = tweepy.OAuth1UserHandler(
#     os.getenv("TWITTER_CLIENT_KEY"),
#     os.getenv("TWITTER_CLIENT_SECRET"),
#     os.getenv("TWITTER_ACCESS_TOKEN"),
#     os.getenv("TWITTER_ACCESS_SECRET"),
# )

# api = tweepy.API(auth)


session = requests.Session()
session.headers.update(Authorization=f"Bearer {os.getenv('MASTODON_ACCESS_TOKEN')}")


emojis = [
    "🏳️‍⚧️",
    "🦀",
    "🎈",
    "👗",
    "☕️",
    "🐶",
    "🎛",
    "💜",
    "🚃",
    "👩‍💻",
    "💕",
    "👾",
    "🤖",
    "🦞",
    "🔥",
    "✨",
    "💾",
    "📸",
    "♀️",
    "🏴‍☠️",
    "🌈",
    "🌆",
    "🎀",
    "🧋",
    "😈",
    "🎸",
    "💅",
]


@aiocron.crontab("*/1 * * * *")
async def replace_emoji():
    emoji = random.sample(emojis, 3)
    print(f"Replacing emoji with: {emoji}")

    name = "bronke" if random.random() > 0.95 else "brooke"
    pronouns = "she/they" if random.random() > 0.95 else "she/her"

    # display_name = name + " chalmers ⊃ " + "\u200b".join(emoji)
    display_name = name + " ⊃ {" + ", ".join(emoji) + "}"

    now = datetime.datetime.now()  # server runs in UTC

    if now.month > birthday.month or (
        now.month == birthday.month and now.day >= birthday.day
    ):
        age = now.year - birthday.year
    else:
        age = now.year - birthday.year - 1

    # api.update_profile(
    #     name=display_name,
    #     location=pronouns + ", @breq@tacobelllabs.net",
    #     description=f'{age}. 🏳️‍⚧️. tinkering with code, chips, math, music. do it all. "the cutest fucking person here" -some girl at a rave. blåhaj. @breqalt.',
    # )

    session.patch(
        "https://tacobelllabs.net/api/v1/accounts/update_credentials",
        data={
            "display_name": display_name,
            "note": f'{age}. 🏳️‍⚧️. {pronouns}. tinkering with code, chips, math, music. do it all. "the cutest fucking person here" -some girl at a rave. blåhaj.  boston & maine.',
        },
    ).raise_for_status()


asyncio.get_event_loop().run_forever()
