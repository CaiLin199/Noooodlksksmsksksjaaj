#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "26254064")
API_HASH = config("API_HASH", "72541d6610ae7730e6135af9423b319c")
BOT_TOKEN = config("BOT_TOKEN", "7370024975:AAHA45hg0iqXvdofFi4Jlf8hfi7uV0ma-vE")
SESSION = config("SESSION", "BQGQmvAAnZC4bkzKqrzk-bQEla0eqARxttqINRfXqxzztUB0PpDtpQXGs36dYQaWREfcsfWlMr7El4NTthna1Zko4C-JMmM5nN2qBWRR-y8jLg76Qh4Co4hrOeLw2DySykY_QkUoQHVl4fTVEbgoygo3eyhiz1kTODw23hgDXKUDaCcaV5tu4QrkP9Aj903XXxQziBiX2JR67_-dvTTAikTacL12dwuiDnDccb7b2JX2xOVMy2_L74jSZamJFAZcnwaK-Gm5T55SzVU8l4s8xrsaJ8NAekag60hfPGZHZqPe2vElpp28SsToO0HVndrQ7EVv9th5iziI_Sf9uZa8EdfCcK-IeAAAAAE7s3WDAA")
FORCESUB = config("FORCESUB", "AnimeQuestX")
AUTH = config("AUTH", "5296584067")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
