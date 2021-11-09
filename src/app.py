import json, requests

DISCORD_API = "https://discord.com/api/v8"
BOT_ID = "907693823407312896"

with open('bot_secret.txt', 'r') as file:
    BOT_SECRET = file.read().rstrip()

def get_token():
    data = {
        'grant_type': 'client_credentials',
        'scope': 'identify connections'
    }
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    r = requests.post(DISCORD_API + '/oauth2/token', data=data, headers=headers, auth=(BOT_ID, BOT_SECRET))
    r.raise_for_status()
    return r.json()

print(get_token())
    