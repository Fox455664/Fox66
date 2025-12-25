import os
import asyncio
import sys
import redis, re
from dotenv import load_dotenv
from os import getenv
from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from bot import bot
from bot import DEVS, DEVSs
from bot import bot_id
from casery import caserid

OWNER_ID = int(f"{caserid}")

r = redis.Redis(
    host="ultimate-ferret-48101.upstash.io", password="AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE", ssl=True,
    port=6379,)

Keyboard = ReplyKeyboardMarkup(
  [
    [("《حذف بوت》"),("《صنع بوت》")],
    [("《تفعيل المجاني》"),("《تعطيل المجاني》")],
    [("تفعيل التواصل"),("تعطيل التواصل")],
    [("تشغيل جميع البوتات"),("ايقاف جميع البوتات")],
    [("《البوتات المصنوعه》"), ("احصائيات البوتات المصنوعه")],
    [("تصفيه البوتات"), ("فحص البوتات")],  
    [("اذاعه عام بجميع البوتات"), ("اذاعه لمطورين البوتات")],
    [("تشغيل بوت"), ("ايقاف بوت")],
    [("رفع البوتات"),("جلب البوتات")],
    [("حذف جميع البوتات"),("تعديل بوت")],
    [("الغاء حظر مستخدم عام"),("حظر مستخدم عام")],
    [("⚡ قسم الاشتراك ⚡")], 
    [("⚡ قسم الاذاعه ⚡")],
    [("《مطور السورس》")],
    [("《السورس》")],
    [("رفع مطور"),("تنزيل مطور")],
    [("المطورين")],     
  ],
  resize_keyboard=True
)

Keybcasoard = ReplyKeyboardMarkup(
  [
    [("《مطور السورس》")],
    [("《السورس》")],
    [("《حذف بوت》"), ("《صنع بوت》")],
    [("《تفعيل المجاني》"),("《تعطيل المجاني》")],
    [("《البوتات المصنوعه》"), ("احصائيات البوتات المصنوعه")],
    [("فحص البوتات")],  
    [("تحديث الصانع")],
  ],
  resize_keyboard=True
)

@bot.on_message(filters.command(["/start","رجوع"], "") & filters.private)
async def for_u55sers(bot, message):
    kep = ReplyKeyboardMarkup([["《صنع بوت》", "《حذف بوت》"], ["《السورس》", "《مطور السورس》"]], resize_keyboard=True)
    if message.from_user.username in DEVS:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالصانع", reply_markup=Keyboard)
    elif message.from_user.username in DEVSs:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالصانع", reply_markup=Keybcasoard)        
    else:
        await message.reply_text(f"╮⦿ اهـلا بڪ عزيـزي ⁽ {message.from_user.mention} ₎\n│⎋ اليـكـ المصنـع", reply_markup=kep)
        
@bot.on_message(filters.command(["/start", "رجوع"], "") & filters.private)
async def for_users (bot,m):
   if check(m.from_user.id):
     kep = ReplyKeyboardMarkup([["《صنع بوت》", "《حذف بوت》"], ["البوتات المصنوعه"], ["تعطيل المجاني", "تفعيل المجاني"], ["تعطيل التواصل", "تفعيل التواصل"], ["السورس"], ["الغاء"]], resize_keyboard=True)
     return
   kep = ReplyKeyboardMarkup([["《صنع بوت》", "《حذف بوت》"], ["《السورس》", "《مطور السورس》"]], resize_keyboard=True)
   print("gg")
   if not check(m.from_user.id):
     await check_sub(bot, m)
   if not is_user(m.from_user.id):
     add_user(m.from_user.id)
     text = '🙍 شخص جديد دخل الى البوت !\n\n'
     text += f'🎯 الأسم: {m.from_user.first_name}\n'
     text += f'♻️ الايدي: {m.from_user.id}\n\n'
     text += f'🌐 اصبح عدد المستخدمين: {len(get_users())}'
     reply_markup=InlineKeyboardMarkup (
      [[
        InlineKeyboardButton (m.from_user.first_name, user_id=m.from_user.id)
      ]]
     )
     if len(get_admins()) > 0:
        list = get_admins()
        for admin in list:
          await bot.send_message(int(admin), text, reply_markup=reply_markup)
        await bot.send_message(int(r.get(f"bot_owner{bot_id}")), text, reply_markup=reply_markup)
     else:
        await bot.send_message(int(r.get(f"bot_owner{bot_id}")), text, reply_markup=reply_markup)
        
     
   
