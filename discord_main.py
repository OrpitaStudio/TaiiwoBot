import time
from taiiwobot import taiiwobot, discord, config, util
import sys
import os  # <-- إضافة مهمة
from flask import Flask  # <-- إضافة
from threading import Thread  # <-- إضافة

# --- كود الويب سيرفر لإبقاء البوت مستمر ---
app = Flask('')

@app.route('/')
def home():
    return "TaiiwoBot is alive!"

def run_server():
  # Render يحدد البورت تلقائيًا عبر متغير PORT
  port = int(os.environ.get('PORT', 8080)) 
  app.run(host='0.0.0.0', port=port)

def keep_alive():
    # دالة لتشغيل السيرفر في "ثريد" (خيط) منفصل
    t = Thread(target=run_server)
    t.start()
# ----------------------------------------

# تحميل الكونفج كما هو في الكود الأصلي
if len(sys.argv) == 2:
    config = config.Config(config_location=sys.argv[1], key="discord_config")
else:
    config = config.Config(key="discord_config")

# [!!] أهم تعديل: قراءة التوكن من متغيرات البيئة في Render
# هذا الكود سيقوم بالكتابة فوق أي "api_key" موجودة في ملف config.json
# سنستخدم اسم 'DISCORD_API_KEY' كاسم للمتغير في Render
token = os.environ.get('DISCORD_API_KEY')

if not token:
    print("[ERROR] لم يتم العثور على 'DISCORD_API_KEY' في متغيرات البيئة!")
    # لا تضع التوكن هنا، سيتم إضافته في لوحة تحكم Render
else:
    # الكود هنا يضع التوكن الذي قرأه من Render
    # داخل الكونفج ليستخدمه البوت
    config['api_key'] = token


# use discord as our server protocol
# الكود الأصلي سيبحث عن config['api_key'] وسيجد القيمة التي وضعناها
server = discord.Discord(config) # ملف discord.py سيستخدم هذا الكونفج

# --- تشغيل السيرفر والبوت ---
keep_alive()  # <-- شغل الويب سيرفر أولاً في ثريد

print("Starting Bot...")
# Start the bot!
# هذا السطر سيشغل البوت في الثريد الرئيسي
taiiwobot.TaiiwoBot(server, config)
