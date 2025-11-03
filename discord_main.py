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

keep_alive()

if len(sys.argv) == 2:
    config = config.Config(config_location=sys.argv[1], key="discord_config")
else:
    config = config.Config(key="discord_config")

token = os.environ.get('DISCORD_API_KEY')

if not token:
    print("=" * 60)
    print("[ERROR] DISCORD_API_KEY environment variable not found!")
    print("[INFO] Please set the DISCORD_API_KEY secret in Replit:")
    print("  1. Click on 'Secrets' in the Tools panel (lock icon)")
    print("  2. Add a new secret with key: DISCORD_API_KEY")
    print("  3. Set the value to your Discord bot token")
    print("  4. Restart this workflow")
    print("=" * 60)
    print("[INFO] Web server running on port 5000. Waiting for API key...")
    while True:
        time.sleep(60)
else:
    config['api_key'] = token
    server = discord.Discord(config)
    print("Starting Bot...")
    taiiwobot.TaiiwoBot(server, config)
