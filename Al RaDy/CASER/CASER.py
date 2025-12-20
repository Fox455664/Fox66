import os
import pyrogram
import redis, re
import asyncio
from pyrogram import Client, idle
from pyrogram import Client as app
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyromod import listen
from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, ChatPrivileges
from pyrogram.enums import ChatType
import asyncio
import random
from bot import DEVS, DEVSs
from bot import bot_id as hos_id, lolo
from CASERr.play import Call
from CASERr.hossam import mutegdv2d
from CASERr.CASERr import photo_responses
from CASERr.azan import azan, azkar, azkar_chatt, nday_catt
from config import user as usr, dev, call, logger, logger_mode, botname, appp
from casery import caes, casery, group, source, photosource, caserid, ch, OWNER 


r = redis.Redis(
    host="127.0.0.1",
    port=6379,)

API_ID = int("24722068")
API_HASH = "72feca3ed88891eeff3852e20817cdca"
Bots = []
Musi = []
CASER = [] 
off =True
@app.on_message(filters.private)
async def me(client, message):
   if off:
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
     return await message.reply_text(f"الصانع معطل تواصل مع المطور السورس {OWNER} \n  @{casery}")
   try:
      await client.get_chat_member(ch, message.from_user.id)
   except:
      return await message.reply_text(f"يجب ان تشترك ف قناة السورس أولا \n https://t.me/{ch}")
   message.continue_propagation()

welcome_enabled = True

@Client.on_chat_member_updated()
async def welcome(client, chat_member_updated):
     if not welcome_enabled:
         return    
     if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
         kicked_by = chat_member_updated.new_chat_member.restricted_by
         user = chat_member_updated.new_chat_member.user        
         if kicked_by is not None and kicked_by.is_self:
             messagee = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
         else:
             if kicked_by is not None:
                 message = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                 try:
                     await lolo.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                 except Exception as e:
                     message += f"\n\nعذرًا، لم استطع حظر الإداري بسبب: "
             else:
                 message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"  
         await lolo.send_message(chat_member_updated.chat.id, message)   

@app.on_message(filters.command(["《السورس》"], ""))
async def alivehi(client: Client, message):
    if message.from_user.username in CASER:
        return
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس ⚡", url=f"{source}")]])
    await message.reply_photo(photo=photosource, caption="", reply_markup=keyboard)
    
@app.on_message(filters.command(["《مطور السورس》"], ""))
async def caesar(client: Client, message):
    if message.from_user.username in CASER:
        return
    user = await client.get_chat(chat_id=f"{casery}")
    name = user.first_name
    username = user.username 
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    await message.reply_photo(photo=photo, caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))

@app.on_message(filters.command(["《صنع بوت》"], ""))
async def cae5465sar(client: Client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        if message.from_user.username in CASER:
            return        
        for x in get_Bots():
            if x[1] == message.from_user.id:
                return await message.reply_text("لقد قمت بصنع بوت من قبل.")
        if len(get_Bots()) >= 10:
            return await message.reply_text("الصانع مكتمل يحبيبي 😂♥")
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("نعم لدي", callback_data="hossam1"), InlineKeyboardButton("ليس لدي", callback_data="CASER1")]])
    h = await message.reply_text("اهلا بك في صانع بوتات الميوزك ⚡🎵\nهل لديك جلسه حساب مساعد؟\nاختر بالازرار بالاسفل", reply_markup=keyboard)
    await asyncio.sleep(120)
    await h.delete()

