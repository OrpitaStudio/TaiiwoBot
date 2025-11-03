import time
from taiiwobot import taiiwobot, discord, config, util
import sys
import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "TaiiwoBot is alive!"

def run_server():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_server)
    t.start()

if len(sys.argv) == 2:
    config = config.Config(config_location=sys.argv[1], key="discord_config")
else:
    config = config.Config(key="discord_config")

token = os.environ.get('DISCORD_API_KEY')

if not token:
    print("[ERROR] DISCORD_API_KEY environment variable not found!")
    print("[INFO] Please set the DISCORD_API_KEY secret in Replit")
else:
    config['api_key'] = token

server = discord.Discord(config)

keep_alive()

print("Starting Bot...")
taiiwobot.TaiiwoBot(server, config)
