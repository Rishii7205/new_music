import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "10577960"))
API_HASH = getenv("API_HASH", "80fd047285f4e94ca80311928b6bb5da")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6112393507:AAG9Xl4WThe8Oq_YUSe2vC0rlqJiaG-GkDo")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kavyanewdb2023:Kavyanewdb2023@cluster0.qdp069e.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOG_ID = int(getenv("LOG_ID", "5655799578"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001759015516"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5655799578"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Raichuop07/V2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MOONLIGHT_SAGA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kavyabotsupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "c7ea1cf58c5840378c47bda546329bf8")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "f0acdf6d88784a159f2ed6adefd08901")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 60))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQCMGZMAvjl4PZ_TlqVvhXBVDPCVPzDNr2MddDeMHTYggmKAprcCZyPZDKR0EhwV_kjOIfVUfP65bUgzEgjL7TiWX6AD4PraSXyiIkiAheqL4morxF3UlhHjg08ACLih6m7TKBESofJ-s0mt-Ivm0azPXbQtC51v13_oGwUXqhPGIMwxaar0iLIjQtt7A96zMrMyqQps7i7yrs4zlL_bSEW9GwBbu7mQ06bBn15qao7nw8I2BgTK59BVArfW-KS-iEtyhqxBUxP5vibrkN4jEiTS7TcQdjL5DREBaVapHXEOMzSVbPbPzlsry1aVhNjn6FZ91SeM0La8ILMW0F13Bxn05jKgAAAAF3CtSsAA")
STRING2 = getenv("STRING_SESSION2", "BQCMGZMAdlrVrfBh_-um7-Xf7WmoG5vndorBdc9pdQyXHr8hew1MwvNK7tcUhDYXb35ZjkwaCJvULpkhkmW_U_OwRd88vU5kVw8of15-ja5dO9lrRfSJabdQhhNsb8s_KTonXZ9YAaA-RFynV41gbm-aryGReIM7CHMFBMN9ORvJOXNBxPek0CrHVDxjZJEOdfmoxmM_ov7050hVM7be9vOEQZlpa1osCg2fPDkaAfp_sTiri86Vxsv8_0k7aExShz6b0Ol4zvO_ERC36S042jJFjPjcDWNpKoXpdBx3xDETeXr7patW_Ey5qsnA4jN1pLbG89Jr2ghvlFImGvqufIsvG7jPQgAAAAF7j0dNAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/ba43f5de1ac7f8541c550.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/ba43f5de1ac7f8541c550.jpg"
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
