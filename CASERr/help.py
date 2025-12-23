import asyncio
import os
import sys
import random
from datetime import datetime
from typing import Union, List, Iterable

from pyrogram import Client, filters, enums
from pyrogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup, 
                            CallbackQuery, ChatPrivileges, ReplyKeyboardMarkup, 
                            ChatPermissions, User)
from pyrogram.errors import FloodWait, PeerIdInvalid

# استيراد الإعدادات والداتا
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned

# ............................................ فحص المساعد ...........................................................    
@Client.on_message(filters.command("فحص المساعد", ""), group=5865)
async def helper_stats(client: Client, message: Message):
    bot_username = client.me.username
    owner_id = await get_dev(bot_username)
    
    # التحقق من أن المرسل هو المطور
    if message.from_user.id == owner_id or message.from_user.username in caes:
        assistant = await get_userbot(bot_username)
        mm = await message.reply_text("🔎 جاري فحص حالة الحساب المساعد واستخراج الإحصائيات...")
        
        start = datetime.now()
        u, g, sg, c, b, a_chat = 0, 0, 0, 0, 0, 0
        
        async for dialog in assistant.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type == enums.ChatType.PRIVATE:
                u += 1
            elif chat_type == enums.ChatType.BOT:
                b += 1
            elif chat_type == enums.ChatType.GROUP:
                g += 1
            elif chat_type == enums.ChatType.SUPERGROUP:
                sg += 1
                try:
                    member = await dialog.chat.get_member(assistant.me.id)
                    if member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
                        a_chat += 1
                except:
                    pass
            elif chat_type == enums.ChatType.CHANNEL:
                c += 1

        end = datetime.now()
        duration = (end - start).seconds
        
        text = f"""
✅ **تم فحص المساعد بنجاح في {duration} ثانية**

👤 **الاسم:** {assistant.me.first_name}
🆔 **الايدي:** `{assistant.me.id}`

📊 **الإحصائيات:**
• الخاص: {u}
• البوتات: {b}
• المجموعات: {g}
• المجموعات الخارقة: {sg}
• القنوات: {c}
• مشرف في: {a_chat} چات

⚠️ **تم الفحص بواسطة:** {assistant.me.mention}
"""
        await mm.edit_text(text)

# ............................................ تعديلات البروفايل ...........................................................    

@Client.on_message(filters.command("تغير الاسم الاول", ""), group=58650)
async def change_helper_name(client: Client, message: Message):
    bot_username = client.me.username
    owner_id = await get_dev(bot_username)
    if message.from_user.id == owner_id or message.from_user.username in caes:
        try:
            ask = await client.ask(message.chat.id, "📝 ارسل الآن الاسم الجديد الذي تريده للمساعد:", timeout=60)
            new_name = ask.text
            assistant = await get_userbot(bot_username)
            await assistant.update_profile(first_name=new_name)
            await message.reply_text(f"✅ تم تغيير اسم المساعد إلى: **{new_name}**")
        except Exception as e:
            await message.reply_text(f"❌ حدث خطأ: {e}")

@Client.on_message(filters.command("تغير البايو", ""), group=586505)
async def change_helper_bio(client: Client, message: Message):
    bot_username = client.me.username
    owner_id = await get_dev(bot_username)
    if message.from_user.id == owner_id or message.from_user.username in caes:
        try:
            ask = await client.ask(message.chat.id, "📝 ارسل الآن البايو (Bio) الجديد:", timeout=60)
            new_bio = ask.text
            assistant = await get_userbot(bot_username)
            await assistant.update_profile(bio=new_bio)
            await message.reply_text("✅ تم تحديث البايو الخاص بالمساعد بنجاح.")
        except Exception as e:
            await message.reply_text(f"❌ حدث خطأ: {e}")

@Client.on_message(filters.command("تغير اسم المستخدم", ""), group=586502)
async def change_helper_username(client: Client, message: Message):
    bot_username = client.me.username
    owner_id = await get_dev(bot_username)
    if message.from_user.id == owner_id or message.from_user.username in caes:
        try:
            ask = await client.ask(message.chat.id, "📝 ارسل اليوزر (Username) الجديد بدون @:", timeout=60)
            new_user = ask.text
            assistant = await get_userbot(bot_username)
            await assistant.set_username(new_user)
            await message.reply_text(f"✅ تم تغيير يوزر المساعد إلى: @{new_user}")
        except Exception as e:
            await message.reply_text(f"❌ حدث خطأ (ربما اليوزر مأخوذ أو غير متاح): {e}")

@Client.on_message(filters.command(["اضافه صوره"], ""), group=5865067)
async def add_helper_photo(client: Client, message: Message):
    bot_username = client.me.username
    owner_id = await get_dev(bot_username)
    if message.from_user.id == owner_id or message.from_user.username in caes:
        try:
            ask = await client.ask(message.chat.id, "📸 قم بإرسال الصورة الآن:", timeout=120)
            if not ask.photo:
                return await message.reply_text("❌ يجب إرسال صورة حصراً.")
            
            photo_path = await ask.download()
            assistant = await get_userbot(bot_username)
            await assistant.set_profile_photo(photo=photo_path)
            await message.reply_text("✅ تم تغيير صورة الحساب المساعد.")
            if os.path.exists(photo_path): os.remove(photo_path)
        except Exception as e:
            await message.reply_text(f"❌ حدث خطأ: {e}")

