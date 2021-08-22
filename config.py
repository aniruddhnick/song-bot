import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", '7437591'))
    API_HASH = os.environ.get("API_HASH", "c5ab761f8df79d9c43fdc0da9defacac")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1927526017:AAHNmiTvdVaS6QXDvQTh0PiEMwJW3VszlxE
")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name with /song command")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2a35fca576aa49de77c98.jpg")
    OWNER = os.environ.get("OWNER", "sagnikoni") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
