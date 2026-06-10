# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env.local")
    load_dotenv("config.env")
except:
    pass

# Hardcoded configuration values provided by user for direct use (Heroku Config Vars will still override via getenv where applicable).
# IMPORTANT: For production/Heroku, set SESSION_STRING as a Config Var using a fresh value from @TgDevToolBot.
# The old public SESSION_STRING is expired and causes AUTH_KEY_UNREGISTERED crashes.

# Pyrogram setup
class PyroConf(object):
    API_ID = 24363932
    API_HASH = "d84176e864496c3cd2542c1a0de42c4a"
    BOT_TOKEN = "8624313001:AAF0SVVtQshRHxY3nkk-91qHsza89Q9yXEE"
    SESSION_STRING = "AQFzw5wAGGrmlTl7xzO7I6n35jW_mC8Po7dF0KLVaMNrUg4BLKBOeWG8SCqDPjLBZwS3H2Fr6VxvwZaYwNwaCpEixVfaVwDyzPXh2Jcq0L8E7GcVJZyk0-U4VCTQKJhU5C0ELjuzFEbHmqyk-LuFBtjEDsWGj8ugYK4xv1r1JfM-5Rje_bCLkwUinpstHZUVxBoh29NdlZGsKvL4ijvGfkENTY0VR3RgojYjMXQrIm1AfsPcRxecFNuoGjjwCICV_vWglQ4q91bpJdvaCdLFlbCQ25S_Y9yggJmwMkKbJPyB1qbgXWKNnk9QBRlZsaPl4Y-SpWwLMuzfJHzb3xWIHqo3oKe9MAAAAAICDJKpAQ"  # User-provided session string (hardcoded per request)
    BOT_START_TIME = time()

    MAX_CONCURRENT_DOWNLOADS = 1
    BATCH_SIZE = 1
    FLOOD_WAIT_DELAY = 10

    FORWARD_CHAT_ID = "-1003989536425"  # channel logs
    FORCE_SUB_CHANNEL = "-1003722708712"  # force channel
    OWNER_ID = 8347200447  # User ID
