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
    SESSION_STRING = "AQFzw5wAsGM2Rm__THrR0sSxapMOuJkDB1yvbKfDZyXwwpvyFVla0YH8HK5zYzIBKH7EiNbzTMbHW5QWWHjsiLUPooFKTfOVZjrwkzTI2ODkfODbGnJ_2AiOpiSTOeHkDT8PNYM6O6CWSQgi-HeP2xj4-FYELjb-BxEAqX2og3DJKH5QAYDCL-bJhjiAmA4pt-Il-p1y_HnBa74cdbIdp5K9fz1xjf1Er3IvU7k-OCgH2QSyAKjFHk2c1WKWfwmmLj4NBncrW_gECHeeYQPuQTeS3Y4CFKgFa4ANvH0Ncp1mF_xL45681hOs63UWXKaE_1oaIisRnES3PsyB5-3OBYLi0CfEJAAAAAHxiCu_AA"  # User-provided session string (hardcoded per request)
    BOT_START_TIME = time()

    MAX_CONCURRENT_DOWNLOADS = 1
    BATCH_SIZE = 1
    FLOOD_WAIT_DELAY = 10

    FORWARD_CHAT_ID = "-1003855725764"  # log channel
    FORCE_SUB_CHANNEL = "-1003953749241"  # force channel (bot is admin)
    OWNER_ID = 8347200447  # User ID
