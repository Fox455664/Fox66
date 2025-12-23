FROM python:3.9-slim

# 1. تثبيت مكتبات النظام الضرورية (التي تدعم الصوت والـ Redis)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    redis-server \
    build-essential \
    libx11-6 \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. تحديث أدوات التثبيت الأساسية
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 3. تثبيت جميع مكتبات بايثون المطلوبة (تم إضافة pytube هنا)
RUN pip install --no-cache-dir \
    pyrogram==2.0.106 \
    telethon \
    tgcrypto \
    ntgcalls==1.1.3 \
    py-tgcalls==1.1.6 \
    oldpyro \
    yt-dlp \
    youtube-search-python \
    youtube-search \
    aiohttp \
    Pillow \
    numpy \
    unidecode \
    aiofiles \
    pyromod \
    requests \
    redis \
    gTTS \
    pytz \
    kvsqlite \
    beautifulsoup4 \
    telegraph \
    wget \
    python-dotenv \
    lyricsgenius \
    flask \
    pytube

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

# 4. تشغيل خادم Redis في الخلفية ثم تشغيل البوت
CMD redis-server --daemonize yes && python3 main.py
