import os
import asyncio
import random
import aiohttp
import aiofiles
import yt_dlp
from youtubesearchpython.__future__ import VideosSearch
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (NoActiveGroupCall, AlreadyJoinedError)
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types import AudioQuality, VideoQuality

# استيراد الإعدادات والقواعد (تأكد أن هذه الملفات موجودة لديك)
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev
from CASERr.CASERr import johned, photosource, suorce

# --- متغيرات القائمة ---
playlist = {}
hossamm = [] 
vidd = {}
namecha = {}
user_mentio = {}
thu = {}
phot = {}

# تأكد من وجود مجلد الصور
if not os.path.isdir("photos"):
    os.makedirs("photos")

# --- وظائف مساعدة للصورة ---
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

# --- توليد صورة التشغيل ---
async def gen_bot_caesar(client, bot_username, OWNER_ID, CASER, message, videoid):
    # إذا الصورة موجودة مسبقاً
    if os.path.isfile(f"photos/{videoid}_{bot_username}.jpg"):
        return f"photos/{videoid}_{bot_username}.jpg"
    
    try:
        # رابط الفيديو لجلب الصورة
        url = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(url, limit=1)
        res = (await results.next())["result"][0]
        thumbnail = res["thumbnails"][0]["url"].split("?")[0]

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
        
        # إضافة اسم السورس
        draw = ImageDraw.Draw(image2)
        # تأكد من وجود ملف الخط font.ttf في مجلد البوت أو غير المسار
        try:
            font2 = ImageFont.truetype("font.ttf", 70)
            draw.text((350, 10), f"{suorce}", fill="white", font=font2)
        except:
            pass # لو الخط مش موجود مش مشكلة
        
        final_path = f"photos/{videoid}_{bot_username}.jpg"
        image2.convert("RGB").save(final_path)
        
        if os.path.isfile(f"thumb{videoid}.png"):
            os.remove(f"thumb{videoid}.png")
            
        return final_path

    except Exception as e:
        print(f"Image Gen Error: {e}")
        # في حالة الفشل، نرجع صورة افتراضية لتجنب خطأ NoneType
        return photosource

# --- وظيفة الانضمام وفتح الكول تلقائياً ---
async def join_call(bot_username, OWNER_ID, client, message, audio_file, group_id, vid, user_mention, photo, thum, namechat): 
    userbot = await get_userbot(bot_username)
    hoss = await get_call(bot_username)    
    
    # تأكد أن الصورة ليست None
    if not photo:
        photo = photosource

    file_path = audio_file
    audio_stream_quality = AudioQuality.STUDIO
    video_stream_quality = VideoQuality.FHD
    
    stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
    
    try:
        await hoss.join_group_call(group_id, stream, stream_type=StreamType().pulse_stream)
        hossamm.clear()
        hossamm.append(file_path)
        return True
    except NoActiveGroupCall:
        try:
            from pyrogram.raw.functions.phone import CreateGroupCall
            await userbot.invoke(CreateGroupCall(
                peer=await userbot.resolve_peer(group_id),
                random_id=int(os.urandom(4).hex(), 16)
            ))
            await asyncio.sleep(2)
            await hoss.join_group_call(group_id, stream, stream_type=StreamType().pulse_stream)
            hossamm.clear()
            hossamm.append(file_path)
            return True
        except Exception as e:
            await message.reply_text(f"❌ خطأ في فتح الكول: {e}")
            return False
    except AlreadyJoinedError:
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

# --- الأوامر ---
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
    
    try:
        # البحث
        search = VideosSearch(text, limit=1)
        # هنا سيحدث الخطأ إذا لم يتم تثبيت نسخة httpx القديمة
        res = (await search.next())["result"][0]
        videoid = res["id"]
        thum = res["title"]
        vid = True if ("v" in message.command[0] or "ف" in message.command[0]) else False
        
        # تحميل
        link = f"https://www.youtube.com/watch?v={videoid}"
        audio_file = await download_yt(bot_username, link, vid)
        
        if audio_file:
            photo = await gen_bot_caesar(client, bot_username, OWNER_ID, "Owner", message, videoid)
            # فحص إضافي للتأكد من الصورة
            if not photo or not os.path.exists(photo):
                photo = photosource
                
            await join_call(bot_username, OWNER_ID, client, message, audio_file, group_id, vid, message.from_user.mention, photo, thum, message.chat.title)
        else:
            await message.reply_text("❌ فشل التحميل.")
            
    except Exception as e:
        await message.reply_text(f"❌ حدث خطأ: {e}")
        print(f"Play Error: {e}")
    
    await mm.delete()

async def download_yt(bot_username, link, video=False):
    # استخدام cookies لضمان التحميل من يوتيوب
    cookies_path = "cookies.txt" if os.path.exists("cookies.txt") else None
    
    opts = [
        "yt-dlp",
        "-g",
        "-f", "bestvideo+bestaudio/best" if video else "bestaudio",
        link
    ]
    if cookies_path:
        opts.extend(["--cookies", cookies_path])

    proc = await asyncio.create_subprocess_exec(
        *opts,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, _ = await proc.communicate()
    if stdout:
        return stdout.decode().strip()
    return None

# --- التحكم ---
@Client.on_message(filters.command(["اسكت", "ايقاف", "انهاء", "stop"], "") & filters.group)
async def stop_music(client, message):
    hoss = await get_call(client.me.username)
    try:
        if message.chat.id in playlist:
            playlist[message.chat.id].clear()
        await hoss.leave_group_call(message.chat.id)
        await message.reply_text("✅ تم إنهاء التشغيل.")
    except:
        await message.reply_text("❌ البوت غير مشغل أصلاً.")

@Client.on_message(filters.command(["توقف", "وقف", "pause"], "") & filters.group)
async def pause_music(client, message):
    hoss = await get_call(client.me.username)
    try:
        await hoss.pause_stream(message.chat.id)
        await message.reply_text("⏸ تم الإيقاف مؤقتاً.")
    except:
        pass

@Client.on_message(filters.command(["كمل", "استكمال", "resume"], "") & filters.group)
async def resume_music(client, message):
    hoss = await get_call(client.me.username)
    try:
        await hoss.resume_stream(message.chat.id)
        await message.reply_text("▶️ تم الاستكمال.")
    except:
        pass
