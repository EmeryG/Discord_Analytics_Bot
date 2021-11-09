import json

DISCORD_API = "https://discord.com/api"
BOT_ID = "907693823407312896"

with open('bot_secret.txt', 'r') as file:
    BOT_SECRET = file.read().rstrip()

print(BOT_SECRET)