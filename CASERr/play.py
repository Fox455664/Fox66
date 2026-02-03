import os
import re
import asyncio
import random
import aiohttp
import aiofiles
import requests
import yt_dlp
import numpy as np
from datetime import datetime, timedelta
from typing import Union
from io import BytesIO

from pyrogram import Client, filters
from pyrogram.errors import (ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant, FloodWait)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputPeerChannel, InputPeerChat

from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (NoActiveGroupCall, TelegramServerError, AlreadyJoinedError)
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls.types import AudioQuality, VideoQuality

from youtubesearchpython.__future__ import VideosSearch
from youtube_search import YoutubeSearch
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from unidecode import unidecode

# استيراد الإعدادات والقواعد
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, devgroup, devuser, group, casery, johned, photosource, muusiic, suorce

# --- متغيرات القائمة ---
playlist = {}
hossamm = [] # لتخزين مسار الملف الحالي للتقديم والتأخير
vidd = {}
namecha = {}
user_mentio = {}
thu = {}
phot = {}
playing = {}
Music = {}

# --- وظائف مساعدة للصورة ---
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

def make_col():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def truncate(text):
    words = text.split(" ")
    text1, text2 = "", ""
    for i in words:
        if len(text1) + len(i) < 30: text1 += " " + i
        elif len(text2) + len(i) < 30: text2 += " " + i
    return [text1.strip(), text2.strip()]

