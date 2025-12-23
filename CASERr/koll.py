import asyncio
from random import randint
from typing import Optional
from pyrogram import Client, filters, enums
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError, AlreadyJoinedError

# استيراد الأدوات المساعدة من السورس
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes

# --- وظيفة لجلب بيانات الكول الحالي ---
async def get_group_call(client: Client, message: Message, err_message: str = "") -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
        
        if full_chat is not None and full_chat.call is not None:
            return full_chat.call
    return None

# --- أمر: مين في الكول ---
@Client.on_message(filters.command(["مين في الكول", "م ف ك", "مين ف الكول", "مين ف كول"], ""))
async def who_is_in_call(client, message):
    bot_username = client.me.username
    hoss = await get_call(bot_username)    
    hh = await message.reply("⏳ استنى ثواني أشوف مين منورنا في الكول... ✨") 
    
    try:
        # المساعد بيدخل ثانية عشان يسحب البيانات
        try:
            await hoss.join_group_call(message.chat.id, AudioPiped("./CASERr/dummy.mp3"), stream_type=StreamType().pulse_stream)
        except AlreadyJoinedError:
            pass
            
        participants = await hoss.get_participants(message.chat.id)
        if not participants:
            return await hh.edit_text("الكول فاضي يا برنس، مفيش حد بيتكلم.")
            
        text = "😎 الأشخاص المتواجدين في المحادثة الآن:\n\n"
        k = 0
        for p in participants:
            k += 1
            status = "يتحدث 🗣" if not p.muted else "ساكت 🔕"
            try:
                user_info = await client.get_users(p.user_id)
                text += f"{k} ➤ {user_info.mention} ➤ {status}\n"
            except:
                text += f"{k} ➤ مستخدم مخفي ➤ {status}\n"
        
        await hh.edit_text(text)
    except NoActiveGroupCall:
        await hh.edit_text("يا برنس الكول مش مفتوح أصلاً! افتحه الأول 😜")
    except Exception as e:
        await hh.edit_text(f"حدث خطأ فني: {e}")

# --- أمر: فتح الكول (بواسطة المساعد) ---
@Client.on_message(filters.command(["فتح الكول", "ف ك", "ف الكول"], ""))
async def start_call(c, message):
    bot_username = c.me.username
    userbot = await get_userbot(bot_username)
    hh = await message.reply_text("🚀 جاري تشغيل المحادثة الصوتية...")   
    
    # التأكد لو الكول مفتوح فعلاً
    existing_call = await get_group_call(userbot, message)
    if existing_call:
        return await hh.edit_text("الكول مفتوح أصلاً يا كبير، منورنا! ✅")
        
    try:
        await userbot.invoke(CreateGroupCall(
            peer=(await userbot.resolve_peer(message.chat.id)), 
            random_id=randint(10000, 999999999)
        ))
        await hh.edit_text("✅ تم فتح الكول بنجاح بواسطة الحساب المساعد.")           
    except Exception as e:
        await hh.edit_text("❌ فشلت في فتح الكول. تأكد من رفع الحساب المساعد (أدمن) مع صلاحية إدارة الكول.")

# --- أمر: قفل الكول ---
@Client.on_message(filters.command(["قفل الكول", "ق الكول", "ق ك"], ""))
async def end_call(c, message):
    bot_username = c.me.username
    userbot = await get_userbot(bot_username)
    hh = await message.reply_text("🛑 جاري إغلاق المحادثة الصوتية...")   
    
    group_call = await get_group_call(userbot, message)
    if not group_call:
        return await hh.edit_text("الكول مقفول خلقه يا برنس! 🤷‍♂️")
        
    try:
        await userbot.invoke(DiscardGroupCall(call=group_call))
        await hh.edit_text("✅ تم قفل الكول بنجاح. نتقابل في سهرة تانية! 👋")           
    except Exception as e:
        await hh.edit_text("❌ مقدرتش أقفل الكول. ارفع المساعد أدمن بصلاحية كاملة.")

# --- أمر: جلب ايدي الاستيكر ---
@Client.on_message(filters.command(["استك", "ايدي الاستيكر"], ""))
async def sticker_id(_, message: Message):
    reply = message.reply_to_message
    if not reply or not reply.sticker:
        return await message.reply("رد على أي ملصق (Sticker) عشان أجيبلك الكود بتاعه 🎯")
    await message.reply_text(f"<b>تفضل يا مطورنا، ايدي الملصق هو:</b>\n\n<code>{reply.sticker.file_id}</code>")

# --- التفاعل مع نهاية الكول ---
@Client.on_message(filters.video_chat_ended)
async def call_ended_handler(client, message):
    duration = message.video_chat_ended.duration
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    
    time_text = ""
    if hours > 0: time_text += f"{hours} ساعة و "
    if minutes > 0: time_text += f"{minutes} دقيقة و "
    time_text += f"{seconds} ثانية"
    
    await message.reply(f"<b>🛑 تم إنهاء مكالمة الفيديو/الصوت.\n⏳ مدة الكول كانت: {time_text}</b>")
