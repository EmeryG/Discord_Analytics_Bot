import json, requests

DISCORD_API = 'https://discord.com/api/v8'
BOT_ID = '907693823407312896'

with open('bot_secret.txt', 'r') as file:
    BOT_SECRET = file.read().rstrip()
    
with open('bot_token.txt', 'r') as file:
    BOT_TOKEN = file.read().rstrip()

def get_users(guild_id):
    headers = {
        'authorization': f'Bot {BOT_TOKEN}'
    }
    
    r = requests.get(DISCORD_API + f'/guilds/{guild_id}/members', headers=headers)

    r.raise_for_status()
    
    return r.json()

print(get_users(819950265552601091))