import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/2d6bd14d1d3a84240b738.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "THE_TVA")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "CatKing_ext")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/mpb00121/vc_bot")
OWNER_NAME = getenv("OWNER_NAME", "Telecat_X")
PROJECT_NAME = getenv("PROJECT_NAME", "VoiceChat_Song_bot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "25"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
START_IMG = getenv("START_IMG","https://te.legra.ph/file/1b4095a3cd864970fb26b.jpg")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2047505238").split()))