@bot.on_message(filters.command("LAVhshdhA") & filters.private, group=1)
async def keyboard_show(bot,m):
    if check(m.from_user.id):
       await m.reply(f"• أهلا بك {m.from_user.mention} .\n• اليك لوحة تحكم\n• لاظهار كيبورد المطور /start", reply_markup=Keyboard, quote=True)

admins_commands = [
   'الاحصائيات', 'تفعيل التواصل',
   'تعطيل التواصل', 'اذاعة بالتثبيت', 'اذاعة',
   'اذاعة بالتوجيه', 'تفعيل الاشتراك', 'تعطيل الاشتراك',
   'ضع قناة الاشتراك', 'حذف قناة الاشتراك', 'قناة الاشتراك','قائمه الأدمنيه',
   'المستخدمين', 'الأدمنية', 'الجروبات',
   'اذاعة بالمجموعات','اذاعة بالتثبيت بالمجموعات', 'اخفاء الكيبورد'
   ]
   
owner_commands = [
   'نقل ملكية البوت', 'رفع ادمن', 'تنزيل ادمن'
]

@bot.on_message(filters.text & filters.private, group=2)
async def keyboard_for_admins(bot, m):
  if m.text in admins_commands:
    if not check(m.from_user.id):
      return await m.reply('🦸 الامر ده للمطور بس', quote=True)
    else:
    
      if m.text == 'الاحصائيات':
        text = f'**👤 عدد المستخدمين: {len(get_users())}\n'
        text += f'📊 عدد المجموعات: {len(get_groups())}\n'
        text += f'🌀 عدد المشرفين: {len(get_admins())}**'
        await m.reply(text, quote=True)
        
      if m.text == 'تفعيل التواصل':
        if r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تفعيل التواصل مسبقاً", quote=True)
          
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل التواصل بنجاح**', quote=True)
        r.set(f'enable_twasol{bot_id}', 1)
      
      if m.text == 'تعطيل التواصل':
        if not r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تعطيل التواصل مسبقاً", quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل التواصل بنجاح**', quote=True)
        r.delete(f'enable_twasol{bot_id}')
      
      if m.text == 'المستخدمين':
        await m.reply_document(get_users_backup(), quote=True)
      
      if m.text == 'الأدمنية':
        await m.reply_document(get_admins_backup(), quote=True)
      
      if m.text == 'الجروبات':
        await m.reply_document(get_groups_backup(), quote=True)
      
      if m.text == 'تفعيل الاشتراك':
        if r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تفعيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل الاشتراك بنجاح**', quote=True) 
        r.set(f"enable_force_subscribe{bot_id}", 1)
      
      if m.text == 'تعطيل الاشتراك':
        if not r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تعطيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل الاشتراك بنجاح**', quote=True) 
        r.delete(f"enable_force_subscribe{bot_id}")
      
      if m.text == 'ضع قناة الاشتراك':
        await m.reply("• ارسل معرف القناة العام مثال @COURSE_CAESAR", quote=True)
        r.set(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
      
      if m.text == 'حذف قناة الاشتراك':
        if not r.get(f'force_channel{bot_id}'):
          return await m.reply("• لا توجد قناة اشتراك معينة", quote=True)
        await m.reply("• تم حذف قناة الاشتراك بنجاح", quote=True)
        r.delete(f'force_channel{bot_id}')
      
      if m.text == 'قناة الاشتراك':
        if not r.get(f'force_channel{bot_id}'):
          await m.reply('• لاتوجد قناة مضافة', quote=True)
        else:
          channel = r.get(f'force_channel{bot_id}').decode('utf-8')
          await m.reply(f"https://t.me/{channel}", quote=True)
      
      if m.text == 'قائمه الأدمنيه':
        if len(get_admins()) == 0:
          await m.reply("• لايوجد آدمنية", quote=True)
        else:
          text = '• قائمة الأدمنية\n'
          for admin in get_admins():
            try:
              get = await bot.get_chat(int(admin))
              text += f'• [{get.first_name}](tg://user?id={admin})\n'
            except:
              text += f'• [@COURSE_CAESAR](tg://user?id={admin})\n'
          await m.reply(text, quote=True)
          
      if m.text == 'اذاعة':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == 'اذاعة بالتثبيت':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
        
      if m.text == 'اذاعة بالتوجيه':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == 'اذاعة بالمجموعات':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == 'اذاعة بالتثبيت بالمجموعات':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == 'اخفاء الكيبورد':
        await m.reply("• تم اخفاء لوحة التحكم لاظهارها مجدداً ارسل /start",
        quote=True, reply_markup=ReplyKeyboardRemove (selective=True))


@bot.on_message(filters.text & filters.private, group=3)
async def for_owner(bot,m):
  text = m.text
  if text in owner_commands:
   if not m.from_user.id == int(r.get(f"bot_owner{bot_id}")):
      return await m.reply("• هذا الأمر يخص المطور الأساسي فقط", quote=True)
   
   if text == 'نقل ملكية البوت':
     await m.reply("• ارسل ايدي المالك الجديد الآن", quote=True)
     r.set(f"{m.from_user.id}transfer{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
   if text == 'رفع ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
   
   if text == 'تنزيل ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}", 1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")

@bot.on_message(filters.text & filters.private, group=4)
async def response_for_commands(bot,m):
   text = m.text
   
   if text in admins_commands:
     return

   if text in owner_commands:
     return 
     
   if check(m.from_user.id):
     if text == 'الغاء':
       await m.reply("• تم الغاء كل شيء", quote=True)
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
       
     
     if r.get(f"{m.from_user.id}transfer{m.chat.id}{bot_id}"):
       try:
         get = await bot.get_chat(int(text))
       except:
         return await m.reply("• الآيدي خطأ أرسل آيدي آخر او تأكد ان المستخدم مو حاظر البوت", quote=True)
       r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
       txt = '• تم نقل ملكية البوت بنجاح إلى :\n\n'
       txt += f'• الأسم : {get.first_name}\n'
       txt += f'• الآيدي : {get.id}\n'
       if get.username:
         txt += f'• اليوزر : @{get.username}\n'
       if get.bio:
         txt += f'• البايو : {get.bio}\n'
       r.set(f"bot_owner{bot_id}", get.id)
       await m.reply(txt, quote=True)
       return
     
     if r.get(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}"):
       try:
         get = await bot.get_chat(int(text))
       except:
         return await m.reply("• الآيدي خطأ أرسل آيدي آخر او تأكد ان المستخدم مو حاظر البوت", quote=True)
         
       if is_admin(int(text)):
         r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
         return await m.reply(f"• المستخدم [{get.first_name}]({get.id}) ادمن من قبل")
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       txt = '• تم رفع المستخدم ادمن بنجاح :\n\n'
       txt += f'• الأسم : {get.first_name}\n'
       txt += f'• الآيدي : {get.id}\n'
       if get.username:
         txt += f'• اليوزر : @{get.username}\n'
       if get.bio:
         txt += f'• البايو : {get.bio}\n'
       add_admin(int(text))
       await m.reply(txt, quote=True)
       return 
     
     if r.get(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}"):
      try: 
       if not is_admin(int(text)):
         r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
         return await m.reply("• المستخدم مو ادمن من قبل")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       del_admin(int(text))
       await m.reply("• تم تنزيل المستخدم ادمن بنجاح", quote=True)
       return 
      except:
       return await m.reply("• الآيدي خطأ")
     
     if r.get(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}"):
       channel = text.replace("@","")
       r.set(f"force_channel{bot_id}", channel)
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
       await m.reply("• تم تعيين القناة بنجاح ", quote=True)
       
     
     
@bot.on_message(filters.private, group=8)
async def forbroacasts(bot,m):
   if m.text:
      if m.text in admins_commands:  return
      if m.text in owner_commands:  return 
   if m.from_user:
     if r.get(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_users():
          try:
            await m.copy(int(user))
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_users():
          try:
            a = await m.copy(int(user))
            await a.pin(disable_notification=False,both_sides=True)
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception as e:
            print(e)
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_users():
          try:
            await m.forward(int(user))
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups():
          try:
            await m.copy(int(group))
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
       
     
     if r.get(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups():
          try:
            a = await m.copy(int(group))
            await a.pin(disable_notification=False)
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")

@bot.on_message(filters.private, group=9)
async def twasol__(bot,m):
   if not check(m.from_user.id):
     if r.get(f'enable_twasol{bot_id}'):
       await m.forward(int(r.get(f"bot_owner{bot_id}")))
   
   if m.from_user.id == int(r.get(f"bot_owner{bot_id}")):
      if m.reply_to_message:
        if m.reply_to_message.forward_from:
          await m.reply(f"• تم إرسال رسالتك إلى {m.reply_to_message.forward_from.first_name} بنجاح", quote=True)
          try:
            await m.copy(m.reply_to_message.forward_from.id)
          except:
            pass
      

@bot.on_message(filters.text & filters.group , group=10)
async def for_admins_in_group(bot,m):
   if not m.reply_to_message:
      return
   if not m.reply_to_message.from_user:
      return
      
   if m.from_user.id == int(r.get(f"bot_owner{bot_id}")):
     text = m.text
     user_id = m.reply_to_message.from_user.id
     if text == 'رفع ادمن':
       if is_admin(user_id):
          return await m.reply("• المستخدم آدمن من قبل")
       else:
          add_admin(user_id)
          await m.reply("• تم رفعه ادمن بنجاح")
     
     if text == 'تنزيل ادمن':
      if not is_admin(user_id):
          return await m.reply("• المستخدم مو آدمن من قبل")
      else:
          del_admin(user_id)
          await m.reply("• تم تنزيله ادمن بنجاح")

def add_user(user_id: int):
	if is_user(user_id):
		return
	r.sadd(f"botusers{bot_id}", user_id)
	
def is_user(user_id: int):
  try:
    a= get_users()
    if user_id in a:
      return True
    return False
  except:
    return False

def del_user(user_id: int):
	if not is_user(user_id):
		return False
	r.srem(f"botusers{bot_id}", user_id)
	return True

def get_users():
   try:
     list = []
     for a in r.smembers(f"botusers{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_users_backup() -> str:
	text = ''
	for user in r.smembers(f"botusers{bot_id}"):
		text += user.decode('utf-8')+'\n'
	with open('users.txt', 'w+') as f:
		f.write(text)
	return 'users.txt'
	
def add_admin(user_id: int):
    if is_admin(user_id):  return 
    r.sadd(f"botadmins{bot_id}", user_id)

def is_admin(user_id: int):
  try:
    a = get_admins()
    if user_id in a:
      return True
    return False
  except:
    return False

def del_admin(user_id: int):
	if not is_admin(user_id):
		return False
	r.srem(f"botadmins{bot_id}", user_id)
	
def get_admins():
   try:
     list = []
     for a in r.smembers(f"botadmins{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_admins_backup() -> str:
	text = ''
	for admin in r.smembers(f"botadmins{bot_id}"):
		text += admin.decode('utf-8')+'\n'
	with open('admins.txt', 'w+') as f:
		f.write(text)
	return 'admins.txt'
	

def check(id):
    if is_admin(id):
      return True
    if id == int(r.get(f"bot_owner{bot_id}")):
      return True
    else:
      return False

async def check_sub(c,m):
    if not r.get(f"enable_force_subscribe{bot_id}"):
      return
    else:
      if not r.get(f"force_channel{bot_id}"):
        return 
      else:
        channel = r.get(f"force_channel{bot_id}").decode('utf-8')
        text = f'✖️ عذراً عليك الاشتراك بقناة البوت أولاً لتتمكن من استخدامه !\n\nhttps://t.me/{channel}\n- /start'
        try:
           get = await c.get_chat_member(r.get(f"force_channel{bot_id}").decode('utf-8'), m.from_user.id)
           if get.status in [enums.ChatMemberStatus.LEFT, enums.ChatMemberStatus.BANNED]:
             return await m.reply(text, quote=True, disable_web_page_preview=True)
        except:
           return await m.reply(text, quote=True, disable_web_page_preview=True)

def add_group(chat_id: int):
    if is_group(chat_id):  return 
    r.sadd(f"botgroups{bot_id}", chat_id)

def is_group(chat_id: int):
  try:
    a = get_groups()
    if chat_id in a:
      return True 
    return False 
  except:
    return False

def del_group(chat_id: int):
	if not is_group(chat_id):
		return False
	r.srem(f"botgroups{bot_id}", chat_id)

def get_groups():
   try:
     list = []
     for a in r.smembers(f"botgroups{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_groups_backup() -> str:
	text = ''
	for group in r.smembers(f"botgroups{bot_id}"):
		text += group.decode('utf-8')+'\n'
	with open('groups.txt', 'w+') as f:
		f.write(text)
	return 'groups.txt'

if not r.get(f"bot_owner{bot_id}"):
   owner = int(f"{OWNER_ID}")
   r.set(f"bot_owner{bot_id}", owner)