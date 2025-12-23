FROM python:3.9-slim

# تثبيت مكتبات النظام الضرورية
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg git redis-server build-essential libx11-6 libgl1 libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# تحديث pip وتثبيت كل المكتبات المطلوبة دفعة واحدة (أضفت pyrolistener هنا)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir \
    pyrogram==2.0.106 telethon pytube flask oldpyro pyromod pyrolistener \
    tgcrypto ntgcalls==1.1.3 py-tgcalls==1.1.6 yt-dlp \
    youtube-search-python aiohttp Pillow numpy aiofiles \
    requests redis gTTS pytz kvsqlite beautifulsoup4 \
    telegraph wget python-dotenv lyricsgenius

COPY . .

# تشغيل الـ Redis والسيرفر والبوت
CMD redis-server --daemonize yes && python3 main.py
