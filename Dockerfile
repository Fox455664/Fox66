FROM python:3.9-slim-buster

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المتطلبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# الأمر لتشغيل تطبيقك (تأكد من أن اسم الملف main.py أو غيره حسب مشروعك)
CMD ["python", "main.py"]
