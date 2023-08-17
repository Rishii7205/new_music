import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "10577960"))
API_HASH = getenv("API_HASH", "80fd047285f4e94ca80311928b6bb5da")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5609544885:AAGr5IeBwlVCyOlsHwA7FRbIA_Tl8geyVPE")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Sanki:Fallen@cluster0.revk6zx.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001840292554"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6157453615))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FallenSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "e76f857641b44a169ba86a735b1286fa")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "53308d5b31fd47b0a6e506e3e110d6bb")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQHBzKIAKvPnInD2uHYpQuE9X_bJs5bXdFGFe6mZ8w97Ds2A3A86-8U_wDd07nlBq9Sh1tzsscAgz0QSNZE4gi87xfMWmn_T9gGWsWyrzM-Vp78EF4q7QedeCX5_iz-2J-BW6KE5P06bucpxS5t_dSaO2jMPHTnx5dM_jEap3xDynkRMzT1LQl5UDZ_bdxZgbxLTRWfpyah6OxRpbuXhMAjDm0-6d8fPJdpZRELYtMfooT_hhjlWVNiBVzAnLg8ED3Xd8usP7_OfQYIrp3lXJdrvtsc9tbwUoZi005iwAHBJSZYWKZNikZUld4O8pD3JID2Sv0U3SUipZ5RHlspqg2o2Zqj6HgAAAAFo3ALWAA")
STRING2 = getenv("STRING_SESSION2", "AQHBzKIAlsRe0MoteGZV8nFZIZUMX28Rn9wr-opj15xYGj22RNVxStwFRSa-jnuTOmCg0jBNPs58mShN6folbd30M2Py96Rx3SfEVutykLTkreiMZmmlKn5A_Jap-MjhENzfMXyOY2upCnO49cOdMwl9LukAFtgcRQICoIKD_gM3Y1mf2jhspgLl6Eqr7Y9_KjcfOXs-9SJ5M9GdJI49ip_cE5mpxb7ODk6LQPnMYiTc0px3JHCjHau1FGNjkmZL61eYymVn8j3NrBVKorK8r8RGoYnHRblDaGB9TlinSgmYlUuCvfqayz1e9-zCP-JCaqkIxfQqk4WJmx4tG775vU-MiRjGBQAAAAF80Y4zAA")
STRING3 = getenv("STRING_SESSION3", "BQHBzKIAmHtD2xPmFjXGdw91Fjt9tAQFYG2a1ti-dOngEccpEzvPmnaHKeo1RCD_vjH6rRSyjU2Jaf995tD4i-sNlcN_9Unq6m2nsKPlLUqX3pb9kVoRzDfhmKPHaPXze8EgOq_favV-x3pi7kPLZyq98PUWGTsN1omYjFELT5xxAMie7dMcJQgqoJasXnNWjmRDD3lkEpIT_A3NkaieIyeMryeAzS_gYYVKCjYNnoJ-QI-RnCcrMHHVgcizOWneOmjMemgh_HYst6GTiNW-I66SJfRkR7DNgesifLbj_dijAAHe8mlh6D3l57fwamM2mJyLiyOweLqsC5OTouiotSPCxT93_QAAAAFsYwxbAA")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/25efe6aa029c6baea73ea.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
