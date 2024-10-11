# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24648630"))
API_HASH = getenv("API_HASH", "2fb7a8358803a958d6993e73a5da136d")
BOT_TOKEN = getenv("BOT_TOKEN", "7260141871:AAFxJ538hnVqfu3DqelIg6JfsiW1ZwsAhnQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7704179769").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://PihuMusic:PihuMusic@cluster0.w3eiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002332668328")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001573605549"))
