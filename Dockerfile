FROM python:3.9-slim

# 1. تثبيت مكتبات النظام الضرورية
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg git redis-server build-essential libx11-6 libgl1 libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. تحديث pip وتثبيت المكتبات الأساسية
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 3. تثبيت المكتبات المتاحة رسمياً
RUN pip install --no-cache-dir \
    pyrogram==2.0.106 telethon pytube flask oldpyro pyromod \
    tgcrypto ntgcalls==1.1.3 py-tgcalls==1.1.6 yt-dlp \
    youtube-search-python aiohttp Pillow numpy aiofiles \
    requests redis gTTS pytz kvsqlite beautifulsoup4 \
    telegraph wget python-dotenv lyricsgenius

# 4. تثبيت مكتبة pyrolistener مباشرة من GitHub (الحل النهائي للخطأ)
RUN pip install --no-cache-dir git+https://github.com/TeMeS-T/pyrolistener

COPY . .

# 5. تشغيل الـ Redis والسيرفر والبوت
CMD redis-server --daemonize yes && python3 main.py
