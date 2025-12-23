import os
import sys
import subprocess

# --- كود التثبيت التلقائي للمكتبات الناقصة ---
def install_missing_libraries():
    # القائمة التي تسبب لك مشاكل دائماً
    required_packages = ["telethon", "oldpyro"]
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"جاري تثبيت المكتبة الناقصة: {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"تم تثبيت {package} بنجاح.")

# تنفيذ التثبيت قبل استدعاء باقي الملفات
install_missing_libraries()
# ------------------------------------------

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
        loop.run_until_complete(start_zombiebot())
    except Exception as e:
        print(f"حدث خطأ أثناء التشغيل: {e}")
