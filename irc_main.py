import time
from taiiwobot import taiiwobot, irc, config

config = config.Config(key="irc_config")
server = irc.IRC(config)
taiiwobot.TaiiwoBot(server, config)