@app.on_callback_query(filters.regex(pattern=r"^(CASER1|hossam1)$"))
async def admin_risghts(client: Client, CallbackQuery):
   command = CallbackQuery.matches[0].group(1)
   chat_id = CallbackQuery.message.chat.id
   if command == "CASER1":
    blal = await client.ask(chat_id, "ارسل رقم الحساب المساعد بكود الدوله \n مثلا: \n مصر:  +20 \n +201010084002 او استخراج الجلسه من هذا البوت @GaLsaT_BoT", timeout=200)
    hossahm = blal.text
    await CallbackQuery.message.reply_text("انتظر جاري ارسال الكود")
    cliehnt = Client(name="hfhg", api_id=API_ID, api_hash=API_HASH, in_memory=True)
    await cliehnt.connect()
    try:
        code = await cliehnt.send_code(hossahm)
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return
    lolo = await client.ask(chat_id, "تم ارسال الكود الي الحساب المساعد قم بارسال الكود المكون من 5 ارقم مبين كل رقم مسافه \n مثلا : \n 1 2 3 4 5", timeout=200)
    hoam = lolo.text  
    try:
        await cliehnt.sign_in(hossahm, code.phone_code_hash, hoam)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        await CallbackQuery.message.reply_text("الكود غير صحيح او انتهي صلاحيه الكود")
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        await CallbackQuery.message.reply_text("الكود غير صحيح او انتهي صلاحيه الكود")
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        mmh = await client.ask(chat_id, "الحساب محمي بكلمه سر ارسل كلمه السر الان (رمز التحقق)", timeout=200)
        await asyncio.sleep(3)
        hm = mmh.text
        try:
            await cliehnt.check_password(password=hm)
            string_session = await cliehnt.export_session_string()
        except:
            await CallbackQuery.message.reply_text("كلمه السر غير صحيحه جرب مره اخرى")
            return  
    else:
        string_session = await cliehnt.export_session_string()
    await cliehnt.disconnect()
    ahsk = await client.ask(chat_id, "ارسل توكن البوت الذى تم استخراجه من بوت فاذر @BotFather", timeout=200)
    await asyncio.sleep(3)
    TOKEN = ahsk.text 
    SESSION = string_session
    Dev = CallbackQuery.message.chat.id    
    if CallbackQuery.from_user.username in DEVS:
        ahjusk = await client.ask(chat_id, "ارسل ايدي المطور", timeout=200)
        await asyncio.sleep(3)
        try:
            Dev = int(ahjusk.text)
        except:
            return await CallbackQuery.message.reply_text("قم بارسال الايدي بشكل صحيح")   
    try:
      bot = Client("hossam", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
      await bot.start()
    except Exception as es:
      return await CallbackQuery.message.reply_text("**التوكن غير صحيح 🚦**")
    bot_i = await bot.get_me()
    CASR = bot_i.username
    CAGHSR = bot_i.first_name
    logger = CallbackQuery.from_user.id
    try:
       user = Client("CASER", api_id=API_ID, api_hash=API_HASH, session_string=SESSION, in_memory=True)       
       await user.start()
    except:
       await bot.stop()
       return await CallbackQuery.message.reply_text(f"**كود الجلسه غير صالح ⚡**")
    id = CallbackQuery.from_user.username
    await bot.stop()
    await user.stop()
    for x in get_Bots():
        if x[0] == CASR:
            return await CallbackQuery.message.reply_text("لقد قمت بصنع هذا البوت من قبل . ")
    oo = [CASR, Dev, TOKEN, SESSION, logger]
    add_Bots(oo)    
    await CallbackQuery.message.reply_text(f"✨ تم تنصيب بوت بنجاح \nيوزر البوت : @{CASR}\n\n بواسطة @{id}\nتوكن البوت :`{TOKEN}`\nجلسه الحساب : `{SESSION}`")
    await client.send_message(chat_id=caserid, text=f"✨ تم تنصيب بوت بنجاح \nيوزر البوت : @{CASR}\n\n بواسطة @{id}\nتوكن البوت :`{TOKEN}`\nجلسه الحساب : `{SESSION}`")   
    try:
     await start_bot(client, CallbackQuery)
    except:
     pass
   if command == "hossam1":
    ahsufbsk = await client.ask(chat_id, "حسنا قم بالرسال الجلسه ف حاله عدم وجود استخرج الجلسه من هنا @GaLsaT_BoT", timeout=200)
    await asyncio.sleep(3)
    SESSION = ahsufbsk.text
    as5k = await client.ask(chat_id, "ارسل توكن البوت الان وفى حاله عدم وجود توكن استخرج توكن من هنا @BotFather", timeout=200)
    await asyncio.sleep(3)
    TOKEN = as5k.text         
    Dev = CallbackQuery.message.chat.id    
    if CallbackQuery.from_user.username in DEVS:
        ahjusk = await client.ask(chat_id, "ارسل ايدي المطور", timeout=200)
        try:
            Dev = int(ahjusk.text)
        except:
            return await CallbackQuery.message.reply_text("قم بارسال الايدي بشكل صحيح")   
    try:
      bot = Client("hossam", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
      await bot.start()
    except Exception as es:
      return await CallbackQuery.message.reply_text("**التوكن غير صحيح 🚦**")
    bot_i = await bot.get_me()
    CASR = bot_i.username
    CAGHSR = bot_i.first_name
    logger = CallbackQuery.from_user.id
    try:
       user = Client("CASER", api_id=API_ID, api_hash=API_HASH, session_string=SESSION, in_memory=True)       
       await user.start()
    except:
       await bot.stop()
       return await CallbackQuery.message.reply_text(f"**كود الجلسه غير صالح استخرج جلسه جديده من هنا @BotFather**")
    id = CallbackQuery.from_user.username
    await bot.stop()
    await user.stop()
    for x in get_Bots():
        if x[0] == CASR:
            return await CallbackQuery.message.reply_text("لقد قمت بصنع هذا البوت من قبل . ")
    oo = [CASR, Dev, TOKEN, SESSION, logger]
    add_Bots(oo)    
    await CallbackQuery.message.reply_text(f"✨ تم تنصيب بوت بنجاح \nيوزر البوت : @{CASR}\n\n بواسطة @{id}\nتوكن البوت :`{TOKEN}`\nجلسه الحساب : `{SESSION}`")
    await client.send_message(chat_id=caserid, text=f"✨ تم تنصيب بوت بنجاح \nيوزر البوت : @{CASR}\n\n بواسطة @{id}\nتوكن البوت :`{TOKEN}`\nجلسه الحساب : `{SESSION}`")   
    try:
     await start_bot(client, CallbackQuery)
    except:
     pass
    
@app.on_message(filters.command(["《تفعيل المجاني》", "《تعطيل المجاني》"], "") & filters.private)
async def onoff(client, message):
  if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
    return
  global off
  if message.text == "《تفعيل المجاني》":
    off = None
    return await message.reply_text("تم تفعيل المجاني بنجاح .")
  else:
    off = True
    await message.reply_text("تم تعطيل المجاني بنجاح .")

async def start_bot(client, message):
    o = 0
    for x in get_Bots():
        try:
            bot_username = x[0]
            if bot_username not in Musi:
                dev_id = x[1]
                TOKEN = x[2]
                SESSION = x[3]
                logg = x[4]
                bot = Client("CASER", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True,  plugins=dict(root="CASERr"))
                user = Client("CASER", api_id=API_ID, api_hash=API_HASH, session_string=SESSION, in_memory=True)
                await bot.start()
                await user.start()
                await Call(bot_username)
                Musi.append(bot_username)
                appp[bot_username] = bot
                usr[bot_username] = user
                dev[bot_username] = dev_id
                logger[bot_username] = logg
                photo_responses[bot_username] = False
                await bot.send_message(dev_id, "**تم تشغيل البوت عزيزي المطور ✨♥**")
                asyncio.create_task(azkar(bot_username))
                asyncio.create_task(azkar_chatt(bot_username))
                asyncio.create_task(nday_catt(bot_username))
                asyncio.create_task(mutegdv2d(bot_username))
                asyncio.create_task(azan(bot_username))
        except Exception as e:
            await message.reply_text(f"**حدث خطا في تشغيل هذا البوت: @{bot_username}** \nالخطا {e} ")
     
@app.on_message(filters.command("تشغيل جميع البوتات", ""))
async def botzbjbbojbfbvfhmbie(client, message):
  if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
   return
  await message.reply_text("**جاري التشغيل انتظر**")
  try:
   await start_bot(client, message)
   await message.reply_text(f"**تم تشغيل جميع البوتات بنجاح ✨♥**")
  except:
   pass
    
@app.on_message(filters.command("رفع البوتات", ""))
async def botzbjhfhfbbojfhmbie(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    if message.reply_to_message:
        if message.reply_to_message.document.file_name.endswith("txt"):
            wait = await message.reply("• انتظر قليلا ..", quote=True)
            await message.reply_to_message.download("./Bots.txt")                
            try:
                file = open("Bots.txt", "r").readlines()
            except FileNotFoundError:
                await message.reply("حدث خطأ أثناء فتح الملف.", quote=True)
                return                    
            for line in file:
                bots = line.strip()
                add_Bots(bots)                   
            await message.reply("تم رفع البوتات بنجاح ✨♥")
    
def add_Bots(bots):
    if is_Bots(bots):
        return
    r.sadd(f"maker{hos_id}", str(bots))

def is_Bots(bots):
    try:
        a = get_Bots()
        if bots in a:
            return True
        return False
    except:
        return False

def del_Bots(bots):
    if not is_Bots(bots):
        return False
    r.srem(f"maker{hos_id}", str(bots))

def get_Bots():
    try:
        lst = []
        for a in r.smembers(f"maker{hos_id}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

def get_Bots_backup(): 
	text = ''
	for bots in r.smembers(f"maker{hos_id}"):
		text += bots.decode('utf-8')+'\n'
	with open('Bots.txt', 'w+') as f:
		f.write(text)
	return 'Bots.txt'

@app.on_message(filters.command("جلب البوتات", ""))
async def botzbjhfhfbhgbojfhmbie(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    await message.reply_document(get_Bots_backup())
    
@app.on_message(filters.command("《البوتات المصنوعه》", ""))
async def botzbjbbojfhmbie(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    o = 0
    text = "قائمة البوتات\n"
    for x in get_Bots():
        o += 1
        bot_username = x[0]
        dev_id = x[1]
        user = await client.get_users(dev_id)
        user = user.username
        text += f"{o}- @{bot_username}: @{user}\n"
    if o == 0:
        return await message.reply_text("لا يوجد بوتات مصنوعة")
    await message.reply_text(text)
   
@app.on_message(filters.command("《حذف بوت》", "") & filters.private)
async def delete_bot_zombie(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        if message.from_user.username in CASER:
            return
        for x in get_Bots():
            bot_username = x[0]
            if x[1] == message.from_user.id:
                try:
                  boot = appp[bot_username]
                  await boot.stop()
                  user = usr[bot_username]
                  await user.stop()
                  del_Bots(x)
                  Musi.remove(bot_username)
                  return await message.reply_text("تم حذف بوتك من الصانع.")
                except Exception as e:
                  del_Bots(x)
        return await message.reply_text("لم تقم بصنع بوتات")
    try:
        bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    for x in get_Bots():
        if x[0] == bot_username:
            try:
             boot = appp[bot_username]
             await boot.stop()
             user = usr[bot_username]
             await user.stop()
             del_Bots(x)
             Musi.remove(bot_username)
            except Exception as e:
             del_Bots(x)
    await message.reply_text("تم حذف البوت بنجاح")

@app.on_message(filters.command("احصائيات البوتات المصنوعه", ""))
async def botstatfhgvhfus(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    g = 0
    d = 0
    u = 0
    text = ""
    bots = get_Bots()
    try:
        for i in bots:
            try:
                bot_username = i[0]
                user = await client.get_users(bot_username)
                bot_id = user.id
                g += len(get_groups(bot_id))
                u += len(get_users(bot_id))
                d += 1
            except Exception as e:
                print(e)
    except:
        return await message.reply_text("لا يوجد بوتات مصنوعه .⚡")
    try:
        await message.reply_text(f"البوتات المصنوعة {d}\n📊 عدد المجموعات: {g}\n👤 عدد المستخدمين: {u}")
    except:
        await message.reply_text("لا يوجد بوتات مصنوعه .⚡")

def get_users(bot_id):
    try:
        list = []
        for a in r.smembers(f"botusers{bot_id}"):
            list.append(int(a.decode('utf-8')))
        return list
    except:
        return []

def get_groups(bot_id):
    try:
        list = []
        for a in r.smembers(f"botgroups{bot_id}"):
            list.append(int(a.decode('utf-8')))
        return list
    except:
        return []
    
@app.on_message(filters.command(["اذاعه عام بجميع البوتات"], ""))
async def cahfjgjfghfvst_dev(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    ask = await client.ask(message.chat.id, "قم بارسال الاذاعه الان", timeout=300)
    if ask.text == "الغاء":
        return await ask.reply_text("تم الالغاء")
    pn = await client.ask(message.chat.id, "هل تريد تثبيت الاذاعه\nارسل « نعم » او « لا »", timeout=200)
    h = await message.reply_text("انتظر بضع الوقت جاري الاذاعه")
    c = 0
    l = 0
    g = 0
    h = 0
    bots = get_Bots()
    for i in bots:
        try:
            bot_username = i[0]
            user = await client.get_users(bot_username)
            bot_id = user.id
            bot = appp[bot_username]
            for user in get_users(bot_id):
                hogs = int(user)
                try:
                    m = await bot.send_message(hogs, ask.text)
                    c += 1
                    if pn.text == "نعم":
                        await m.pin(disable_notification=False)
                except Exception as es:
                    print(es)
                    l += 1
            for group in get_groups(bot_id):
                hog = int(group)
                try:
                    m = await bot.send_message(hog, ask.text)
                    g += 1
                    if pn.text == "نعم":
                        await m.pin(disable_notification=False)
                except Exception as es:
                    print(es)
                    h += 1
        except Exception:
             l += 1
    return await ask.reply_text(f"تم الارسال الي {c} مستخدم \n تم ارسال في {g} جروب ✨♥")
    
@app.on_message(filters.command(["اذاعه لمطورين البوتات"], ""))
async def cast_dev(client, message):
 if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
 ask = await client.ask(message.chat.id, "**قم بارسال الاذاعه الان**", timeout=300)
 if ask.text == "الغاء":
     return await ask.reply_text("تم الالغاء")
 d = 0
 f = 0
 bots = get_Bots()
 for i in bots:
     try:
      bot_username = i[0]
      dev_id = i[1]
      bot = appp[bot_username]
      try: 
       await bot.send_message(dev_id, ask.text)
       d += 1
      except Exception as es:
       f += 1
     except Exception:
      f += 1
 return await ask.reply_text(f"**تم الارسال الي {d} مطور\n**وفشل الارسال الي {f} مطور**")

@app.on_message(filters.command(["حظر مستخدم عام"], ""))
async def fvst_dev(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    ask = await client.ask(message.chat.id, "قم بارسال معرف المستخدم \n للالغاء الامر ارسل الغاء", timeout=300)
    if ask.text == "الغاء":
        return await ask.reply_text("تم الالغاء")
    hosban = ask.text
    g = 0
    h = 0
    bots = get_Bots()
    for i in bots:
        try:
            bot_username = i[0]
            user = await client.get_users(bot_username)
            bot_id = user.id
            bot = appp[bot_username]
            for group in get_groups(bot_id):
                hog = int(group)
                try:
                    m = await bot.ban_chat_member(hog, hosban)
                    g += 1
                except Exception as es:
                    print(es)
                    h += 1
        except Exception:
             l += 1
    return await ask.reply_text(f" تم الحظر في {g} جروب ✨♥")

@app.on_message(filters.command(["الغاء حظر مستخدم عام"], ""))
async def fvst5_dev(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    ask = await client.ask(message.chat.id, "قم بارسال معرف المستخدم \n للالغاء الامر ارسل الغاء", timeout=300)
    if ask.text == "الغاء":
        return await ask.reply_text("تم الالغاء")
    hosban = ask.text
    g = 0
    h = 0
    bots = get_Bots()
    for i in bots:
        try:
            bot_username = i[0]
            user = await client.get_users(bot_username)
            bot_id = user.id
            bot = appp[bot_username]
            for group in get_groups(bot_id):
                hog = int(group)
                try:
                    m = await bot.unban_chat_member(hog, hosban)
                    g += 1
                except Exception as es:
                    print(es)
                    h += 1
        except Exception:
             l += 1             
    return await ask.reply_text(f" تم  الغاء الحظر في {g} جروب ✨♥")

@app.on_message(filters.command(["تفعيل الاشتراك لبوت"], ""))
async def CASERhg5d(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    try:
        bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    try:
        bot5 = await client.ask(message.chat.id, "هات القناه الي اضيفها", timeout=200)
    except:
        return
    channel = bot5.text.replace("https://t.me/", "") 
    for x in get_Bots():
         if x[0] == bot_username:
             user = await client.get_users(bot_username)
             try:           
               await lolo.promote_chat_member(channel, bot_username, privileges=ChatPrivileges(can_change_info=False, can_invite_users=True, can_delete_messages=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False, can_manage_chat=False, can_manage_video_chats=False))
             except Exception as e:
               print(e)
             bot_id = user.id
             oo = [channel] 
             add_channel(bot_username, oo)
    await message.reply_text("**تم تفعيل الاشتراك للبوت بنجاح**")

@Client.on_message(filters.command("تفعيل الاشتراك الاجباري", ""))
async def hchhG6M(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    ask = await client.ask(message.chat.id, "هات رابط القناه", timeout=300)
    if ask.text == "الغاء":
        return await ask.reply_text("تم الالغاء")
    channel = ask.text.replace("https://t.me/", "")
    await message.reply_text("**جاري تفعيل الاشتراك في جميع البوتات ..⚡**")
    o = 0
    for x in get_Bots():
         o += 1
         bot_username = x[0]
         try:           
             await lolo.promote_chat_member(channel, bot_username, privileges=ChatPrivileges(can_change_info=False, can_invite_users=True, can_delete_messages=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False, can_manage_chat=False, can_manage_video_chats=False))
         except Exception as e:
             print(e)
         user = await client.get_users(bot_username)
         bot_id = user.id
         oo = [channel] 
         add_channel(bot_username, oo)
    if o == 0:
         return await message.reply_text("لا يوجد بوتات لتحديثها")
    await message.reply_text(f"**تم تفعيل الاشتراك في جميع البوتات بنجاح ✨♥ \n وعددهم [{o}]**")    

@Client.on_message(filters.command("تعطيل الاشتراك الاجباري", ""))
async def hchhGu55M(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    ask = await client.ask(message.chat.id, "هات رابط القناه", timeout=300)
    if ask.text == "الغاء":
        return await ask.reply_text("تم الالغاء")
    channel = ask.text.replace("https://t.me/", "")
    await message.reply_text("**جاري تعطيل الاشتراك في جميع البوتات ..⚡**")
    o = 0
    for x in get_Bots():
        o += 1
        bot_username = x[0]
        user = await client.get_users(bot_username)
        bot_id = user.id
        for l in get_channel(bot_username):
         if l[0] == channel:
          del_channel(bot_username, l)
    if o == 0:
        return await message.reply_text("لا يوجد بوتات")
    await message.reply_text(f"**تم تعطيل الاشتراك في جميع البوتات بنجاح ✨♥ \n وعددهم [{o}]**")    
       
@app.on_message(filters.command(["تعطيل الاشتراك لبوت"], ""))
async def CASEGhg5d(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    try:
        bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    try:
        bot5 = await client.ask(message.chat.id, "هات القناه الي اضيفها", timeout=200)
    except:
        return
    channel = bot5.text.replace("https://t.me/", "") 
    for x in get_Bots():
         if x[0] == bot_username:
             user = await client.get_users(bot_username)
             bot_id = user.id
             for l in get_channel(bot_username):
              if l[0] == channel:
               del_channel(bot_username, l)
    await message.reply_text("**تم تعطيل الاشتراك الاجباري للبوت بنجاح**")
    
def add_channel(bot_id, oo):
    if is_channel(bot_id, oo):
        return
    r.sadd(f"channel{bot_id}", str(oo))

def is_channel(bot_id, oo):
    try:
        a = get_channel(bot_id)
        if oo in a:
            return True
        return False
    except:
        return False

def del_channel(bot_id, oo):
    if not is_channel(bot_id, oo):
        return False
    r.srem(f"channel{bot_id}", str(oo))

def get_channel(bot_id):
    try:
        lst = []
        for a in r.smembers(f"channel{bot_id}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@app.on_message(filters.command(["فحص البوتات"],""))
async def testbgbjfvnvots(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    bots = get_Bots()
    text = "احصائيات البوتات المصنوعه"
    b = 0
    for i in bots:
        try:
         bot_username = i[0]
         user = await client.get_users(bot_username)
         bot_id = user.id
         b += 1
         text += f"\n**{b}- @{bot_username} ، Group : {len(get_groups(bot_id))}**"
        except Exception as es:
           print(es)
    await message.reply_text(text)

@app.on_message(filters.command(["تصفيه البوتات"],""))
async def botstathfbbus(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    ask = await client.ask(message.chat.id, "ارسل الحد الادني لإحصائيات!", timeout=30)
    if ask.text == "الغاء":
        return await ask.reply_text("تم الالغاء")
    bots = get_Bots()
    m = int(ask.text)
    text = f"تم ايقاف هذه البوتات لان الاحصائيات اقل من: {ask.text} مجموعة"
    b = 0
    for x in bots:
        bot_username = x[0]
        user = await client.get_users(bot_username)
        bot_id = user.id
        dev_id = x[1]
        user = await client.get_users(dev_id)
        user = user.username
        g = len(get_groups(bot_id))
        if g < m:
            b += 1
            try:
                boot = appp[bot_username]
                await boot.stop()
                use1r = usr[bot_username]
                await use1r.stop()
                del_Bots(x)
                Musi.remove(bot_username)
            except Exception as es:
                print(es)
                del_Bots(x)
            text += f"\n{b}- @{bot_username} ، Group: {g}"    
    await message.reply_text(text)

@app.on_message(filters.command("ايقاف جميع البوتات", ""))
async def hos(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    await message.reply_text("**جاري ايقاف جميع البوتات ..⚡**")
    o = 0
    for x in get_Bots():
        o += 1
        bot_username = x[0]
        try:         
         boot = appp[bot_username]
         await boot.stop()
         user = usr[bot_username]
         await user.stop()
         Musi.remove(bot_username)
        except Exception as e:    
          print(e)
    if o == 0:
        return await message.reply_text("لا يوجد بوتات ايقافها")
    await message.reply_text(f"تم ايقاف جميع البوتات بنجاح ✨♥ \n وعددهم [{o}]")

@app.on_message(filters.command("تعديل بوت", ""))
async def hos57304(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        if message.from_user.username in CASER:
            return
        for x in get_Bots():
            if x[1] == message.from_user.id:
                return await message.reply_text("لقد قمت بصنع بوت من قبل . ")   
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("تغيير التوكن", callback_data=f"hossam12"), InlineKeyboardButton("تغيير الجلسه", callback_data=f"CASER12")]])
    await message.reply_text("اختار ما تريد بالاسفل", reply_markup=keyboard)

@app.on_callback_query(filters.regex(pattern=r"^(CASER12|hossam12)$"))
async def adm57in_risghts(client: Client, CallbackQuery):
   command = CallbackQuery.matches[0].group(1)
   chat_id = CallbackQuery.message.chat.id
   if command == "CASER12":
    try:
        bot = await client.ask(chat_id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    as5k = await client.ask(chat_id, "ارسل الجلسه الان", timeout=200)
    await asyncio.sleep(3)
    SES8SION = as5k.text     
    for x in get_Bots():
        if x[0] == bot_username: 
            dev_id = x[1]
            TOKEN = x[2]
            SESSION = x[3]
            logg = x[4]
            try:
             boot = appp[bot_username]
             await boot.stop()
             user = usr[bot_username]
             await user.stop()
             usr.clear()         
             call.clear()         
             del_Bots(x)
             Musi.remove(bot_username)
            except Exception as e:
             del_Bots(x)
             oo = [bot_username, dev_id, TOKEN, SES8SION, logger]
             add_Bots(oo)    
        try:
         await start_bot(client, CallbackQuery)
         await CallbackQuery.message.reply_text("**تم بنجاح ♥**")  
        except:
         pass             
   if command == "hossam12":
    try:
        bot = await client.ask(chat_id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    as5k = await client.ask(chat_id, "ارسل توكن البوت الان", timeout=200)
    await asyncio.sleep(3)
    TOK5EN = as5k.text       
    for x in get_Bots():
        if x[0] == bot_username: 
            dev_id = x[1]
            TOKEN = x[2]
            SESSION = x[3]
            logg = x[4]
            try:
             boot = appp[bot_username]
             await boot.stop()
             user = usr[bot_username]
             await user.stop()
             usr.clear()         
             call.clear()         
             del_Bots(x)
             Musi.remove(bot_username)
             call.clear()         
            except Exception as e:
             del_Bots(x)
             oo = [bot_username, dev_id, TOK5EN, SESSION, logger]
             add_Bots(oo)    
        try:
         await start_bot(client, CallbackQuery)
         await CallbackQuery.message.reply_text("**تم بنجاح ♥**")  
        except:
         pass             
    
@app.on_message(filters.command("حذف جميع البوتات", ""))
async def hossamGM(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    await message.reply_text("**جاري حذف جميع البوتات ..⚡**")
    o = 0
    for x in get_Bots():
        o += 1
        bot_username = x[0]
        try:         
         boot = appp[bot_username]
         await boot.stop()
         user = usr[bot_username]
         await user.stop()
         del_Bots(x)
         Musi.remove(bot_username)
        except:        	
         del_Bots(x)
    if o == 0:
        return await message.reply_text("لا يوجد بوتات لحذفها")
    await message.reply_text(f"تم حذف جميع البوتات بنجاح ✨♥ \n وعددهم [{o}]")
    
@app.on_message(filters.command(["تشغيل بوت"],""))
async def CASRgd(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    try:
        bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    for x in get_Bots():
        if x[0] == bot_username:
          dev_id = x[1]
          user = await client.get_users(dev_id)
          user = user.username
          try:
              bot = appp[bot_username]
              user1 = usr[bot_username]
              await bot.start()
              await user1.start()
              Musi.append(bot_username)
          except Exception as e:
              await client.send_message(message.chat.id, f"فشل في تشغيل هذا البوت : @{bot_username}")
    await message.reply_text("تم تشغيل البوت بنجاح")

@app.on_message(filters.command(["ايقاف بوت"],""))
async def CASERgd(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    try:
        bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    for x in get_Bots():
        if x[0] == bot_username:
         try: 
          boot = appp[bot_username]
          await boot.stop()
          user = usr[bot_username]
          await user.stop()
          Musi.remove(bot_username)
         except:
          print("...")
    await message.reply_text("تم ايقاف البوت بنجاح")
    
@app.on_message(filters.command("رفع مطور", "") & filters.private)
async def mazojgvmbie(client, message):
  if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
    return
  try:
      ask = await client.ask(message.chat.id, "ارسل يوزر المطور", timeout=300)
  except:
      return    
  SE = ask.text.replace("@", "")
  DEVSs.append(SE)
  await client.send_message(message.chat.id, "تم رفع المطور بنجاح")
            
@app.on_message(filters.command("المطورين", "") & filters.private)
async def getbannbvnbedusers(client, message):
  if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
    return
  caesar = "قائمة المطورين:\n\n"
  for username in DEVSs:
      caesar += f"- @{username}\n" 
  await client.send_message(message.chat.id, caesar)
  
@app.on_message(filters.command("تنزيل مطور", "") & filters.private)
async def unbanncbb_user(client, message):
  if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
    return
  try:
      ask = await client.ask(message.chat.id, "ارسل يوزر المطور", timeout=300)
  except:
      return    
  SE = ask.text.replace("@", "")
  if SE in DEVSs:
      DEVSs.remove(SE)
      await client.send_message(message.chat.id, "تم تنزيل المطور بنجاح")
  else:
      await client.send_message(message.chat.id, "اليوزر ليس لمطور في الصانع")
        
@app.on_message(filters.command("⚡ قسم الاشتراك ⚡", ""))
async def chhfus(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    kep = ReplyKeyboardMarkup([["تفعيل الاشتراك الاجباري", "تعطيل الاشتراك الاجباري"], ["تفعيل الاشتراك لبوت", "تعطيل الاشتراك لبوت"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك قسم الاشتراك", reply_markup=kep)

@app.on_message(filters.command("⚡ قسم الاذاعه ⚡", ""))
async def gvhfbcfvjgbus(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    kep = ReplyKeyboardMarkup([["الاحصائيات"], ["اذاعة بالتوجيه", "اذاعة", "اذاعة بالتثبيت"], ["رجوع"]], resize_keyboard=True)

    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك قسم تحكم الصانع", reply_markup=kep)
