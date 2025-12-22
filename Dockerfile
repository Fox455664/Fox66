FROM python:3.9-slim

# 1. تثبيت مكتبات النظام الضرورية (بما في ذلك ملفات X11 المفقودة و Redis)
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

# 2. تحديث أدوات التثبيت
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 3. تثبيت مكتبات بايثون (أضفت لك 'oldpyro' في القائمة)
RUN pip install --no-cache-dir \
    pyrogram==2.0.106 \
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
    flask

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

# 4. تشغيل Redis في الخلفية ثم تشغيل البوت
CMD redis-server --daemonize yes && python3 main.py
