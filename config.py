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
LOG_ID = int(getenv("LOG_ID", "-1001960459350"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001759015516"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5518687442"))

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
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kavyasupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))


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
STRING1 = getenv("STRING_SESSION", "BQGMcpgAKAdI_ZjyUG0NRJ6PJE3cP813OjhJFEqry2I2NehnjMNcLKb1TPfWOi29Z-vnkmaO0Uv8nVI4T7Y3r93UokvctuHXkV6PnPQGPsBQXVZdRLTtWFPwAVmnboWREUUKih6ZEVqA0C6Qz-k_4D-Hzu6jfhY3ZG9y4AqRW1gPfBjZQ4XLBRdhGqWYXv24XbsEzxNUFF9WViemrgJBBF1RJw0sU66RZVtaNoIFH33AmiID2KH9lvExWq3Efw1xXjZKS_VpdtmLFZPRdx5gHps7MDu4189P9pBxJKIu_XGlFpujQ3Uk14rB6mkCtaUDzUnsiDP9P9mct4yADiA36KW09oomVwAAAAF3CtSsAA")
STRING2 = getenv("STRING_SESSION2", "BQGMcpgAnMCbudnAfl3M7tiAanROmVGOcKWU0fVpeHpJ7BHGimChJPXTaRHc31SaUZLCOsP-v0Mg91o3TphC6EiNM7-8L5SyJwPLYUk07SlaMd_zdkwfr1_1P2Ep0XX2qVUzdDpjJBRWa-fjCFEgmqOOIuR4QFuKFMbKG9SFg9Gi-JHHet4KysV6FHihBw1o_6SraCYF81Njmh03mpIQDDiHoA3mN0W4C5ItlGsLGurff35kPD4tfevXC78ArfuY8IlAmsIzMlT8bYu-1suvydoadB9JizL43r6hHHxFyyK2JjIbvRfzS3OE8Uh1e4uIPC84x88fzYeUBjkGrbHq6M7fadPhSwAAAAF7j0dNAA")
STRING3 = getenv("STRING_SESSION3", "BQGMcpgAxCVIOB-tY4yKGYBCZbfB22vVmmQZtKnAgxU985CKfsubzxzmMA8BAi6La6yVj5HhAs_6UU05khDFoK-n-westKGjCkeVR3YeFns-Ti_bpvw4vhaZX5-zMmxVn7smMEBxYPkMN8mQLuxDyVhRSoD3vwj37FH5diPmc8XB8cB81izh0csjKZJP36Vasb6o2xnSkDogBqcXCGj9wyovbST22avq8X4mJk-6krM5bh94f5sBlAwS_n-qQTUdCM2PKzDeCjqzepzIkLpRMC9w21sgtGJIdMVbCL1bm1fBKXANiH7rxutON4novPYILfdgDfHlKm7G3fzXbkS5O7UnDWm1HwAAAAGKUy9BAA")
STRING4 = getenv("STRING_SESSION4", "BQGMcpgAoeqptwJlCVvicIdbmo6RJ6tKdMYsZtLuILTvvLGkPPxmZcF1rCSTmTmF9ru4Czpb7f-xF4vyCctx57nQ1bPagptgy9mz3H4UMZ3L3comdEhokHJjgQa0G6oh-lZq6N3b31KwWVxoxR6dXUNX8LrHYfpG7b6mKhw8Odn89swhvBt7gAnrTLh3qLcV7KqxmslP6oeUHme4EhsDbldI7SmJqHaHm1C7-PHvZko5CDJY7HVyCRozRlCZ3wHPpISI2l_8FyntVBKQxkyU-dcwFZlAo4_4vQ5F7n5l1olmpWy3oN9Ta7HtyDf5jw-purqNF_XQErVeNQ_4n8tdYDaGYGth_AAAAAFeiK6lAA")
STRING5 = getenv("STRING_SESSION5", "BQGMcpgATdB-9xfWj7XR3S0XuCwg0DrVUIK5VbdW1jty30ODakKtVwdnDYGn_SPN6h8CkxLHiZdElxppWFJba8bX-jpDYOKia4cF6liX3A2eFiPCwW0KAJ6-AfgssytAQeia0PZTEUKEJI0q5pKWyCJ-K-_G--nTjJi-k8Vh0i8e-_KwYMVp0i1P02medXTe9TyiBFSPGDGoqLg6JhiVPEAul6DfWafYOitZcSaCZjYos9J3Oh3kuz9YArzCCj1m4qS_OMO-h09cD8MHhIJMjaisJQ0ToRhQcH8P-wdLoypgM7MC-iqYaw9nX9udNftqZDLOu4scF73fvDMHqWBYlT5JNqXalQAAAAF9gW10AA")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/931635325e67b1b348ab2.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/931635325e67b1b348ab2.jpg"
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
