import os
import sys
import subprocess

# --- كود التثبيت التلقائي المطور لحل جميع المشاكل السابقة ---
def install_missing_libraries():
    # أضفت pytube للقائمة
    required_packages = ["telethon", "oldpyro", "pytube", "pyromod"]
    
    for package in required_packages:
        try:
            # محاولة استدعاء المكتبة للتأكد من وجودها
            if package == "pytube":
                import pytube
            elif package == "telethon":
                import telethon
            elif package == "oldpyro":
                import oldpyro
            else:
                __import__(package)
        except ImportError:
            print(f"🔄 جاري تثبيت المكتبة الناقصة: {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ تم تثبيت {package} بنجاح.")
            except Exception as e:
                print(f"❌ فشل تثبيت {package}: {e}")

# تنفيذ التثبيت فوراً قبل أي استدعاء آخر
install_missing_libraries()
# -------------------------------------------------------

import asyncio
from pytgcalls import idle
import random
from pyrogram import Client
from pytgcalls import PyTgCalls
from bot import *
from pyromod import listen

# تشغيل البوت
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        # ملاحظة: تأكد أن start_zombiebot معرفة داخل ملف bot.py
        loop.run_until_complete(start_zombiebot())
    except Exception as e:
        print(f"❌ خطأ في التشغيل النهائي: {e}")
