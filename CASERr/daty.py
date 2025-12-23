import os
import redis
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import user, dev, call, logger

# سحب البيانات من Koyeb
API_ID = int(os.getenv("API_ID", "25761783"))
API_HASH = os.getenv("API_HASH", "7770de22ee036afb30a99d449c51f4b8")

# الاتصال بقاعدة بيانات Redis (Upstash)
REDIS_URL = os.getenv("REDIS_URL", "redis-cli --tls -u redis://default:AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE@ultimate-ferret-48101.upstash.io:6379")
r = redis.from_url(REDIS_URL, decode_responses=False)

def get_Bots():
    try:
        lst = []
        # بنخزن البوتات في مفتاح اسمه maker_bots
        for a in r.smembers("maker_bots"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

async def get_dev(bot_username):
    # بيجيب ايدي المطور من المتغيرات أو من الداتا
    owner = os.getenv("OWNER_ID")
    if owner: return int(owner)
    for x in get_Bots():
        if x[0] == bot_username: return x[1]
    return 7669264153

async def get_userbot(bot_username):
    if bot_username in user: return user[bot_username]
    for x in get_Bots():
        if x[0] == bot_username:
            ubot = Client("CASER_ASSISTANT", api_id=API_ID, api_hash=API_HASH, session_string=x[3])
            await ubot.start()
            user[bot_username] = ubot
            return ubot
    return None

async def get_call(bot_username):
    if bot_username in call: return call[bot_username]
    ubot = await get_userbot(bot_username)
    if ubot:
        calo = PyTgCalls(ubot, cache_duration=100)
        await calo.start()
        call[bot_username] = calo
        return calo
    return None

async def get_logger(bot_username):
    log_id = os.getenv("LOGGER_ID")
    if log_id: return int(log_id)
    for x in get_Bots():
        if x[0] == bot_username: return x[4]
    return None
