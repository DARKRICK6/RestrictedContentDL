# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

    if not getenv("BOT_TOKEN") or not getenv("BOT_TOKEN").count(":") == 1:
        print("Error: BOT_TOKEN must be in format '123456:abcdefghijklmnopqrstuvwxyz'")
        exit(1)

    if (
        not getenv("SESSION_STRING")
        or getenv("SESSION_STRING") == "xxxxxxxxxxxxxxxxxxxxxxx"
    ):
        print("Error: SESSION_STRING must be set with a valid string")
        exit(1)


# Pyrogram setup
class PyroConf(object):
    API_ID = int(getenv("29308940", "29308940"))
    API_HASH = getenv("666df5578043cc906ec8f25b05c2f1cb", "")
    BOT_TOKEN = getenv("8493075779:AAHs2AOHWxmcUjcP4ZIZ69_xKW0QFYWr4fw"
    SESSION_STRING = getenv("SESSION_STRING")
    BOT_START_TIME = time()