@Client.on_message(filters.command(["ازاله صوره"], ""), group=5865084)
async def remove_helper_photo(client: Client, message: Message):
    bot_username = client.me.username
    owner_id = await get_dev(bot_username)
    if message.from_user.id == owner_id or message.from_user.username in caes:
        try:
            assistant = await get_userbot(bot_username)
            photos = [p async for p in assistant.get_chat_photos("me")]
            if photos:
                await assistant.delete_profile_photos(photos[0].file_id)
                await message.reply_text("✅ تم حذف صورة البروفايل الحالية.")
            else:
                await message.reply_text("❌ المساعد لا يملك صورة حالياً.")
        except Exception as e:
            await message.reply_text(f"❌ خطأ أثناء الإزالة: {e}")

# ............................................ التحكم في المجموعات ...........................................................    

@Client.on_message(filters.command("دعوه المساعد الي الانضمام", ""), group=5865024)
async def helper_join_chat(client: Client, message: Message):
    bot_username = client.me.username
    owner_id = await get_dev(bot_username)
    if message.from_user.id == owner_id or message.from_user.username in caes:
        try:
            ask = await client.ask(message.chat.id, "🔗 ارسل رابط الجروب أو اليوزر الآن:", timeout=60)
            link = ask.text.replace("https://t.me/", "")
            assistant = await get_userbot(bot_username)
            await assistant.join_chat(link)
            await message.reply_text("✅ انضم المساعد بنجاح.")
        except Exception as e:
            await message.reply_text(f"❌ فشل الانضمام: {e}")

# ............................................ الإذاعة بالمساعد ...........................................................    

@Client.on_message(filters.command(["توجيه عام بالمساعد", "اذاعه عام بالمساعد"], ""), group=58650417)
async def helper_broadcast(client: Client, message: Message):
    command = message.command[0]
    bot_username = client.me.username
    owner_id = await get_dev(bot_username)
    
    if message.from_user.id == owner_id or message.from_user.username in caes:
        ask = await client.ask(message.chat.id, "📢 ارسل الآن (النص أو الوسائط) التي تريد إذاعتها بالمساعد:", timeout=300)
        if ask.text == "الغاء": return await ask.reply_text("✅ تم الإلغاء.")
        
        await message.reply_text("⏳ جاري الإذاعة لجميع المحادثات.. قد يستغرق هذا وقتاً طويلاً.")
        
        assistant = await get_userbot(bot_username)
        done, fail = 0, 0
        
        async for dialog in assistant.get_dialogs():
            try:
                if "اذاعه" in command:
                    await ask.copy(dialog.chat.id)
                else:
                    await ask.forward(dialog.chat.id)
                done += 1
                await asyncio.sleep(0.3) # لتجنب الحظر
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except:
                fail += 1
        
        await message.reply_text(f"✅ **تمت الإذاعة بنجاح!**\n\n• تم الإرسال إلى: {done}\n• فشل في: {fail}")

# ............................................ الحذف والمسح ...........................................................    

@Client.on_message(filters.command(["حذف", "مسح"], ""), group=5675436417)
async def delete_messages_count(client: Client, message: Message):
    bot_username = client.me.username
    assistant = await get_userbot(bot_username)
    try:
        count = int(message.text.split(None, 1)[1])
        deleted = 0
        async for msg in assistant.get_chat_history(message.chat.id, limit=count):
            try:
                await msg.delete()
                deleted += 1
            except: pass
        await message.reply_text(f"✅ تم مسح {deleted} رسالة من المحادثة.")
    except:
        await message.reply_text("❌ ارسل الأمر مع عدد الرسائل، مثال: `مسح 10`")

@Client.on_message(filters.command(["مسح رسايله", "حذف رسايله"], ""), group=5607684417)
async def delete_user_messages(client: Client, message: Message):
    bot_username = client.me.username
    assistant = await get_userbot(bot_username)
    
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await message.reply_text("⏳ جاري حذف رسائل هذا المستخدم..")
        async for msg in assistant.get_chat_history(message.chat.id):
            if msg.from_user and msg.from_user.id == user_id:
                try: await msg.delete()
                except: pass
        await message.reply_text("✅ تم حذف جميع رسائل المستخدم المذكور.")
    else:
        await message.reply_text("❌ رد على رسالة المستخدم الذي تريد حذف جميع رسائله.")

# ............................................ التفاعلات التلقائية ...........................................................    

REACTIONS = ["👍", "❤", "🔥", "🥰", "🎉", "🤩", "🙏", "👌", "🕊", "😍", "😎", "🍓", "💋", "💘", "🌚"]

@Client.on_message(filters.channel, group=1234567)
async def auto_reaction_channels(client: Client, message: Message):
    bot_username = client.me.username
    assistant = await get_userbot(bot_username)
    try:
        reaction = random.choice(REACTIONS)
        await assistant.send_reaction(message.chat.id, message.id, reaction)
    except:
        pass
