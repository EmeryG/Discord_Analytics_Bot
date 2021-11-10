import requests

DISCORD_API = 'https://discord.com/api/v8'
BOT_ID = '907693823407312896'

with open('bot_secret.txt', 'r') as file:
    BOT_SECRET = file.read().rstrip()
    
with open('bot_token.txt', 'r') as file:
    BOT_TOKEN = file.read().rstrip()

headers = { 'authorization': f'Bot {BOT_TOKEN}' }

class Guild:
    def __init__(self, guild_id):
        self.guild_id = guild_id
    
    def get_req(self, extension):
        r = requests.get(DISCORD_API + f'/guilds/{self.guild_id}/{extension}', headers=headers)
        r.raise_for_status()
        return r.json()
    
    def get_users(self):
        return self.get_req('users')

    def get_roles(self):
        return self.get_req('roles')

with open('server_id.txt', 'r') as file:
    DEFAULT_GUILD = Guild(file.read().rstrip())