# --- توليد صورة التشغيل ---
async def gen_bot_caesar(client, bot_username, OWNER_ID, CASER, message, videoid):
    if os.path.isfile(f"photos/{videoid}_{bot_username}.jpg"):
        return f"photos/{videoid}_{bot_username}.jpg"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            title = result.get("title", "Unsupported Title")
            duration = result.get("duration", "Unknown")
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            views = result.get("viewCount", {}).get("short", "Unknown")

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()
        
        youtube = Image.open(f"thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        background = image1.convert("RGBA").filter(filter=ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        image2 = enhancer.enhance(0.6)
        
        # إضافة لمسات السورس
        draw = ImageDraw.Draw(image2)
        font2 = ImageFont.truetype("font.ttf", 70)
        draw.text((350, 10), f"{suorce}", fill="white", font=font2)
        
        image2.convert("RGB").save(f"photos/{videoid}_{bot_username}.jpg")
        os.remove(f"thumb{videoid}.png")
        return f"photos/{videoid}_{bot_username}.jpg"
    except Exception as e:
        print(f"Image Gen Error: {e}")
        return photosource

# --- وظيفة الانضمام وفتح الكول تلقائياً ---
async def join_call(bot_username, OWNER_ID, client, message, audio_file, group_id, vid, user_mention, photo, thum, namechat): 
    userbot = await get_userbot(bot_username)
    hoss = await get_call(bot_username)    
    
    file_path = audio_file
    # إعدادات الجودة الفائقة
    audio_stream_quality = AudioQuality.STUDIO
    video_stream_quality = VideoQuality.FHD
    
    stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
    
    try:
        await hoss.join_group_call(group_id, stream, stream_type=StreamType().pulse_stream)
        hossamm.clear()
        hossamm.append(file_path)
        return True
    except NoActiveGroupCall:
        # الحساب المساعد يفتح الكول
        try:
            await userbot.invoke(CreateGroupCall(
                peer=await userbot.resolve_peer(group_id),
                random_id=int(os.urandom(4).hex(), 16)
            ))
            await asyncio.sleep(2)
            await hoss.join_group_call(group_id, stream, stream_type=StreamType().pulse_stream)
            hossamm.clear()
            hossamm.append(file_path)
            return True
        except Exception:
            await message.reply_text("❌ الحساب المساعد يحتاج صلاحية (إدارة المكالمات) لفتح الكول تلقائياً.")
            return False
    except AlreadyJoinedError:
        # إضافة للقائمة إذا كان البوت شغال فعلاً
        playlist.setdefault(group_id, []).append(file_path)
        vidd.setdefault(group_id, []).append(vid)
        thu.setdefault(group_id, []).append(thum)
        phot.setdefault(group_id, []).append(photo)
        user_mentio.setdefault(group_id, []).append(user_mention)
        namecha.setdefault(group_id, []).append(namechat)
        await message.reply_text(f"⏳ تمت إضافة **{thum}** إلى القائمة بالترتيب: {len(playlist[group_id])}")
        return False
    except Exception as e:
        print(f"Join Error: {e}")
        return False

# --- أوامر التقديم والتاخير (10 ثواني) ---
@Client.on_message(filters.command(["تقديم", "قدام"], "") & filters.group)
async def seek_forward(client, message):
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    if not hossamm: return await message.reply_text("مفيش حاجة شغالة حالياً!")
    try:
        await hoss.change_stream(message.chat.id, AudioVideoPiped(hossamm[0], additional_ffmpeg_parameters="-ss 00:00:10", audio_parameters=AudioQuality.STUDIO, video_parameters=VideoQuality.FHD))
        await message.reply_text("✅ تم التقديم 10 ثواني")
    except: pass

@Client.on_message(filters.command(["تاخير", "ورا"], "") & filters.group)
async def seek_back(client, message):
    await message.reply_text("⏳ ميزة التأخير تتطلب إعادة تحميل الملف، سيتم توفيرها في التحديث القادم.")

# --- أمر التشغيل الرئيسي (شغل / فيديو) ---
@Client.on_message(filters.command(["شغل", "تشغيل", "فيد", "فديو", "/play", "/vplay"], "") & filters.group)
async def play_handler(client, message):
    if await johned(client, message): return
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    group_id = message.chat.id
    
    if message.reply_to_message:
        vid = True if ("v" in message.command[0] or "ف" in message.command[0]) else False
        m = await message.reply_text("🔄 جاري معالجة الرد...")
        audio_file = await message.reply_to_message.download()
        await join_call(bot_username, OWNER_ID, client, message, audio_file, group_id, vid, message.from_user.mention, photosource, "ملف مستلم", message.chat.title)
        await m.delete()
        return

    try:
        text = message.text.split(None, 1)[1]
    except:
        return await message.reply_text("❌ ارسل (شغل + اسم الاغنية)")

    mm = await message.reply_text("🔎 جاري البحث والتحميل...")
    
    # البحث
    search = VideosSearch(text, limit=1)
    res = (await search.next())["result"][0]
    videoid = res["id"]
    thum = res["title"]
    vid = True if ("v" in message.command[0] or "ف" in message.command[0]) else False
    
    # تحميل
    link = f"https://www.youtube.com/watch?v={videoid}"
    audio_file = await download_yt(bot_username, link, vid)
    
    if audio_file:
        photo = await gen_bot_caesar(client, bot_username, OWNER_ID, "Owner", message, videoid)
        await join_call(bot_username, OWNER_ID, client, message, audio_file, group_id, vid, message.from_user.mention, photo, thum, message.chat.title)
    
    await mm.delete()

async def download_yt(bot_username, link, video=False):
    # اسم ملف الكوكيز الذي قمت بحفظه
    cookie_file = "cookies/cookies2.txt"
    
    # تحديد الصيغة
    fmt = "bestvideo+bestaudio/best" if video else "bestaudio"
    
    # بناء الأمر مع إضافة الكوكيز
    command = [
        "yt-dlp",
        "--cookies", cookie_file,
        "-g",
        "-f", fmt,
        link
    ]

    proc = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    
    stdout, stderr = await proc.communicate()
    
    if stdout:
        return stdout.decode().strip()
    
    # طباعة الخطأ في التيرمينال للمساعدة في حل المشكلة إذا تكررت
    if stderr:
        print(f"Error downloading: {stderr.decode()}")
        
    return None

# --- التحكم (ايقاف، كمل، اسكت) ---
@Client.on_message(filters.command(["اسكت", "ايقاف", "انهاء", "stop"], "") & filters.group)
async def stop_music(client, message):
    hoss = await get_call(client.me.username)
    try:
        playlist[message.chat.id].clear()
        await hoss.leave_group_call(message.chat.id)
        await message.reply_text("✅ تم إنهاء التشغيل وسكتنا خلاص 🤐")
    except:
        await message.reply_text("❌ مفيش حاجة شغالة أصلاً!")

@Client.on_message(filters.command(["توقف", "وقف", "pause"], "") & filters.group)
async def pause_music(client, message):
    hoss = await get_call(client.me.username)
    await hoss.pause_stream(message.chat.id)
    await message.reply_text("⏸ تم إيقاف التشغيل مؤقتاً")

@Client.on_message(filters.command(["كمل", "استكمال", "resume"], "") & filters.group)
async def resume_music(client, message):
    hoss = await get_call(client.me.username)
    await hoss.resume_stream(message.chat.id)
    await message.reply_text("▶️ تم استكمال التشغيل")

# --- نهاية الملف ---
