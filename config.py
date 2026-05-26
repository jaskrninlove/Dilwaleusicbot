from os import getenv
from dotenv import load_dotenv
import random

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 0))
        self.API_HASH = getenv("API_HASH")

        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.MONGO_URL = getenv("MONGO_URL")

        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = int(getenv("OWNER_ID", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/elysiiannetwork")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+jl7btCRGFGgwNGRl")

        self.API_URL = getenv("API_URL", "https://pvtz.nexgenbots.xyz")
        self.VIDEO_API_URL = getenv("VIDEO_API_URL", "https://api.video.nexgenbots.xyz")
        self.API_KEY = getenv("API_KEY", None) # Get this value from https://console.nexgenbots.xyz

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://i.pinimg.com/736x/02/66/b4/0266b47c68fb482f3a7ac141011f5e89.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://i.pinimg.com/736x/84/b4/c2/84b4c2989f097ea8c37a6a0a5fc72bf9.jpg")
        self.START_IMGS = [
        "https://i.pinimg.com/736x/04/f5/de/04f5deb166d984718f410b723e4ad301.jpg",
        "https://i.pinimg.com/736x/b7/8b/89/b78b89c64f56da640dd3232b0652cf9b.jpg",
        "https://i.pinimg.com/736x/39/63/45/396345be53a4d7d4d26141f2d449cdf0.jpg",
        "https://i.pinimg.com/736x/b4/80/76/b480762f8109d74561a9da817c1e3ed4.jpg",
        "https://i.pinimg.com/736x/69/ab/c7/69abc749ef98216412a37162447b4c1d.jpg",
        "https://i.pinimg.com/736x/48/2c/e8/482ce8bb1c0e19e98ca508e9aff27006.jpg",
        "https://i.pinimg.com/736x/49/a8/ec/49a8ec205e2a213ccd0404bffe7afc86.jpg"

        ]     

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
